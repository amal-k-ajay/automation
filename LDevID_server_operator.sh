#!/bin/sh

OPENSSL=openssl
OPENSSL_CONF=/usr/lib/ssl/openssl.cnf
export OPENSSL_CONF

certs_dir=certs

# End Entity certificate: create request first
$OPENSSL ecparam -name prime256v1  -genkey -out "$certs_dir/operator_server.key"

CN="10.10.10.10" ON="Device Operator" $OPENSSL req -new -sha256 -key "$certs_dir/operator_server.key" -config ca.cnf -out "$certs_dir/operator_server.csr"

# Sign request: end entity extensions
 $OPENSSL  x509 -req -days 365 -in "$certs_dir/operator_server.csr" -CA "$certs_dir/ca_LDevID.crt" -CAkey "$certs_dir/ca_LDevID_key.key" \
    -CAcreateserial -extfile ca.cnf -extensions usr_cert -out "$certs_dir/operator_server.crt"
 $OPENSSL ec -in "$certs_dir/operator_server.key" -pubout > "$certs_dir/operator_server.pub"

 




