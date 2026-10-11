import logging
from pathlib import Path

from src.network_device import NetworkDevice
from src.parser_utils import parse_json, parse_yaml, parse_xml, parse_csv


ROOT = Path(__file__).resolve().parent
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

    # Parse the four data files
    devices = parse_json(ROOT / "data" / "devices.json")
    interfaces = parse_yaml(ROOT / "data" / "interfaces.yaml")
    inventory = parse_csv(ROOT / "data" / "inventory.csv")
    vlans = parse_xml(ROOT / "data" / "vlans.xml")

    # Summarize network devices
    for device in devices:
        network_device = NetworkDevice(
            device["hostname"],
            device["ip"],
            device["type"],
        )
        network_device.summarize()

    # Display interface information
    for interface in interfaces.get("interfaces", []):
        message = (
            f"Interface {interface['name']} is "
            f"{interface['status']}"
        )
        print(message)
        logging.info("INTERFACE_MSG: %s", message)

    # Display device information
    for device in devices:
        message = f"Device {device['hostname']} is a {device['type']}"
        print(message)
        logging.info("DEVICE_MSG: %s", message)

    # Display VLAN information
    for vlan in vlans.findall("vlan"):
        vlan_id = vlan.findtext("id")
        vlan_name = vlan.findtext("name")
        message = f"VLAN {vlan_id} is the {vlan_name}"
        print(message)
        logging.info("VLAN_MSG: %s", message)

    logging.info("LAB1_END")


if __name__ == "__main__":
    main()


