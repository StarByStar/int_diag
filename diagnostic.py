import platform
import subprocess
import pathlib
import os


# Определение операционной системы
def os_name():
    return platform.system() + ' ' + platform.release()


# Пинг до узла
def ping(name):
    ping = subprocess.check_output(['ping', name, '-n', '10', '-l', '1200'])
    return str(ping, 'utf-8')


# Пинг основного шлюза
def ping_gw():
    out = list(str(subprocess.check_output(['route', 'print', '0.0.0.0', '-4']), 'utf-8').split())
    route = out[len(out) - 3]
    ping = subprocess.check_output(['ping', str(route), '-n', '5', '-l', '1200'])
    return str(ping, 'utf-8')


# Трассировка
def tracert(name):
    tracert = subprocess.check_output(['tracert', '-d', '-w', '200', name])
    return str(tracert, 'utf-8')


# Список запущенных процессов
def tasklist():
    task = subprocess.check_output(['tasklist'])
    return str(task, 'utf-8')


# ipconfig -all
def ipconfig():
    ipconf = subprocess.check_output(['ipconfig', '-all'])
    return str(ipconf, 'utf-8')


# netstat -e
def nestate():
    nestate = subprocess.check_output(['netstat', '-e'])
    return str(nestate, 'utf-8')


# netstat -s
def nestats():
    nestate = subprocess.check_output(['netstat', '-s'])
    return str(nestate, 'utf-8')


# netsh wlan show interface
def wlanif():
    iface = subprocess.run(['netsh', 'wlan', 'show', 'interface'], capture_output=True, shell=True)
    return str(iface.stdout, 'utf-8')


# Вывод файла host
def check_host():
    file_path = os.path.expandvars("%SystemRoot%") + '/System32/drivers/etc/hosts'
    host = pathlib.Path(file_path).read_text()
    return host


# Получение статистики из wirelessnetconsole
def wireless_console():
    cmd = "./diag/WirelessNetConsole.exe"
    process = subprocess.check_output([cmd])
    return str(process)


# Замер скорости по iperf
def iperf(server, timeout='15'):
    cmd = './diag/iperf.exe'
    process = subprocess.check_output([cmd, '-t', timeout, '-w', '2M', '-c', server])
    return str(process)