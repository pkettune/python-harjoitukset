import subprocess
import platform

def clear_screen():
    system = platform.system().lower()
    if system == 'windows':
        subprocess.run('cls', shell=True)
    else:
        subprocess.run('clear', shell=True)