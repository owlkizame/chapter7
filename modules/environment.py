import os


def run(**args):
    print("[*] in environment modules.")
    return str(os.environ)