import platform
import subprocess
import pathlib
import os
import sys

# Определение операционной системы
def os_name():
    return platform.system() + ' ' + platform.release()


# Пинг до узла
def ping(name):
    ping = subprocess.check_output(['ping', name, '-n', '4', '-l', '1200'], shell=True)
    return str(ping)


# Пинг основного шлюза
def ping_gw():
    out = list(str(subprocess.check_output(['route', 'print', '0.0.0.0', '-4'], shell=True)).split())
    route = out[len(out) - 3]
    ping = subprocess.check_output(['ping', str(route), '-n', '5', '-l', '1200'], shell=True)
    return str(ping)


# Трассировка
def tracert(name):
    tracert = subprocess.check_output(['tracert', '-d', '-w', '200', name], shell=True)
    return str(tracert)


# Список запущенных процессов
def tasklist():
    task = subprocess.check_output(['tasklist'], shell=True,)
    return str(task)


# ipconfig -all
def ipconfig():
    ipconf = subprocess.check_output(['ipconfig', '-all'], shell=True)
    return str(ipconf)


# netstat -e
def nestate():
    nestate = subprocess.check_output(['netstat', '-e'], shell=True)
    return str(nestate)


# netstat -s
def nestats():
    nestate = subprocess.check_output(['netstat', '-s'], shell=True)
    return str(nestate)


# Вывод файла host
def check_host():
    file_path = os.path.expandvars("%SystemRoot%") + '/System32/drivers/etc/hosts'
    host = pathlib.Path(file_path).read_text()
    return host


# Определение операционной системы
# netsh wlan show interface
def wlanif():
    iface = subprocess.run(['netsh', 'wlan', 'show', 'interface'], capture_output=True, shell=True)
    return str(iface.stdout)