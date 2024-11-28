import psutil
import os
import time
import ctypes
import subprocess

def run_command(command):
    try:
        # Run the command and capture the output
        result = subprocess.run(command, capture_output=True, text=True, shell=True)

        # Check if the command was successful
        if result.returncode == 0:
            print("Command executed successfully:")
            print(result.stdout)  # Print standard output
        else:
            print("Command failed with return code:", result.returncode)
            print(result.stderr)  # Print standard error
    except Exception as e:
        print("An error occurred:", str(e))

def is_opera_running():
    # Check if Opera GX is running
    for process in psutil.process_iter(['name']):
        if process.info['name'].lower() == 'opera.exe':  # Adjust for Opera GX
            return True
    return False

def shutdown_computer():
    # Warning message before shutdown
    time.sleep(100)  # Wait for 10 seconds before shutdown to allow user to save work
    os.system("shutdown /s /t 10")

if __name__ == "__main__":
    while True:
        if is_opera_running():
            print("A non legal aplication is runing, the computer will sleep")
            time.sleep(10)
            if run_command():
                command_to_run = "Multipass"
                print("Code correct")
                break
            else:  
                shutdown_computer()
                break
        if not is_opera_running ():
            print("Clean")
            break
        time.sleep(15)  # Check every 15 seconds
