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
        os.getcwd() + '/LDevID_server_operator.sh',
        os.getcwd() + '/LDevID_client_operator.sh'
    ]
        
    run_openssl_scripts(script_paths)
    python_scripts = [os.getcwd() + '/xml_files2/gen_keystore_file.py', os.getcwd() + '/xml_files2/gen_truststore_file.py', os.getcwd() + '/xml_files2/gen_tls_listen_file.py', os.getcwd() + '/second_connect.py']
    run_python_scripts(python_scripts)
