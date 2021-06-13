import time
import serial
import sys,tty,termios
class _Getch:
    def __call__(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

def get():
    inkey = _Getch()
    d1 = input()
    d2 = input()
    dir = input()
    if dir=='east':
        s.write("/goStraight/run -50 \n".encode())
        time.sleep(int(d2)/4.5)
        s.write("/stop/run \n".encode())
        time.sleep(1)
        s.write("/turn/run 20 0.01 \n".encode())
        time.sleep(2.5)
        s.write("/stop/run \n".encode())
        time.sleep(1)
        s.write("/goStraight/run -50 \n".encode())
        time.sleep(int(d1)/3)
        s.write("/stop/run \n".encode())
    elif dir=='west':
        s.write("/goStraight/run -50\n".encode())
        time.sleep(int(d2)/4.5)
        s.write("/stop/run \n".encode())
        time.sleep(1)
        s.write("/turn/run -20 -0.01 \n".encode())
        time.sleep(3.5)
        s.write("/stop/run \n".encode())
        time.sleep(1)
        s.write("/goStraight/run -50 \n".encode())
        time.sleep(int(d1)/3)
        s.write("/stop/run \n".encode())
    else:
        print ("not an arrow key!")
    return 1

if len(sys.argv) < 1:
    print ("No port input")
s = serial.Serial(sys.argv[1])
while get():
    i = 0


