import subprocess
import os

def fetch_certificate_info(crt_file):
    with open(crt_file) as f:
        cert_data = f.read()

    cert_info_start = cert_data.find("-----BEGIN CERTIFICATE-----")
    cert_info_end = cert_data.find("-----END CERTIFICATE-----")

    return cert_data[cert_info_start + len("-----BEGIN CERTIFICATE-----")+1:cert_info_end-1]

def fetch_pubkey_info(pub_key_file):
    with open(pub_key_file) as f:
        pub_key_data = f.read()

    pub_key_info_start = pub_key_data.find("-----BEGIN PUBLIC KEY-----")
    pub_key_info_end = pub_key_data.find("------END PUBLIC KEY-----")

    return pub_key_data[pub_key_info_start + len("------BEGIN PUBLIC KEY-----"):pub_key_info_end - len("------END PUBLIC KEY-----")]

def fetch_privkey_info(priv_key_file):
    with open(priv_key_file) as f:
        priv_key_data = f.read()

    priv_key_info_start = priv_key_data.find("-----BEGIN EC PRIVATE KEY-----")
    priv_key_info_end = priv_key_data.find("------END EC PRIVATE KEY-----")

    return priv_key_data[priv_key_info_start + len("-----BEGIN EC PRIVATE KEY-----")+1:priv_key_info_end - len("------END EC PRIVATE KEY-----")]

def process_xml_file(xml_file):
    with open(xml_file) as f:
        xml_data = f.read()

    cert_info = fetch_certificate_info(crt_file)
    xml_data = xml_data.replace('add_data_here</cert>', cert_info + '</cert>')

    pub_key_info = fetch_pubkey_info(pub_key_file)
    xml_data = xml_data.replace('add_data_here</public-key>', pub_key_info + '</public-key>')

    priv_key_info = fetch_privkey_info(priv_key_file)
    xml_data = xml_data.replace('add_data_here</private-key>', priv_key_info + '</private-key>')

    new_file_name = "xml_files2/keystore.xml"
    with open(new_file_name, "w") as f:
        f.write(xml_data)

if __name__ == "__main__":
    xml_file = os.getcwd() + "/xml_files2/keystore_template.xml"
    crt_file = os.getcwd() + "/certs/operator_server.crt"
    pub_key_file = os.getcwd() + "/certs/operator_server.pub"
    priv_key_file = os.getcwd() + "/certs/operator_server.key"

    process_xml_file(xml_file)

    print("Processed XML file saved as: keystore.xml")

