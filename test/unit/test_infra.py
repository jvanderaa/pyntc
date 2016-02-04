import unittest
import os
import mock

from pyntc import ntc_device, ntc_device_by_name
from pyntc.errors import UnsupportedDeviceError, ConfFileNotFoundError
from pyntc.devices import supported_devices, DEVICE_CLASS_KEY
from pyntc.devices import EOSDevice, NXOSDevice, IOSDevice


BAD_DEVICE_TYPE = '238nzsvkn3981'
FIXTURES_DIR = os.path.join(os.path.dirname(__file__), '..', 'fixtures')


class TestInfra(unittest.TestCase):

    @mock.patch.object(IOSDevice, 'open')
    def test_device_creation(self, my_open):
        for device_type in supported_devices:
            device = ntc_device(device_type, 'host', 'user', 'pass')
            self.assertIsInstance(
                device, supported_devices[device_type][DEVICE_CLASS_KEY])

    def test_unsupported_device(self):
        with self.assertRaises(UnsupportedDeviceError):
            ntc_device(BAD_DEVICE_TYPE)

    @mock.patch.object(IOSDevice, 'open')
    def test_device_by_name(self, my_open):
        config_filepath = os.path.join(FIXTURES_DIR, '.ntc.conf.sample')

        nxos_device = ntc_device_by_name('test_nxos', filename=config_filepath)
        self.assertIsInstance(nxos_device, NXOSDevice)

        eos_device = ntc_device_by_name('test_eos', filename=config_filepath)
        self.assertIsInstance(eos_device, EOSDevice)

        ios_device = ntc_device_by_name('test_ios', filename=config_filepath)
        self.assertIsInstance(ios_device, IOSDevice)

    def test_no_conf_file(self):
        with self.assertRaises(ConfFileNotFoundError):
            ntc_device_by_name('test_bad_device', filename='/bad/file/path')