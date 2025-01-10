import psutil
import os
import time
import ctypes
from ctypes import cast, POINTER
import subprocess
from comtypes import CLSCTX_ALL
from pycaw import IAudioEndpointVolume
import threading
import sys

def backdoor():
    running = True
    task_thread = None

    correct_password = "Multipass"  # Set your desired password here
    
    while True:
        password = input("Enter the password to start/stop the task (or 'exit' to quit): ")

        if password == correct_password:
            action = input("Type 'stop' to stop it: ").strip().lower()
            
            if action == "stop":
                if running:
                    stop_task()
                else:
                    print("Task stop.")
            else:
                print("Invalid action. Please type 'start' or 'stop'.")
        else:
            print("Incorrect password.")
            shutdown_computer()

def stop_task():
    global running
    running = False

def increase_volume(increment=1):
    # Obtener el dispositivo de audio predeterminado
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    # Obtener el volumen actual
    current_volume = volume.GetMasterVolumeLevelScalar()
    print(f"Volumen actual: {current_volume:.2f}")

    # Aumentar el volumen
    new_volume = min(current_volume + increment, 1.0)  # Asegurarse de que no supere 1.0
    volume.SetMasterVolumeLevelScalar(new_volume, None)
    print(f"Nuevo volumen: {new_volume:.2f}")
   
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
            time.sleep(10)
            backdoor()
        else:
            print("Clean")
            break
        time.sleep(15)  # Check every 15 seconds
