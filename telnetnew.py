#Import required modules/packages/library
import pexpect

#Define Variables
ip_address = '192.168.56.101'
username = 'cisco'
password = 'cisco123!'

#Create telnet session
session = pexpect.spawn('telnet ' + ip_address, encoding='utf-8', timeout=20)

result = session.expect(['Username:', pexpect.TIMEOUT])

#Check for error, if exists then display error and exit
if result != 0:
    print('--- FAILURE! creating session for: ', ip_address)
    exit()

#Session is expecting username, enter details
session.sendline(username)
result = session.expect(['Password:', pexpect.TIMEOUT])

#Check for error, if exists then display error and exit
if result != 0:
    print('--- FAILURE! entering username:', username)
    exit()

#Session is expecting password, enter details
session.sendline(password)
result = session.expect(['#', pexpect.TIMEOUT])

#Check for error, if exists then display error and exit
if result != 0:
    print('--- FAILURE! entering password:', password)
    exit()

# Add the hostname 'Router 2'
session.sendline('conf t')
session.sendline('hostname Router 2')
session.expect(['\(config\)#', pexpect.TIMEOUT])

# Display a success message if it works
print('-------------------------------------------------')
print('')
print('--- Success! connecting to:', ip_address)
print('---               Username:', username)
print('---               Password:', password)
print('')
print('---------------------------------')

# Terminate telnet to the device and close the session
session.sendline('quit')
session.close()
