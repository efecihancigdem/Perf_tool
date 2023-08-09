"""Module providing the SSH functionality."""
import paramiko

class remote():
    def __init__(self, hostname : str , OS : str) -> None:
        self.hostname = hostname
        self.port = 3022
        self.OS = OS
        self.connection = paramiko.SSHClient()
    
    def connect(self, USER_NAME : str, PASSWORD : str) -> None:
        try:
            self.connection.load_system_host_keys()
            self.connection.connect(hostname=self.hostname, port=self.port, username=USER_NAME, password=PASSWORD)
        except:
            print(f"Cannot establish conenction to {self.hostname}")
    
    def execute(self, COMMAND : str) -> tuple:
        if self.connection.get_transport().is_active():
            (stdin, stdout, stderr) = self.connection.exec_command(COMMAND)
            return (stdin, stdout, stderr)
        else:
            print(f"Conenction to {self.hostname} is dead.")
    
    def close_connection(self):
        self.connection.close()