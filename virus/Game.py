#Program on develop do not touch or eject

import psutil
import os
import time
import ctypes
from ctypes import cast, POINTER
import subprocess
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import threading
import sys

def backdoor():
    running = True
    task_thread = None

    correct_password = "Multipass"  # Set your desired password here
    
    while True:
        password = input("Enter the password to start/stop the task (or 'exit' to quit): ")

        if password == correct_password:
            action = input("Type 'start' to start the task or 'stop' to stop it: ").strip().lower()
            if action == "start":
                if not running:
                    start_task()
                else:
                    print("Task is already running.")
            elif action == "stop":
                if running:
                    stop_task()
                else:
                    print("Task is not running.")
            else:
                print("Invalid action. Please type 'start' or 'stop'.")
        elif password.lower() == "exit":
            if running:
                stop_task()
            print("Exiting the program.")
            break
        else:
            print("Incorrect password. Please try again.")

def stop_task():
    global running
    running = False
    task_thread.join()  # Wait for the thread to finish
    print("Password correct.")

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
            if backdoor():
            else:
                increase_volume()
                print("Code incorrect, computer going to sleep")
                time.sleep(5)
                shutdown_computer()
        if not is_opera_running ():
            print("Clean")
            break
        time.sleep(15)  # Check every 15 seconds
