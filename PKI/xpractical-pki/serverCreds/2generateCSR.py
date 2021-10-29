from pki_helpers import generate_csr, generate_private_key
server_private_key = generate_private_key(
  "server-private-key.pem", "serverpassword"
)
server_private_key

generate_csr(
  server_private_key,
  filename="server-csr.pem",
  country="US",
  state="Maryland",
  locality="Baltimore",
  org="My Company",
  alt_names=["localhost"],
  hostname="my-site.com",
)
