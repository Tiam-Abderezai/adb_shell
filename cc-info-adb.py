import os
from ppadb.client import Client as AdbClient

ccNumber = "fffffff"
clientDevice = "XXXXXXX"
clientIP = "127.0.0.1"
clientPort = 5037

def execADB():
    # Default is "127.0.0.1" and 5037
    client = AdbClient(clientIP, clientPort)
    # Pass arg device name (use 'adb devices' to get device name)
    device = client.device(clientDevice)
    # Enter 'hello world' text into EditText
    device.shell(f"input text {ccNumber}")

if __name__ == '__main__':
    execADB()
