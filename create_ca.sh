#!/bin/sh

OPENSSL=openssl
OPENSSL_CONF=/usr/lib/ssl/openssl.cnf
export OPENSSL_CONF

# Create the "certs" directory if it doesn't exist
certs_dir=certs
if [ ! -d "$certs_dir" ]; then
    mkdir "$certs_dir"
fi

  # Root Heresteller IDEVID A: create certificate request then sign it
$OPENSSL ecparam -name prime256v1  -genkey -out "$certs_dir/ca_IDevID_key.key"

 CN="IDev Root CA" ON="Device Manufacturer 1" $OPENSSL req -days 365 -new -config ca.cnf  \
	-key "$certs_dir/ca_IDevID_key.key"  -sha256 -out "$certs_dir/ca_IDev_csr.csr"

$OPENSSL x509 -extfile ca.cnf -extensions v3_ca  -req -days 365 -sha256 -in "$certs_dir/ca_IDev_csr.csr" -signkey "$certs_dir/ca_IDevID_key.key" -out "$certs_dir/ca_IDevID.crt"

openssl x509 -in "$certs_dir/ca_IDevID.crt" -out "$certs_dir/ca_IDevID.pem" -outform pem


