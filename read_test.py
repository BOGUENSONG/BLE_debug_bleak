import asyncio
import sys
import argparse
from bleak import BleakScanner
from bleak import BleakClient

async def find_by_name(name: str):
    global mac_addr
    devices = await BleakScanner.discover()
    print("found [%d] devices!" % len(devices))
    for d in devices:
        print("- %s (name: %s)" % (d.address, d.name))
        if (d.name == name):
            return d.address
    return None

async def print_services(mac_addr: str, service_uuid: str, characteristic_uuid: str, loop: asyncio.AbstractEventLoop):
    service_flag = 0
    char_flag = 0
    connect_flag = 0
    try:
        async with BleakClient(mac_addr, loop=loop, timeout=5.0) as client:
            connect_flag = 1
            svcs = client.services
            for service in svcs:
                if (service.uuid == service_uuid):
                    print("Service Found!")
                    service_flag = 1
                    for char in service.characteristics:
                        if (char.uuid == characteristic_uuid):
                            print("Characteristic Found! Read Start")
                            char_flag = 1
                            read = await client.read_gatt_char(characteristic_uuid)
                            print(read)
                            break
    except:
        print("not connected T.T please restart!!!!")
    if ( (not service_flag) and connect_flag):
        print("There is No Service : " + SERVICE_UUID)
    if ( (not char_flag) and connect_flag):
        print("There is No CHARACTERISTIC_UUID : " + CHARACTERISTIC_UUID)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('name', type=str, help='Device name')
    parser.add_argument('service_uuid', type=str, help='Service UUID')
    parser.add_argument('characteristic_uuid', type=str, help='Characteristic UUID')

    args = parser.parse_args(sys.argv[1:])

    loop = asyncio.get_event_loop()
    mac_addr = loop.run_until_complete(find_by_name(args.name))

if (mac_addr is not None) :
    print("Find! Connect start : " + mac_addr)
    loop.run_until_complete(print_services(mac_addr, args.service_uuid, args.characteristic_uuid, loop))
else:
    print("Sorry, There is No '%s'." % args.name)
