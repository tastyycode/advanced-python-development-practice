import socket
import sys

import click
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


@click.command(help='Displays the values of the sensors')
def show_sensors():
    click.echo("Python version: {0.major}.{0.minor}".format(python_version()))
    for address in ip_addresses():
        click.echo("IP addresses: {0[1]} ({0[0]})".format(address))
    click.echo("CPU Load: {:.1f}".format(cpu_load()))
    click.echo("RAM Available: {} MiB".format(ram_available() / (1024**2)))
    click.echo("AC Connected: {}".format(ac_connected()))


if __name__ == '__main__':
    show_sensors(sys.argv)
