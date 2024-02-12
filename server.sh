#!/bin/sh

OPENSSL=openssl
OPENSSL_CONF=/usr/lib/ssl/openssl.cnf
export OPENSSL_CONF

certs_dir=certs

# End Entity certificate: create request first
$OPENSSL ecparam -name prime256v1  -genkey -out "$certs_dir/IDevID_ee_ser_key.key"

 $OPENSSL req -subj '/serialNumber=123456-ad' \
 -new -sha256  -key "$certs_dir/IDevID_ee_ser_key.key" -out "$certs_dir/IDevID_ee_ser_req.csr"

 #Sign request: end entity extensions
 $OPENSSL  x509 -req -days 365 -in "$certs_dir/IDevID_ee_ser_req.csr" -CA "$certs_dir/ca_IDevID.crt" -CAkey "$certs_dir/ca_IDevID_key.key" \
    -CAcreateserial -extfile ca.cnf -extensions usr_cert   -out "$certs_dir/IDevID_ee_ser.crt"
$OPENSSL ec -in "$certs_dir/IDevID_ee_ser_key.key" -pubout >"$certs_dir/IDevID_ee_ser_pub_key.pub"





