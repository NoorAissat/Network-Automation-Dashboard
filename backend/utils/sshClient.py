import os
from dotenv import load_dotenv
from modules.connection import get_connection


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV_PATH = os.path.join(BASE_DIR, ".env")
load_dotenv(ENV_PATH)

SSH_HOST = os.getenv("SSH_HOST")
SSH_USERNAME = os.getenv("SSH_USERNAME")
SSH_PASSWORD = os.getenv("SSH_PASSWORD")


def ssh_connect():
    if not all([SSH_HOST, SSH_USERNAME, SSH_PASSWORD]):
        raise ValueError("SSH credentials not set in backend/.env")
    return get_connection(SSH_HOST, SSH_USERNAME, SSH_PASSWORD)
