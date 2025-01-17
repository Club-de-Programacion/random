import psutil
import os
import time
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL

running = True

def backdoor():
    task_thread = None

    correct_password = "Multipass"  # Set your desired password here
    
    while True:
        password = input("Enter the password to start/stop the task (or 'exit' to quit): ")

        if password == correct_password:
            stop_task()
            print("Task stop.")
            break
        else:
            print("Incorrect password.")
            shutdown_computer()
            break

def stop_task():
    global running
    running = False

def is_opera_running():
    # Check if Opera GX is running
    for process in psutil.process_iter(['name']):
        if process.info['name'].lower() == 'opera.exe':  # Adjust for Opera GX
            return True
    return False

def shutdown_computer():
    while running:
        os.system("shutdown /s /t 10")

if __name__ == "__main__":
    while True:
        if is_opera_running():
            print("A non legal aplication is runing, the computer will sleep")
            time.sleep(1)
            backdoor()
            break
        else:
            print("Clean")
            break
