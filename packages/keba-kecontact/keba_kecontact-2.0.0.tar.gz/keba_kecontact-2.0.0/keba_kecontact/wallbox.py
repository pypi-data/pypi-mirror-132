from abc import ABC
import logging
import json
import string
import asyncio
import string

_LOGGER = logging.getLogger(__name__)


class WallboxDeviceInfo(ABC):
    def __init__(self, host, device_id, manufacturer, model, sw_version):
        self.device_id = device_id
        self.manufacturer = manufacturer
        self.model = model
        self.sw_version = sw_version
        self.webconfigurl = f"http://{host}"
        self.host = host

    def __str__(self):
        return f"{self.manufacturer} - {self.model} (device_id: {self.device_id}) - {self.sw_version} running at {self.host}"


class Wallbox(ABC):
    def __init__(
        self,
        keba,
        device_info: WallboxDeviceInfo,
        loop=None,
        refresh_interval=5,
        refresh_interval_fast_polling=1,
    ):
        """Initialize charging station connection."""
        # super().__init__(host, self.hass_callback)

        self._loop = asyncio.get_event_loop() if loop is None else loop

        self._keba = keba
        self.device_info = device_info
        self.data = dict()

        self._callback = None

        # Internal variables
        self._refresh_interval = refresh_interval
        self._refresh_interval_fast_polling = refresh_interval_fast_polling

        self._fast_polling_count_max = int(
            self._refresh_interval * 2 / self._refresh_interval_fast_polling
        )
        self._fast_polling_count = self._fast_polling_count_max

        self._polling_task = None
        self._polling_task = self._loop.create_task(self._periodic_request())

    def set_callback(self, callback):
        self._callback = callback

    def get_value(self, key):
        if key is None:
            return self.data
        else:
            try:
                value = self.data[key]
                return value
            except KeyError:
                return None

    async def datagram_received(self, data):
        """Handle received datagram."""
        _LOGGER.debug("Datagram received, starting to process.")
        self.data["Online"] = True
        decoded_data = data.decode()

        if "TCH-OK :done" in decoded_data:
            _LOGGER.debug("Command accepted: %s", decoded_data.rstrip())
            return True

        if "TCH-ERR" in decoded_data:
            _LOGGER.warning("Command rejected: %s", decoded_data.rstrip())
            return False

        json_rcv = json.loads(data.decode())

        # Prepare received data
        if "ID" in json_rcv:
            if json_rcv["ID"] == "2":
                try:
                    json_rcv["Max curr"] = json_rcv["Max curr"] / 1000.0
                    json_rcv["Curr HW"] = json_rcv["Curr HW"] / 1000.0
                    json_rcv["Curr user"] = json_rcv["Curr user"] / 1000.0
                    json_rcv["Curr FS"] = json_rcv["Curr FS"] / 1000.0
                    json_rcv["Curr timer"] = json_rcv["Curr timer"] / 1000.0
                    json_rcv["Setenergy"] = round(json_rcv["Setenergy"] / 10000.0, 2)

                    # Extract plug state
                    plug_state = json_rcv["Plug"]
                    json_rcv["Plug_plugged"] = plug_state > 3
                    json_rcv["Plug_wallbox"] = plug_state > 0
                    json_rcv["Plug_locked"] = plug_state == 3 | plug_state == 7
                    json_rcv["Plug_EV"] = plug_state > 4

                    # Extract charging state
                    state = json_rcv["State"]
                    json_rcv["State_on"] = state == 3
                    if state is not None:
                        switcher = {
                            0: "starting",
                            1: "not ready for charging",
                            2: "ready for charging",
                            3: "charging",
                            4: "error",
                            5: "authorization rejected",
                        }
                        json_rcv["State_details"] = switcher.get(
                            state, "State undefined"
                        )

                    # Extract failsafe details
                    json_rcv["FS_on"] = json_rcv["Tmo FS"] > 0
                    self.data.update(json_rcv)
                except KeyError:
                    _LOGGER.warning(
                        "Could not extract report 2 data for KEBA charging station"
                    )
                return True
            elif json_rcv["ID"] == "3":
                try:
                    json_rcv["I1"] = json_rcv["I1"] / 1000.0
                    json_rcv["I2"] = json_rcv["I2"] / 1000.0
                    json_rcv["I3"] = json_rcv["I3"] / 1000.0
                    json_rcv["P"] = round(json_rcv["P"] / 1000000.0, 2)
                    json_rcv["PF"] = json_rcv["PF"] / 1000.0
                    json_rcv["E pres"] = round(json_rcv["E pres"] / 10000.0, 2)
                    json_rcv["E total"] = round(json_rcv["E total"] / 10000.0, 2)
                    self.data.update(json_rcv)
                except KeyError:
                    _LOGGER.warning(
                        "Could not extract report 3 data for KEBA charging station"
                    )
            elif json_rcv["ID"] == "100":
                try:
                    json_rcv["E start"] = round(json_rcv["E start"] / 10000.0, 2)
                    json_rcv["E pres"] = round(json_rcv["E pres"] / 10000.0, 2)
                    self.data.update(json_rcv)
                except KeyError:
                    _LOGGER.warning(
                        "Could not extract report 100 data for KEBA charging station"
                    )
            else:
                _LOGGER.debug("Report ID not known/implemented")
        else:
            _LOGGER.debug("No ID in response from Keba charging station")
            return False

        # Join data to internal data store and send it to the callback function
        if self._callback is not None:
            _LOGGER.debug("Execute callback")
            self._callback(self, self.data)

    ####################################################
    #            Data Polling Management               #
    ####################################################

    async def _send(self, payload: str, fast_polling: bool = False):
        await self._keba.send(self, payload)
        if fast_polling:
            _LOGGER.debug("Fast polling enabled")
            self._fast_polling_count = 0
            self._polling_task.cancel()
            self._polling_task = self._loop.create_task(self._periodic_request())

    async def request_data(self):
        """Send request for KEBA charging station data.

        This function requests report 2, report 3 and report 100.
        """
        await self._send("report 2")
        await self._send("report 3")
        await self._send("report 100")

    async def _periodic_request(self):
        """Send  periodic update requests."""

        await self.request_data()

        sleep = self._refresh_interval
        if self._fast_polling_count < self._fast_polling_count_max:
            self._fast_polling_count += 1
            sleep = self._refresh_interval_fast_polling

        _LOGGER.debug("Periodic data request executed, now wait for %s seconds", sleep)
        await asyncio.sleep(sleep)

        self._polling_task = self._loop.create_task(self._periodic_request())
        _LOGGER.debug("Periodic data request rescheduled")

    ####################################################
    #                   Functions                      #
    ####################################################

    async def set_failsafe(self, timeout=30, fallback_value=6, persist=0):
        """Send command to activate failsafe mode on KEBA charging station.
        This function sets the failsafe mode. For deactivation, all parameters must be 0.
        """
        if (timeout < 10 and timeout != 0) or timeout > 600:
            raise ValueError(
                "Failsafe timeout must be between 10 and 600 seconds or 0 for deactivation."
            )

        if (fallback_value < 6 and fallback_value != 0) or fallback_value > 63:
            raise ValueError(
                "Failsafe fallback value must be between 6 and 63 A or 0 to stop charging."
            )

        if persist not in [0, 1]:
            raise ValueError("Failsafe persist must be 0 or 1.")

        await self._send(
            "failsafe "
            + str(timeout)
            + " "
            + str(fallback_value * 1000)
            + " "
            + str(persist),
            fast_polling=True,
        )

    async def set_ena(self, ena):
        """Start a charging process."""
        if not isinstance(ena, bool):
            raise ValueError("Enable parameter must be True or False.")

        await self._send("ena " + str(1 if ena else 0), fast_polling=True)

    async def set_current(self, current, delay=0):
        """Send command to set current limit on KEBA charging station.
        This function sets the current limit in A after a given delay in seconds. 0 A stops the charging process similar to ena 0.
        """
        if (
            not isinstance(current, (int, float))
            or (current < 6 and current != 0)
            or current >= 63
        ):
            raise ValueError(
                "Current must be int or float and value must be above 6 and below 63 A."
            )

        if not isinstance(delay, int) or delay < 0 or delay >= 860400:
            raise ValueError(
                "Delay must be int and value must be between 0 and 860400 seconds."
            )

        await self._send("currtime " + str(current * 1000) + " " + str(delay))

    async def set_energy(self, energy=0):
        """Send command to set energy limit on KEBA charging station.
        This function sets the energy limit in kWh. For deactivation energy should be 0.
        """
        if (
            not isinstance(energy, (int, float))
            or (energy < 1 and energy != 0)
            or energy >= 10000
        ):
            raise ValueError(
                "Energy must be int or float and value must be above 0.0001 kWh and below 10000 kWh."
            )

        await self._send("setenergy " + str(energy * 10000), fast_polling=True)

    async def set_output(self, out: int):
        """Start a charging process."""
        if not isinstance(out, int) or out < 0 or (out > 1 and out < 10) or out > 150:
            raise ValueError("Output parameter must be True or False.")

        await self._send("output " + str(out))

    async def start(
        self, rfid, rfid_class="01010400000000000000"
    ):  # Default color white
        """Authorize a charging process with predefined RFID tag."""
        if not all(c in string.hexdigits for c in rfid) or len(rfid) > 16:
            raise ValueError("RFID tag must be a 8 byte hex string.")

        if not all(c in string.hexdigits for c in rfid_class) or len(rfid) > 20:
            raise ValueError("RFID class tag must be a 10 byte hex string.")

        await self._send("start " + rfid + " " + rfid_class, fast_polling=True)

    async def stop(self, rfid: str):
        """De-authorize a charging process with predefined RFID tag."""
        if not all(c in string.hexdigits for c in rfid) or len(rfid) > 16:
            raise ValueError("RFID tag must be a 8 byte hex string.")

        await self._send("stop " + rfid, fast_polling=True)

    async def display(self, text: str, mintime: int = 2, maxtime: int = 10):
        """Show a text on the display."""
        if not isinstance(mintime, (int, float)) or not isinstance(
            maxtime, (int, float)
        ):
            raise ValueError("Times must be int or float.")

        if mintime < 0 or mintime > 65535 or maxtime < 0 or maxtime > 65535:
            raise ValueError("Times must be between 0 and 65535")

        await self._send(
            "display 1 "
            + str(int(round(mintime)))
            + " "
            + str(int(round(maxtime)))
            + " 0 "
            + text[0:23]
        )

    async def unlock_socket(self):
        """Unlock the socket.
        For this command you have to disable the charging process first. Afterwards you can unlock the socket.
        """
        await self._send("unlock")
