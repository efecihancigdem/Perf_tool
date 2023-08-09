"""Remote class"""
from src.remote import Remote

#Env Variables
HOST_NAME = '127.0.0.1'
USER_NAME = 'efe'
PASSWORD = '5432154321'
PORT = 3022
COMMAND = 'ip address'

#Remote execution
linux1 = Remote(HOST_NAME)
linux1.connect(USER_NAME,PASSWORD)
output = linux1.execute(COMMAND)[1].read()
print(str(output,'utf8'))
linux1.close_connection()
