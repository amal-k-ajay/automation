import subprocess
import os

def fetch_certificate_info(crt_file):
    with open(crt_file) as f:
        cert_data = f.read()

    cert_info_start = cert_data.find("-----BEGIN CERTIFICATE-----")
    cert_info_end = cert_data.find("-----END CERTIFICATE-----")

    return cert_data[cert_info_start + len("-----BEGIN CERTIFICATE-----")+1:cert_info_end-1]


def process_xml_file(xml_file):
    with open(xml_file) as f:
        xml_data = f.read()

    cert_info = fetch_certificate_info(crt_file)
    xml_data = xml_data.replace('add_data_here</cert>', cert_info + '</cert>')

    new_file_name = "xml_files1/truststore.xml"
    with open(new_file_name, "w") as f:
        f.write(xml_data)

if __name__ == "__main__":
    xml_file = os.getcwd() + "/xml_files1/truststore_template.xml"
    crt_file = os.getcwd() + "/certs/IDevID_ee_ser.crt"
    
    process_xml_file(xml_file)

    print("Processed XML file saved as: truststore.xml")

