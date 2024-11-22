import psutil
import os
import time
import ctypes
import subprocess

def is_opera_running():
    # Check if Opera GX is running
    for process in psutil.process_iter(['name']):
        if process.info['name'].lower() == 'operagx.exe':  # Adjust for Opera GX
            return True
    return False

def shutdown_computer():
    # Warning message before shutdown
    time.sleep(10)  # Wait for 10 seconds before shutdown to allow user to save work
    os.system("shutdown /s /t 10")


if __name__ == "__main__":
    while True:
        if is_opera_running():
            print("A non legal aplication is runing, the computer will sleep")
            time.sleep(10)
            if comand_ejecuted():
                comando_a_detectar = "Multipass"
                print("Code correct")
                break
            else:  
                shutdown_computer()
                break
        if not is_opera_running ():
            print("Clean")
            break
        time.sleep(5)  # Check every 5 seconds
