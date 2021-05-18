import subprocess
import io

sp = subprocess.Popen(['ls'], stdout=subprocess.PIPE, shell=True)
print(sp)
out = io.TextIOWrapper(sp.stdout, encoding='UTF-8')
s = ' '
while s:
    s = out.readline()
    print(s)
