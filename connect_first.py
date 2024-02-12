import subprocess
import os

# Set the home directory
home_directory = "/home/amal/Desktop/workspace/"

# Define the commands for sysrepo
sysrepo_commands = [
    "sudo sysrepocfg --edit=" + os.getcwd() + "/xml_files1/keystore.xml -m ietf-keystore",
    "sudo sysrepocfg --edit=" + os.getcwd() + "/xml_files1/truststore.xml -m ietf-truststore",
    "sudo sysrepocfg --edit=" + os.getcwd() + "/xml_files1/tls_listen.xml -m ietf-netconf-server"
]

# Define the command for netopeer2-cli
netopeer2_cli_command = "sudo netopeer2-cli"
netopeer2_server_command = "sudo netopeer2-server -d -v3"

# Execute sysrepo commands
sysrepo_folder = os.path.join(home_directory, "sysrepo")
os.chdir(sysrepo_folder)

for command in sysrepo_commands:
    subprocess.run(command, shell=True)

# Move out of sysrepo folder and enter netopeer2 folder
os.chdir(home_directory)
netopeer2_folder = os.path.join(home_directory, "netopeer2")

subprocess.run(['gnome-terminal', '--', 'bash', '-c', 'cd {}; {}; exec bash'.format(netopeer2_folder, netopeer2_server_command)])
# Open a new terminal and execute netopeer2-cli
subprocess.run(['gnome-terminal', '--', 'bash', '-c', 'cd {}; {}; exec bash'.format(netopeer2_folder, netopeer2_cli_command)])

# Add a delay to allow netopeer2-cli to start before sending commands
import time
time.sleep(1)

# Send additional command to netopeer2-cli (e.g., "help")
additional_command = "help"
subprocess.run(['xdotool', 'type', additional_command])
subprocess.run(['xdotool', 'key', 'Return'])

additional_command_1 = "connect-first --tls --cert " + os.getcwd() + "/automation/certs/cli.crt --key " + os.getcwd() + "/automation/certs/cli_key.key --trusted " + os.getcwd() + "/automation/certs/ca_IDevID.pem"
subprocess.run(['xdotool', 'type', additional_command_1])
subprocess.run(['xdotool', 'key', 'Return'])

time.sleep(1)

additional_command_2 = "status"
subprocess.run(['xdotool', 'type', additional_command_2])
subprocess.run(['xdotool', 'key', 'Return'])


