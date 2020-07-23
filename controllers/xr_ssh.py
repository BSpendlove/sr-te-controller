from netmiko import ConnectHandler, NetMikoAuthenticationException, NetMikoTimeoutException
from controllers.textfsm_extractor import textfsm_extractor
import env_file

class CiscoXRAPI:
    def __init__(self, ip, port=22, device_type="cisco_xr"):
        self.ip = ip
        self.port = port
        self.device_type = device_type
        self.creds = env_file.get(path="env/netmiko")

        self.netmiko_creds = {
            "ip": self.ip,
            "port": self.port,
            "device_type": self.device_type,
            "username": self.creds["SSH_USERNAME"],
            "password": self.creds["SSH_PASSWORD"],
            "secret": self.creds["SSH_SECRET"]
        }

        self.ssh_session = None

    def get_hostname(self):
        return self.ssh_session.base_prompt

    def connect(self):
        try:
            self.ssh_session = ConnectHandler(**self.netmiko_creds)
            return {"error": False}
        except NetMikoAuthenticationException:
            return {"error": True, "message": "Netmiko Authentication Exception."}
        except NetMikoTimeoutException:
            return {"error": True, "message": "Netmiko Timeout Exception."}

    def get_isis_neighbors(self, textfsm=True):
        cmd = "show isis neighbors"
        output = self.ssh_session.send_command(cmd)

        if textfsm:
            neighbors = textfsm_extractor("cisco_xr_show_isis_neighbors", output)
            return {"total": len(neighbors), "isis_neighbors": neighbors}
        
        return output

    def get_isis_database(self, textfsm=True):
        cmd = "show isis database"
        output = self.ssh_session.send_command(cmd)

        if textfsm:
            lsps = textfsm_extractor("cisco_xr_show_isis_database", output)
            return {"total": len(lsps), "lsp_entries": lsps}
