import subprocess
import os

def extract_fingerprint(fingerprint_file):

    # Read the input data from the file
    with open(fingerprint_file, 'r') as f:
        fingerprint_data = f.read()

    # Extract the data after '='
    fingerprint = fingerprint_data.split('=')[-1]

    # Remove any trailing whitespace
    fingerprint = fingerprint.strip()

    return fingerprint

def process_xml_file(xml_file, fingerprint_file):
    with open(xml_file) as f:
        xml_data = f.read()

    fingerprint = extract_fingerprint(fingerprint_file)
    xml_data = xml_data.replace('add_data_here</fingerprint>', '02:' + fingerprint + '</fingerprint>')

    new_file_name = "xml_files2/tls_listen.xml"
    with open(new_file_name, "w") as f:
        f.write(xml_data)

if __name__ == "__main__":
    xml_file = os.getcwd() + "/xml_files2/tls_listen_template.xml"
    fingerprint_file = os.getcwd() + "/certs/client_fingerprint.txt"
    
    process_xml_file(xml_file, fingerprint_file)

    print("Processed XML file saved as: tls_listen.xml")
