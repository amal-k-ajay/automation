#!/bin/sh

OPENSSL=openssl
OPENSSL_CONF=/usr/lib/ssl/openssl.cnf
export OPENSSL_CONF

certs_dir=certs

# End Entity certificate: create request first
$OPENSSL ecparam -name prime256v1  -genkey -out "$certs_dir/cli_key.key"

CN="CNC" ON="Device Operator" $OPENSSL req -new -sha256 -key "$certs_dir/cli_key.key" -config ca_roles.cnf -out "$certs_dir/cli_req.csr" 

 #Sign request: end entity extensions
 $OPENSSL  x509 -req -days 365 -in "$certs_dir/cli_req.csr" -CA "$certs_dir/ca_LDevID.crt" -CAkey "$certs_dir/ca_LDevID_key.key" \
    -CAcreateserial -extfile ca_roles.cnf -extensions usr_cert -out "$certs_dir/cli.crt"


