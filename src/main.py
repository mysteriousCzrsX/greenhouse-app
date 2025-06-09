"""
@file main.py
@brief Entry point of the greenhouse control application.
@date 2025
"""

from multiprocessing import Process
import subprocess
import time

def run_flask():
    subprocess.run(["python", "web_server.py"])

def run_gui():
    subprocess.run(["python", "gui_interface.py"])

def run_control():
    subprocess.run(["python", "control_system.py"])

if __name__ == "__main__":
    flask_process = Process(target=run_flask)
    flask_process.start()

    time.sleep(1)  # Give Flask time to start
    control_process = Process(target=run_control)
    control_process.start()
    #gui_process = Process(target=run_gui)
    #gui_process.start()

    #gui_process.join()
    control_process.join()
    flask_process.terminate()
