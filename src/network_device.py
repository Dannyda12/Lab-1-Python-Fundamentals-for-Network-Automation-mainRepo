import logging


class NetworkDevice:
    def __init__(self, hostname, ip_address, device_type):
        self.hostname = hostname
        self.ip_address = ip_address
        self.device_type = device_type

    def summarize(self):
        summary = (
            f"DEVICE_SUMMARY: {self.hostname} "
            f"{self.device_type} {self.ip_address} "
        )
        print(summary)
        logging.info(summary)
        return summary
    
    

        