import subprocess
import pyautogui as pag
import time


def uninstall():
    # UNISTALL PROGRAM FUNCTION
    cmd = 'msiexec /x {FE9E9CFB-D33D-4E75-B0ED-5D7725870E38}'
    p1 = subprocess.Popen(cmd, shell = True, stdout=subprocess.PIPE)
    time.sleep(2)
    pag.press('enter')
    p = p1.wait()

def install(cmd):
    # INSTALL PROGRAM FUNCTION
    p1 = subprocess.Popen(cmd, shell = True, stdout=subprocess.PIPE)
    time.sleep(2)
    pag.press('enter')
    time.sleep(2)
    pag.press('enter')
    time.sleep(2)
    pag.press('enter')
    time.sleep(5)
    pag.press('enter')
    p = p1.wait()





cmd, directory = 'git pull', 'C:\\maxpower-install'

p1 = subprocess.run(cmd, shell = True, stdout = subprocess.PIPE, text = True, cwd = directory)

res = p1.stdout


if(p1.returncode == 1):
    print('error')
elif (res == 'Already up to date.\n'):
    print('up')
else:
    res = pag.confirm(text='Nueva actualizacion,¿Desea actualizar?', title='Maxpower system', buttons=['OK', 'Cancel'])
    if(res == 'OK'):
        uninstall()
            # verify if user is 32 or 64 bits
        p1 = subprocess.run('set pro', shell = True, stdout = subprocess.PIPE, text = True)
        res = p1.stdout.split('\n')
        arch = res[0].split('=')[1]
        archite = res[1].split('=')[1]
        if(arch == 'AMD64' or archite == 'AMD64'):
            print('64 bits 1')
            cmd = 'C:\\maxpower-install\\x64\\Release\\setup.exe'
        else:
            print('32 bits')
            cmd = 'C:\\maxpower-install\\x32\\Release\\setup.exe'
            
        install(cmd)
            
            
            
            
# C:\Program Files\Maxpower\MaxPower System
            



# print(p1.stdout)

# msiexec /x {FE9E9CFB-D33D-4E75-B0ED-5D7725870E38}