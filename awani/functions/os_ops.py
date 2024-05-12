import socket
import os
import subprocess as sp

paths = {
    'notepad': "C:\\Windows\\system32\\notepad.exe",
    'calculator': "C:\\Windows\\System32\\calc.exe"
}


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip_add = s.getsockname()[0]
    return ip_add

def open_notepad():
    os.startfile(paths['notepad'])

def open_cmd():
    os.system('start cmd')

def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)

def open_calculator():
    sp.Popen(paths['calculator'])

# print(get_ip())
# open_notepad()
# open_cmd()
# open_camera()
# open_calculator()