import paramiko

HOST_NAME = 'example.com'
PORT = 22

USER_NAME = 'user7'
PASSWORD = 'passwd'

cmd = 'uname'

client = paramiko.SSHClient()

client.load_system_host_keys()
client.connect(hostname=HOST_NAME, port=PORT, username=USER_NAME, password=PASSWORD)

(stdin, stdout, stderr) = client.exec_command(cmd)

output = stdout.read()
print(output)
print(str(output, 'utf8'))

client.close()