import jwt

payload = {
    'some': 'palaki ashok kumar',
    'aud': ['urn:foo', 'urn:bar'],
    'iat': 1371720939
}

token = jwt.encode(payload, 'secret')
decoded = jwt.decode(token, 'secret', audience='urn:foo', algorithms=['HS256'])
print(token)
print(decoded)

#
# from cryptography.x509 import load_pem_x509_certificate
# from cryptography.hazmat.backends import default_backend
#
# cert_str = "-----BEGIN CERTIFICATE-----MIIDETCCAfm...".encode()
# cert_obj = load_pem_x509_certificate(cert_str, default_backend())
# public_key = cert_obj.public_key()
# private_key = cert_obj.private_key()
# print(public_key)
# print(private_key)