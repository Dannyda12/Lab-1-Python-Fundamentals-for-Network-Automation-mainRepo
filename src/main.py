import logging

from network_device import NetworkDevice
from parser_utils import parse_json, parse_yaml, parse_xml, parse_csv

logging.basicConfig(
    filename="logs/lab.log",
    level=logging.INFO,
    format="%(message)s",
)

def main():
    logging.info("DEV_CONTAINER_STARTED")
    devices = parse_json("data/devices.json")
    devices = parse_json("data/devices.json")
    interfaces = parse_yaml("data/interfaces.yaml")
    inventory = parse_csv("data/inventory.csv")
    vlans = parse_xml("data/vlans.xml")


    for device in devices:
        device_obj = NetworkDevice(
            device["hostname"],
            device["ip"],
            device["type"],
        )
        device_obj.summarize()
        logging.info("INTERFACE_MESSAGE")

    for interface in interfaces["interfaces"]:
        msg = F"INTERFACE_MESSAGE: {interface['name']}  {interface['status']}"
        print(msg)
        logging.info(msg)

    for device in devices:
        msg = F"DEVICE_MESSAGE: {device['hostname']}  {device['ip']}  {device['type']}"
        print(msg)
        logging.info(msg)

    for vlan in vlans.findall("vlan"):
        msg = f"VLAN_MESSAGE: {vlan.find('id').text} {vlan.find('name').text}"
        print(msg)
        logging.info(msg)

if __name__ == "__main__":
    logging.info("LAB1_START")
    main()
    logging.info("LAB1_END")
    


