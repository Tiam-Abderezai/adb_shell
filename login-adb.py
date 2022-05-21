import os
from ppadb.client import Client as AdbClient

username = "\\user@email.com"
password = "password"
clientDevice = "XXXXXXXXXX"
clientIP = "127.0.0.1"
clientPort = 5037

def execADB():
    # Default is "127.0.0.1" and 5037
    client = AdbClient(clientIP, clientPort)
    # Pass arg device name (use 'adb devices' to get device name)
    device = client.device(clientDevice)
    # Enter 'hello world' text into EditText
    device.shell(f"input text {username}")
    # keyevent KEYCODE_TAB twice to go to next EditText
    device.shell(f"input keyevent KEYCODE_TAB")
    device.shell(f"input keyevent KEYCODE_TAB")
    # enter password
    device.shell(f"input text {password}")
    device.shell(f"input keyevent KEYCODE_TAB")
    device.shell(f"input keyevent KEYCODE_TAB")

    # device.shell(f"input text ${password}")

if __name__ == '__main__':
    execADB()
