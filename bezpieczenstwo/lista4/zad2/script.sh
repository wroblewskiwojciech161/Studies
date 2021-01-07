# Generate key A:
openssl genrsa -out privkeyA.pem 2048

# Generate A certificate:
openssl req -new -key privkeyA.pem -out certA.csr

# Generate key B:
openssl genrsa -out privkeyB.pem 2048

# Generate certificate:

openssl req -new -x509 -key privkeyB.pem -out CAcert.crt -days 15

openssl x509 -req -days 45 -in certA.csr -CA CAcert.crt -CAkey privkeyB.pem -set_serial 01 -out certA.crt
