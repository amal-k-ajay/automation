import subprocess
import os

def run_openssl_scripts(script_paths):
    for script_path in script_paths:
        process = subprocess.Popen(f'bash {script_path}', shell=True)
        process.wait()

def run_python_scripts(python_scripts):
    for script_path in python_scripts:
        process = subprocess.Popen(f'python3 {script_path}', shell=True)
        process.wait()

if __name__ == '__main__':
    script_paths = [
        os.getcwd() + '/create_ca.sh',
        os.getcwd() + '/server.sh',
        os.getcwd() + '/create_ca_LDevID.sh',
        os.getcwd() + '/client_LDevID.sh',
    ]

    run_openssl_scripts(script_paths)
    python_scripts = ['xml_files1/gen_keystore_file.py', 'xml_files1/gen_truststore_file.py', os.getcwd() + '/connect_first.py']
    run_python_scripts(python_scripts)
