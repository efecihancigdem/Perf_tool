"""Module providing the SSH functionality."""
import paramiko

class Remote():
    """Remote Class"""
    def __init__(self, hostname : str) -> None:
        """Function initng the object."""
        self.hostname = hostname
        self.port = 3022
        self.ssh = paramiko.SSHClient()
        return None

    def connect(self, user_name : str, password : str) -> None:
        """Function creates ssh connection."""
        try:
            self.ssh.load_system_host_keys()
            self.ssh.connect(hostname=self.hostname,
                             port=self.port,
                             username=user_name,
                             password=password)
        except:
            print(f"Cannot establish conenction to {self.hostname}")
        return None

    def execute(self, command : str) -> tuple:
        """Function executes command over ssh connection."""
        if self.ssh.get_transport().is_active():
            (stdin, stdout, stderr) = self.ssh.exec_command(command)
            return (stdin, stdout, stderr)
        print(f"Conenction to {self.hostname} is dead.")
        return None

    def close_connection(self) -> None:
        """Function closes ssh connection."""
        self.ssh.close()
        return None

