import subprocess
import platform


def ping(ip: str, timeout: int = 1):
    if platform.system() == "Windows":
        command = f"ping -n 1 -w {timeout} {ip}"
    else:
        command = f"ping -c 1 -w {timeout} {ip}"
    try:
        result = subprocess.check_output(command, shell=True)
        return True
    except subprocess.CalledProcessError:
        return False
