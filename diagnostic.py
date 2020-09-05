import platform
import subprocess
import pathlib
import os


# Определение операционной системы
def os_name():
    return platform.system() + ' ' + platform.release()


# Пинг ya.ru
# https://pyneng.readthedocs.io/ru/latest/book/12_useful_modules/subprocess.html
def ping_ya():
    ping = subprocess.check_output(['ping', 'ya.ru', '-n', '10', '-l', '1200'])
    return str(ping, 'utf-8')


# Пинг DNS (заменить на st эртх)
def ping_dns(dns):
    ping = subprocess.check_output(['ping', dns, '-n', '10', '-l', '1200'])
    return str(ping, 'utf-8')


# Трассировка mail.ru
def tracert_mail():
    tracert = subprocess.check_output(['tracert', '-d', '-w', '200', 'mail.ru'])
    return str(tracert, 'utf-8')


# Трассировка vk.com
def tracert_vk():
    tracert = subprocess.check_output(['tracert', '-d', '-w', '200', 'vk.com'])
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


# Пинг основного шлюза
def ping_gw():
    out = list(str(subprocess.check_output(['route', 'print', '0.0.0.0', '-4']), 'utf-8').split())
    route = out[len(out) - 3]
    ping = subprocess.check_output(['ping', str(route), '-n', '5', '-l', '1200'])
    return str(ping, 'utf-8')


# Получение статистики из wirelessnetconsole
def wireless_console():
    pass


# Замер скорости по iperf
def iperf():
    pass