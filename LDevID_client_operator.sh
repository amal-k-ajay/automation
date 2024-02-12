#!/bin/sh

OPENSSL=openssl
OPENSSL_CONF=/usr/lib/ssl/openssl.cnf
export OPENSSL_CONF

certs_dir=certs

# End Entity certificate: create request first
$OPENSSL ecparam -name prime256v1  -genkey -out "$certs_dir/operator_client.key"

CN="IA Station" ON="Device Operator" $OPENSSL req -new -sha256 -key "$certs_dir/operator_client.key" -config ca_roles_keystoreadmin.cnf -out "$certs_dir/operator_client.csr"

 #Sign request: end entity extensions
 $OPENSSL  x509 -req -days 365 -in "$certs_dir/operator_client.csr" -CA "$certs_dir/ca_LDevID.crt" -CAkey "$certs_dir/ca_LDevID_key.key" \
    -CAcreateserial -extfile ca_roles_keystoreadmin.cnf -extensions usr_cert -out "$certs_dir/operator_client.crt"
$OPENSSL ec -in "$certs_dir/operator_client.key" -pubout > "$certs_dir/operator_client.pub"

openssl x509 -in "$certs_dir/operator_client.crt" -out "$certs_dir/operator_client.pem" -outform PEM
openssl x509 -in "$certs_dir/operator_client.pem" -noout -fingerprint > "$certs_dir/client_fingerprint.txt"




