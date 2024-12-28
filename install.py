import os
import time

print("Installing Tool dependencies:")
time.sleep(1.2)

def install_dependencies():
    os.system("apt-get install espeak -y")
    os.system("apt-get install pulseaudio -y")
    os.system("apt-get install curl -y")

install_dependencies()
os.system("clear")
print("Installation Completed. Now run python Error.py to use tool")
os.system("pulseaudio --start")
text9 = "Installation Completed. Now run python Error.py to get data"
os.system(f"espeak '{text9}'")
