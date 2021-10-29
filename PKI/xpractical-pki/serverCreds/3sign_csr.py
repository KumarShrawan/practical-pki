from cryptography import x509
from cryptography.hazmat.backends import default_backend
csr_file = open("server-csr.pem", "rb")
csr = x509.load_pem_x509_csr(csr_file.read(), default_backend())
csr

ca_public_key_file = open("../CA/ca-public-key.pem", "rb")
ca_public_key = x509.load_pem_x509_certificate(
  ca_public_key_file.read(), default_backend()
)
ca_public_key

from getpass import getpass
from cryptography.hazmat.primitives import serialization
ca_private_key_file = open("../CA/ca-private-key.pem", "rb")
ca_private_key = serialization.load_pem_private_key(
  ca_private_key_file.read(),
  getpass().encode("utf-8"),
  default_backend(),
)
#Password:
#private_key


from pki_helpers import sign_csr
sign_csr(csr, ca_public_key, ca_private_key, "server-public-key.pem")
