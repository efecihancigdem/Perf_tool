"""Module providing the SSH functionality."""
import paramiko

HOST_NAME = '127.0.0.1'
USER_NAME = 'efe'
PASSWORD = '741049160'
PORT = 3022
COMMAND = 'hostname'

client = paramiko.SSHClient()

client.load_system_host_keys()
client.connect(hostname=HOST_NAME, port=PORT, username=USER_NAME, password=PASSWORD)

(stdin, stdout, stderr) = client.exec_command(COMMAND)

output = stdout.read()
print(str(output, 'utf8'))

client.close()
