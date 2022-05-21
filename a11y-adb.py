import os
from ppadb.client import Client as AdbClient

clientDevice = "XXXXXXXXXX"
clientIP = "127.0.0.1"
clientPort = 5037

def execADB():
    # Default is "127.0.0.1" and 5037
    client = AdbClient(clientIP, clientPort)
    # Pass arg device name (use 'adb devices' to get device name)
    device = client.device(clientDevice)
    exit = False
    while exit == False:
        print("Enter '1' to start / '2' / 'q' to quit")
        i = input()
        if i == '1':
            # To start the accessibility service you can use:
            device.shell(
                "settings put secure enabled_accessibility_services com.google.android.marvin.talkback/com.google.android.marvin.talkback.TalkBackService")
        if i == '2':
            # And to stop:
            device.shell("am force-stop com.google.android.marvin.talkback")
        if i == 'q':
            # Quit
            quit()

if __name__ == '__main__':
    execADB()
