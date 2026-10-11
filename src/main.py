
import logging
from pathlib import Path

from network_device import NetworkDevice
from parser_utils import parse_json, parse_yaml, parse_xml, parse_csv

ROOT = Path(__file__).resolve().parent.parent
LOG_DIR = ROOT / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    filename=str(LOG_DIR / "lab.log"),
    level=logging.INFO,
    format="%(message)s",
    force=True,
)


def main():
    logging.info("LAB1_START")
    logging.info("[STEP 2] Dev Container Started")

    devices = parse_json(ROOT / "data/devices.json")
    interfaces = parse_yaml(ROOT / "data/interfaces.yaml")
    inventory = parse_csv(ROOT / "data/inventory.csv")
    vlans = parse_xml(ROOT / "data/vlans.xml")

    for device in devices:
        device_obj = NetworkDevice(
            device["hostname"],
            device["ip"],
            device["type"],
        )
        device_obj.summarize()

    for interface in interfaces["interfaces"]:
        msg = f"Interface {interface['name']} is {interface['status']}"
        print(msg)
        logging.info("INTERFACE_MSG: %s", msg)

    for device in devices:
        msg = f"Device {device['hostname']} is a {device['type']}"
        print(msg)
        logging.info("DEVICE_MSG: %s", msg)

    for vlan in vlans.findall("vlan"):
        msg = f"VLAN {vlan.find('id').text} is the {vlan.find('name').text}"
        print(msg)
        logging.info("VLAN_MSG: %s", msg)

    logging.info("LAB1_END")


if __name__ == "__main__":
    main()



