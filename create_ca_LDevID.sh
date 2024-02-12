#!/bin/sh

OPENSSL=openssl
OPENSSL_CONF=/usr/lib/ssl/openssl.cnf
export OPENSSL_CONF

certs_dir=certs

  # Root Heresteller IDEVID A: create certificate request then sign it
$OPENSSL ecparam -name prime256v1  -genkey -out "$certs_dir/ca_LDevID_key.key"

 CN="LDev Root CA" ON="Device Operator 1" $OPENSSL req -days 365 -new -config ca.cnf  \
	-key "$certs_dir/ca_LDevID_key.key"  -sha256 -out "$certs_dir/ca_LDev_csr.csr"

$OPENSSL x509 -extfile ca_roles.cnf -extensions v3_ca -req -days 365 -sha256 -in "$certs_dir/ca_LDev_csr.csr" -signkey "$certs_dir/ca_LDevID_key.key" -out "$certs_dir/ca_LDevID.crt"

# Create PEM file from the CA certificate
$OPENSSL x509 -in "$certs_dir/ca_LDevID.crt" -out "$certs_dir/ca_LDevID.pem" -outform PEM
