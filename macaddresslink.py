# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, with_statement

import sys

import json
import pprint

import requests
import netifaces

__author__ = 'Shane R. Spencer'
__author_email__ = 'shane@bogomip.com'
__license__ = 'MIT'
__copyright__ = '2014 Shane R. Spencer'
__version__ = '0.0.1'
__url__ = 'https://github.com/MacAddressLink/macaddresslink.py'
__description__ = 'macaddress.link client'

###############################################################################
## Main

def main():

    address_set = {}

    for interface in netifaces.interfaces():

        if netifaces.AF_LINK in netifaces.ifaddresses(interface):
            addresses = [x['addr'] for x in netifaces.ifaddresses(interface)[netifaces.AF_LINK]]
            address = addresses[0]
        else:
            continue

        if address == '00:00:00:00:00:00':
            continue

        address_set[address] = {}

        if netifaces.AF_INET in netifaces.ifaddresses(interface):
            address_set[address]['ipv4'] = [x['addr'] for x in netifaces.ifaddresses(interface)[netifaces.AF_INET]]

        if netifaces.AF_INET6 in netifaces.ifaddresses(interface):
            address_set[address]['ipv6'] = [x['addr'] for x in netifaces.ifaddresses(interface)[netifaces.AF_INET6]]
        
    r = requests.post('http://update.direct.macaddress.link/', data=json.dumps(address_set))
    pprint.pprint(r.json())

if __name__ == '__main__':
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        pass
