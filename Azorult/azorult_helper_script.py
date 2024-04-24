import winreg
import time
import sys


def read_key_value(registry_path, key_name):
   

    previous_value = None
    while True:
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, registry_path, 0, winreg.KEY_READ)
            value, type = winreg.QueryValueEx(key, key_name)
            winreg.CloseKey(key)
        except winreg.error as e:
            print(f"Error: {e}")
            return None
        if value != previous_value:
            print(f"Value: {value}")
            previous_value = value
        time.sleep(0.1)


if __name__ == "__main__":
    
    if len(sys.argv) != 3:
        print("usage: python script.py <registry_path> <key_name>")
        exit(1)

    registry_path = sys.argv[1]
    key_name = sys.argv[2]

   
    read_key_value(registry_path, key_name)
