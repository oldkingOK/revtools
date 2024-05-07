import subprocess
import os

class process:
    def __init__(self, exe):
        self.exe = exe
        self.process = subprocess.Popen([exe], shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    def sendline(self, data):
        self.process.stdin.write(data.encode() + b"\n")
        self.process.stdin.flush()
    
    def recvline(self):
        return self.process.stdout.readline()
    
    def interactive(self):
        pass

    def get_pid(self):
        return self.process.pid

def pause():
    os.system("pause")