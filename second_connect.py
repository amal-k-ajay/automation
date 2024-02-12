import subprocess
import os

def get_window_id(command):
    result = subprocess.check_output(['xdotool', 'search', '--onlyvisible', '--class', 'gnome-terminal'])
    return result.decode('utf-8').strip()

# Set the home directory
home_directory = os.path.dirname(os.getcwd())

# move to sysrepo folder
sysrepo_folder = os.path.join(home_directory, "sysrepo")
os.chdir(sysrepo_folder)


# Define the cert-to-name mapping commands
commands = [
    "sudo sysctl fs.protected_regular=0",
    "sudo sysrepoctl --update " + home_directory + "/automation/ietf-x509-cert-to-name@2022-11-17.yang"
]

# Execute the cert-to-name mapping commands
for command in commands:
    subprocess.run(command, shell=True)


# Define the command for netopeer2-cli
netopeer2_cli_command = "sudo netopeer2-cli"
netopeer2_server_command = "sudo netopeer2-server -d -v3"

# Move out of sysrepo folder and enter netopeer2 folder

#netopeer2_folder = os.path.join(home_directory, "netopeer2")
os.chdir(home_directory + "/automation/")

# start server and client
subprocess.run(['gnome-terminal', '--', 'bash', '-c','netopeer2-server -d -v3'])
subprocess.run(['gnome-terminal', '--', 'bash', '-c', 'netopeer2-cli'])


# Add a delay to allow netopeer2-cli to start before sending commands
import time
time.sleep(1)

# Send additional command to netopeer2-cli
additional_command = "help"
subprocess.run(['xdotool', 'type', additional_command])
subprocess.run(['xdotool', 'key', 'Return'])

additional_command_1 = "connect-first --tls --cert " + os.getcwd() + "/certs/cli.crt --key " + os.getcwd() + "/certs/cli_key.key --trusted " + os.getcwd() + "/certs/ca_IDevID.pem"
subprocess.run(['xdotool', 'type', additional_command_1])
subprocess.run(['xdotool', 'key', 'Return'])

time.sleep(1)

additional_command_2 = "status"
subprocess.run(['xdotool', 'type', additional_command_2])
subprocess.run(['xdotool', 'key', 'Return'])

time.sleep(1)

edit_config_commands = [
    "edit-config --target candidate --config=" + os.getcwd() + "/xml_files2/keystore.xml", "commit",
    "edit-config --target candidate --config=" + os.getcwd() + "/xml_files2/truststore.xml", "commit", 
    "edit-config --target candidate --config=" + os.getcwd() + "/xml_files2/tls_listen.xml", "commit",
]

# Loop through each command and send it using xdotool
for command in edit_config_commands:
    subprocess.run(['xdotool', 'type', command])
    subprocess.run(['xdotool', 'key', 'Return'])
    time.sleep(1) 

for _ in range(2):  # Close two terminals
    window_id = get_window_id("gnome-terminal")  # Get the window ID using xdotool
    subprocess.run(['xdotool', 'windowclose', window_id])  # Close the terminal using xdotool
    time.sleep(1)  # Brief delay to ensure full closure

commands2 = [

    "sudo ip link add dev vm1 type veth peer name vm2",
    "sudo ip addr add 10.10.10.10/24 dev vm1",
    "sudo ip addr add 10.10.10.11/24 dev vm2",
    "sudo ip link set dev vm1 up",
    "sudo ip link set dev vm2 up"
]

# Execute the cert-to-name mapping commands
for command in commands2:
    subprocess.run(command, shell=True)

# restart server and client
subprocess.run(['gnome-terminal', '--', 'bash', '-c','netopeer2-server -d -v3'])
subprocess.run(['gnome-terminal', '--', 'bash', '-c', 'netopeer2-cli'])

second_connect = "connect --tls --host 10.10.10.10 --cert " + os.getcwd() + "/certs/operator_client.crt --key " + os.getcwd() + "/certs/operator_client.key --trusted " + os.getcwd() + "/certs/ca_LDevID.pem"
subprocess.run(['xdotool', 'type', second_connect])
subprocess.run(['xdotool', 'key', 'Return'])

time.sleep(1) 

additional_command_3 = "status"
subprocess.run(['xdotool', 'type', additional_command_3])
subprocess.run(['xdotool', 'key', 'Return'])
