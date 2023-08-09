"""Module providing the SSH functionality."""
import paramiko

class Remote():
    def __init__(self, hostname : str , os : str) -> None:
        self.hostname = hostname
        self.port = 3022
        self.os = os
        self.ssh = paramiko.SSHClient()
    
    def connect(self, user_name : str, password : str) -> None:
        try:
            self.ssh.load_system_host_keys()
            self.ssh.connect(hostname=self.hostname, port=self.port, username=user_name, password=password)
        except:
            print(f"Cannot establish conenction to {self.hostname}")
    
    def execute(self, COMMAND : str) -> tuple:
        if self.ssh.get_transport().is_active():
            (stdin, stdout, stderr) = self.ssh.exec_command(COMMAND)
            return (stdin, stdout, stderr)
        else:
            print(f"Conenction to {self.hostname} is dead.")
    
    def close_connection(self):
        self.ssh.close()