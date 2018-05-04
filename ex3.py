#!/usr/bin/env python
"""

Using NAPALM retreive 'get_bgp_neighbors' from pynet-rtr1. Parse the returned data structure to and
verify that the BGP peer to 10.220.88.38 is in the established state ('is_up' field in the NAPALM
returned data structure).
"""
from __future__ import print_function, unicode_literals
from pprint import pprint
from napalm import get_network_driver
from my_devices import pynet_rtr1

def main():
    for a_device in (pynet_rtr1,):
        device_type = a_device.pop('device_type')
        driver = get_network_driver(device_type)
        device = driver(**a_device)

        print()
        print(">>>Device open")
        device.open()

        print("-"*50)
        bgp_info = device.get_bgp_neighbors()
        hostname = a_device['hostname']
        print("{hostname}:\n".format(hostname=hostname))
        for a_peer in bgp_info['global']['peers']:
            peer_info = bgp_info['global']['peers'][a_peer]
            print("{}' is up? {is_up}".format(a_peer, **peer_info))
        #pprint(bgp_info)
        print()
    print()


if __name__ == "__main__":
    main()
