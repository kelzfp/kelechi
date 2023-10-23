import pexpect

# Define Variables
ip_address = '192.168.56.101'
username = 'cisco'
password = 'cisco123!'
hostname = 'Router2'  # Add the new hostname

# Function to save code locally
def save_code_locally():
    code = """
import pexpect

# Define Variables
ip_address = '192.168.56.101'
username = 'cisco'
password = 'cisco123!'
hostname = 'Router2'

# Create telnet session
session = pexpect.spawn('telnet ' + ip_address, encoding='utf-8', timeout=20)

result = session.expect(['Username:', pexpect.TIMEOUT])

# Check for error, if exists then display error and exit
if result != 0:
    print('--- FAILURE! creating session for: ', ip_address)
    exit()

# Session is expecting username, enter details
session.sendline(username)
result = session.expect(['Password:', pexpect.TIMEOUT])

# Check for error, if exists then display error and exit
if result != 0:
    print('--- FAILURE! entering username:', username)
    exit()

# Session is expecting password, enter details
session.sendline(password)
result = session.expect([hostname + '#', pexpect.TIMEOUT])

# Check for error, if exists then display error and exit
if result != 0:
    print('--- FAILURE! entering password:', password)
    exit()

# Display a success message if it works
print('-------------------------------------------------')
print('')
print('--- Success! connecting to:', ip_address)
print('---               Hostname:', hostname)
print('---               Username:', username)
print('---               Password:', password)
print('')
print('---------------------------------')

# Terminate telnet to the device and close the session
session.sendline('quit')
session.close()
"""

    with open('my_telnet_script.py', 'w') as file:
        file.write(code)

# Create telnet session
session = pexpect.spawn('telnet ' + ip_address, encoding='utf-8', timeout=20)

result = session.expect(['Username:', pexpect.TIMEOUT])

# Check for error, if it exists, then display an error and exit
if result != 0:
    print('--- FAILURE! creating session for: ', ip_address)
    exit()

# Session is expecting a username; enter the details
session.sendline(username)
result = session.expect(['Password:', pexpect.TIMEOUT])

# Check for error, if it exists, then display an error and exit
if result != 0:
    print('--- FAILURE! entering username:', username)
    exit()

# Session is expecting a password; enter the details
session.sendline(password)
result = session.expect([hostname + '#', pexpect.TIMEOUT])

# Check for error, if it exists, then display an error and exit
if result != 0:
    print('--- FAILURE! entering password:', password)
    exit()

# Display a success message if it works
print('-------------------------------------------------')
print('')
print('--- Success! connecting to:', ip_address)
print('---               Hostname:', hostname)
print('---               Username:', username)
print('---               Password:', password)
print('')
print('---------------------------------')

# Terminate telnet to the device and close the session
session.sendline('quit')
session.close()

# Save the code locally
save_code_locally()
