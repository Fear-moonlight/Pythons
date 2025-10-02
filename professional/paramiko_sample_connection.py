import paramiko
import logging
logging.basicConfig(level=logging.DEBUG)

# # SSH proxy (jump) server details
# proxy_host = 'CMLBJ'
# proxy_port = 22
# proxy_user = 'root'
# proxy_key_filename = '/Users/aliesmaeilicharkhab/.ssh/id_rsa'  # Update this

# # Destination Cisco device details
# dest_host = '10.12.27.101'
# dest_port = 22
# dest_user = 'cisco'
# dest_password = 'cisco'

# try:
#     # Create an SSH client and specify the ProxyCommand
#     ssh_command = f'ssh -i {proxy_key_filename} -W %h:%p {proxy_user}@{proxy_host}'
#     client = paramiko.SSHClient()
#     client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#     client.connect(dest_host, port=dest_port, username=dest_user, password=dest_password, sock=paramiko.ProxyCommand(ssh_command))

#     # Send commands or perform operations on the Cisco device
#     stdin, stdout, stderr = client.exec_command('show version')
#     print(stdout.read().decode())

#     # Close the connection
#     client.close()

# except paramiko.AuthenticationException as auth_error:
#     print("Authentication failed:", auth_error)

# except paramiko.SSHException as ssh_error:
#     print("SSH error:", ssh_error)

# except Exception as e:
#     print("Error:", e)

# hostname = 'CMLBJ'
# port = 22
# username = 'root'
# private_key_path = '/Users/aliesmaeilicharkhab/.ssh/id_rsa'  # Update this

# try:
#     # Load the private key for authentication
#     private_key = paramiko.RSAKey(filename=private_key_path)

#     # Create an SSH client
#     client = paramiko.SSHClient()
#     client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#     # Connect to the server using the private key for authentication
#     client.connect(hostname, port=port, username=username, pkey=private_key)

#     # Send commands or perform operations on the server
#     stdin, stdout, stderr = client.exec_command('ls -l')
#     print(stdout.read().decode())

#     # Close the connection
#     client.close()

# except paramiko.AuthenticationException as auth_error:
#     print("Authentication failed:", auth_error)

# except paramiko.SSHException as ssh_error:
#     print("SSH error:", ssh_error)

# except Exception as e:
#     print("Error:", e)
# SSH connection parameters
hostname = '10.12.27.101'
port = 22
username = 'cisco'
password = 'cisco'
proxy_command = 'ssh -i  ~/.ssh/id_rsa -W %h:%p root@CMLBJ'

# Create an SSH client
client = paramiko.SSHClient()

# Automatically add the server's host key (this is insecure in a production environment)
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Use the proxy command to connect to the remote server
try:
    client.connect(hostname, port, username, sock=paramiko.ProxyCommand(proxy_command))
    print("Connected to", hostname)

    # Execute a command
    stdin, stdout, stderr = client.exec_command('ls -l')

    # Print the command output
    print(stdout.read().decode())
except paramiko.AuthenticationException:
    print("Authentication failed")
except paramiko.SSHException as e:
    print("SSH connection failed:", str(e))
finally:
    # Close the SSH connection
    client.close()