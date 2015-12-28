from netifaces import interfaces, ifaddresses, AF_INET
import requests
import json
from uuid import uuid5

def getLocalAddesses():

    ifaces = dict()
    for ifaceName in interfaces():
        addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr':'No IP addr'}] )]
        if ', '.join(addresses) is not 'No IP addr':
            ifaces[str(ifaceName)] = ', '.join(addresses)

    return ifaces


def getinetAddress():
    jsonip = json.loads(requests.get('http://jsonip.com').text)
    return jsonip['ip']

def getCommands():
    # some callback