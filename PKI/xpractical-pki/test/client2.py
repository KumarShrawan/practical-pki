# client.py
def get_secret_message():
    response = requests.get("http://localhost:4443", verify="ca-public-key.pem")
    print(f"The secret message is {response.text}")
