# Author: Alessandra Fais
# Mat: 481017
# Computer Science and Networking
# Advanced Programming 2016/17
# Homework 2

from ipaddress import ip_address
from constants import colors as col
import sys
import switch
import control
import input_interface_simulator


def main():

    def print_list(l):
        [print(str(x) + '  ', end='') for x in l]
        print()

    # Take from the user the input and output interfaces of the switch and the network
    input_interfaces = [int(x) for x in input('Insert a list of input interfaces (ex. 1 2 3):\t').split()]
    output_interfaces = [int(x) for x in input('Insert a list of output interfaces (ex. 1 2 3):\t').split()]
    ip_address1 = ip_address(input('Insert the first ip address of the network (ex. 192.168.0.1):\t'))
    ip_address2 = ip_address(input('Insert the last ip address of the network (ex. 192.168.0.10):\t'))
    ip_addresses = [ip_address(ip) for ip in range(int(ip_address1), int(ip_address2))]

    print(col.GREEN + '\nSetting up the switch, the controller and the input interface simulator...' + col.ENDC)

    print(col.GREEN + 'Input interfaces: ' + col.ENDC, end='')
    print_list(input_interfaces)
    print(col.GREEN + 'Output interfaces: ' + col.ENDC, end='')
    print_list(output_interfaces)
    print(col.GREEN + 'Network: ' + col.ENDC, end='')
    print_list(ip_addresses)
    print()

    # Create the generator of the packets
    pg = input_interface_simulator.InputInterfaceSimulator(input_interfaces, ip_addresses)

    # Create the switch and the controller
    c = control.Controller(ip_addresses)
    s = switch.Switch(output_interfaces, pg.gen(), c, True)  # TODO pass gen() or gen?

    s.main_loop()
    return 0

if __name__ == "__main__":
    sys.exit(main())
