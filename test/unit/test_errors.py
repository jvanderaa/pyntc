import pytest

from pyntc import errors as ntc_errors


def test_ntc_error():
    error_message = "This is an error message"
    error_class = ntc_errors.NTCError
    error = error_class(error_message)
    with pytest.raises(error_class) as err:
        raise error

    assert err.value.message == error_message


def test_unsupported_device_error():
    error_message = "new-vendor is not a supported vendor."
    error_class = ntc_errors.UnsupportedDeviceError
    error = error_class("new-vendor")
    with pytest.raises(error_class) as err:
        raise error

    assert err.value.message == error_message


def test_device_name_not_found_error():
    error_message = "Name new-host not found in ntc.conf. The file may not exist."
    error_class = ntc_errors.DeviceNameNotFoundError
    error = error_class("new-host", "ntc.conf")
    with pytest.raises(error_class) as err:
        raise error

    assert err.value.message == error_message


def test_conf_file_not_found_error():
    error_message = "NTC Configuration file ntc.conf could not be found."
    error_class = ntc_errors.ConfFileNotFoundError
    error = error_class("ntc.conf")
    with pytest.raises(error_class) as err:
        raise error

    assert err.value.message == error_message


def test_command_error():
    error_message = "Command fail was not successful: '% invalid command'"
    error_class = ntc_errors.CommandError
    error = error_class("fail", "'% invalid command'")
    with pytest.raises(error_class) as err:
        raise error

    assert err.value.message == error_message


def test_command_list_error():
    error_message = (
        "\n"
        "Command fail failed with message: '% invalid command'\n"
        "Command List: \n"
        "\tcommand 1\n"
        "\tfail\n"
        "\tcommand 2\n"
    )
    error_class = ntc_errors.CommandListError
    error = error_class(
        ["command 1", "fail", "command 2"],
        "fail",
        "'% invalid command'",
    )
    with pytest.raises(error_class) as err:
        raise error

    assert err.value.message == error_message


def test_feature_not_found_error():
    error_message = "vlans feature not found for ios device type."
    error_class = ntc_errors.FeatureNotFoundError
    error = error_class("vlans", "ios")
    with pytest.raises(error_class) as err:
        raise error

    assert err.value.message == error_message


def test_file_system_not_found_error():
    error_message = 'Unable to parse "dir" command to identify the default file system on host1.'
    error_class = ntc_errors.FileSystemNotFoundError
    error = error_class("host1", "dir")
    with pytest.raises(error_class) as err:
        raise error

    assert err.value.message == error_message


def test_reboot_timeout_error():
    error_message = "Unable to reconnect to host1 after 3600 seconds"
    error_class = ntc_errors.RebootTimeoutError
    error = error_class("host1", 3600)
    with pytest.raises(error_class) as err:
        raise error

    assert err.value.message == error_message


def test_not_enough_free_space_error():
    error_message = "host1 does not meet the minimum disk space requirements of 1000"
    error_class = ntc_errors.NotEnoughFreeSpaceError
    error = error_class("host1", 1000)
    with pytest.raises(error_class) as err:
        raise error

    assert err.value.message == error_message


def test_os_install_error():
    error_message = "host1 was unable to boot into v1.2.3"
    error_class = ntc_errors.OSInstallError
    error = error_class("host1", "v1.2.3")
    with pytest.raises(error_class) as err:
        raise error

    assert err.value.message == error_message


def test_ntc_file_not_found_error():
    error_message = "v1.2.3.bin was not found in flash on host1"
    error_class = ntc_errors.NTCFileNotFoundError
    error = error_class("host1", "v1.2.3.bin", "flash")
    with pytest.raises(error_class) as err:
        raise error

    assert err.value.message == error_message


def test_wlan_enable_error():
    error_message = "Unable to enable WLAN IDs on host1\nExpected: [1, 2, 3]\nFound:    [1, 2]\n"
    error_class = ntc_errors.WLANEnableError
    error = error_class("host1", [3, 2, 1], [2, 1])
    with pytest.raises(error_class) as err:
        raise error

    assert err.value.message == error_message


def test_wlan_disable_error():
    error_message = "Unable to disable WLAN IDs on host1\nExpected: [1, 2, 3]\nFound:    [1, 2]\n"
    error_class = ntc_errors.WLANDisableError
    error = error_class("host1", [3, 2, 1], [2, 1])
    with pytest.raises(error_class) as err:
        raise error

    assert err.value.message == error_message
