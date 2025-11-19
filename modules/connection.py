from netmiko import ConnectHandler

def get_connection(host, username, password):
    device = {
        "device_type": "linux",
        "host": host,
        "username": username,
        "password": password,
    }

    print(f"Connecting to {host}...")
    conn = ConnectHandler(**device)
    return conn
