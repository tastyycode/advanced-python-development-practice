import socket
import sys

import psutil

HELP_TEXT = """usage: python {program_name:s}

Displays the values of the sensors

Options and arguments:
--help:     Display this message"""


def python_version():
    return sys.version_info


def ip_addresses():
    hostname = socket.gethostname()
    addresses = socket.getaddrinfo(hostname, None)

    address_info = []
    for address in addresses:
        address_info.append((address[0].name, address[4][0]))
    return address_info


def cpu_load():
    return psutil.cpu_percent(interval=0.1)


def ram_available():
    return psutil.virtual_memory().available


def ac_connected():
    return psutil.sensors_battery().power_plugged


def show_sensors():
    print("Python version: {0.major}.{0.minor}".format(python_version()))
    for address in ip_addresses():
        print("IP addresses: {0[1]} ({0[0]})".format(address))
    print("CPU Load: {:.1f}".format(cpu_load()))
    print("RAM Available: {} MiB".format(ram_available() / (1024**2)))
    print("AC Connected: {}".format(ac_connected()))

def command_line(argv):
    program_name, *arguments = argv
    if not arguments:
        show_sensors()
    elif arguments and arguments[0] == '--help':
        print(HELP_TEXT.format(program_name=program_name))
        return
    else:
        raise ValueError('Unkown arguments {}'.format(arguments))


if __name__ == '__main__':
    command_line(sys.argv)