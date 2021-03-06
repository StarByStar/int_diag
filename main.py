import subprocess
import eel
import json
import requests
import os
import sys
import platform
import pathlib
from diagnostic import *


# Справочник для хранения ключа (по № договора),
# города, имени st сервера, iperf сервера
cities = \
    {10: ['ufa', 'st2.ufa.ertelecom.ru', 'iperf.ufa.ertelecom.ru'],
     12: ['yola', 'st2.yola.ertelecom.ru', 'iperf.yola.ertelecom.ru'],
     16: ['kazan', 'st2.kazan.ertelecom.ru', 'iperf.kazan.ertelecom.ru'],
     17: ['chel', 'st2.chel.ertelecom.ru', 'iperf.chel.ertelecom.ru'],
     18: ['izhevsk', 'st2.izhevsk.ertelecom.ru', 'iperf.izhevsk.ertelecom.ru'],
     21: ['cheb', 'st2.cheb.ertelecom.ru', 'iperf.cheb.ertelecom.ru'],
     22: ['barnaul', 'st2.barnaul.ertelecom.ru', 'iperf.barnaul.ertelecom.ru'],
     23: ['krd', 'st2.krd.ertelecom.ru', 'iperf.rostov.ertelecom.ru'],
     24: ['krsk', 'st2.krsk.ertelecom.ru', 'iperf.krsk.ertelecom.ru'],
     27: ['mgn', 'st2.mgn.ertelecom.ru', 'iperf.mgn.ertelecom.ru'],
     30: ['ulu', 'st2.ulu.ertelecom.ru', 'iperf.irkutsk.ertelecom.ru'],
     32: ['bryansk', 'st2.bryansk.ertelecom.ru', 'iperf.bryansk.ertelecom.ru'],
     34: ['volgograd', 'st2.volgograd.ertelecom.ru', 'iperf.volgograd.ertelecom.ru'],
     36: ['voronezh', 'st2.voronezh.ertelecom.ru', 'iperf.voronezh.ertelecom.ru'],
     38: ['irkutsk', 'st2.irkutsk.ertelecom.ru', 'iperf.irkutsk.ertelecom.ru'],
     43: ['kirov', 'st2.kirov.ertelecom.ru', 'iperf.kirov.ertelecom.ru'],
     45: ['kurgan', 'st2.kurgan.ertelecom.ru', 'iperf.kurgan.ertelecom.ru'],
     46: ['kursk', 'st2.kursk.ertelecom.ru', 'iperf.kursk.ertelecom.ru'],
     48: ['lipetsk', 'st2.lipetsk.ertelecom.ru', 'iperf.lipetsk.ertelecom.ru'],
     52: ['nn', 'st2.nn.ertelecom.ru', 'iperf.nn.ertelecom.ru'],
     54: ['nsk', 'st2.nsk.ertelecom.ru', 'iperf.nsk.ertelecom.ru'],
     55: ['omsk', 'st2.omsk.ertelecom.ru', 'iperf.omsk.ertelecom.ru'],
     56: ['oren', 'st2.oren.ertelecom.ru', 'iperf.oren.ertelecom.ru'],
     58: ['penza', 'st2.penza.ertelecom.ru', 'iperf.penza.ertelecom.ru'],
     59: ['perm', 'st2.perm.ertelecom.ru', 'iperf.perm.ertelecom.ru'],
     61: ['rostov', 'st2.rostov.ertelecom.ru', 'iperf.rostov.ertelecom.ru'],
     62: ['ryazan', 'st2.ryazan.ertelecom.ru', 'iperf.ryazan.ertelecom.ru'],
     63: ['samara', 'st2.samara.ertelecom.ru', 'iperf.samara.ertelecom.ru'],
     64: ['saratov', 'st2.saratov.ertelecom.ru', 'iperf.saratov.ertelecom.ru'],
     66: ['ekat', 'st2.ekat.ertelecom.ru', 'iperf.ekat.ertelecom.ru'],
     69: ['tver', 'st2.ekat.ertelecom.ru', 'iperf.ekat.ertelecom.ru'],
     70: ['tomsk', 'st2.tomsk.ertelecom.ru', 'iperf.tomsk.ertelecom.ru'],
     71: ['tula', 'st2.tula.ertelecom.ru', 'iperf.tula.ertelecom.ru'],
     72: ['tmn', 'st2.tmn.ertelecom.ru', 'iperf.tmn.ertelecom.ru'],
     73: ['ulsk', 'st2.ulsk.ertelecom.ru', 'iperf.ulsk.ertelecom.ru'],
     76: ['yar', 'st2.yar.ertelecom.ru', 'iperf.yar.ertelecom.ru'],
     77: ['msk', 'st2.msk.ertelecom.ru', 'iperf.msk.ertelecom.ru'],
     78: ['spb', 'st2.spb.ertelecom.ru', 'iperf.spb.ertelecom.ru']
     }


eel.init("web")
# проверка валидности номера договора
def agreement_check(agr):
    assert agr.isdigit(), "Номер договора должен быть положительным числом"
    assert len(str(agr)) == 12, "Номер договора должен состоять из 12 чисел"

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


# Получение статистики из wirelessnetconsole
def wireless_console():
    cmd = resource_path("WirelessNetConsole.exe")
    process = subprocess.check_output([cmd], shell=True)
    return str(process)


# Замер скорости по iperf
def iperf(server, timeout='5'):
    cmd = resource_path("iperf.exe")
    process = subprocess.check_output([cmd, '-t', timeout, '-w', '2M', '-c', server], shell=True)
    return str(process)


# Определение города, dns, iperf Клиента по № договора
def get_city(agr, cities):
    if int(agr[:2]) in cities:
        return cities[int(agr[:2])]
    else:
        return ['unknown', '8.8.8.8', 'iperf.perm.ertelecom.ru']


#Кодирование в JSON формат
def json_code(agr, city, os_name, ping_dns, ping_ya, ping_gw, tracert_mail,
              tracert_vk, task, ipconf, netstats, netstate, check_host, wlan, iperf, wireless_console):
    report_struct = {
        "agreement": agr,
        "city": city,
        "os version": os_name,
        "ping dns": ping_dns,
        "ping yandex.ru": ping_ya,
        "ping gw":ping_gw,
        "tracert mail.ru": tracert_mail,
        "tracert vk.com": tracert_vk,
        "tasklist": task,
        "ipconfig": ipconf,
        "netstat -s": netstats,
        "netstat -e": netstate,
        "host": check_host,
        "netsh wlan": wlan,
        "iperf": iperf,
        "wireless console": wireless_console
    }
    jsonData = json.dumps(report_struct)
    #report = "report.json"
    #file = open(report, mode='w', encoding='UTF-8')
    #json.dump(report_struct, file)
    #file.close()
    return jsonData


# Сохранение json в файл для отладки
def save_to_file(json_data):
    report = "report.json"
    file = open(report, mode='w', encoding='UTF-8')
    json.dump(json_data, file)
    file.close()


# Запуск диагностики при клике на кнопку
@eel.expose
def diag_start(agr):
    #agreement_check(agr)

    return json_code(agr,
              get_city(agr, cities)[0],
              os_name(),
              ping(get_city(agr, cities)[1]),
              ping('ya.ru'),
              ping_gw(),
              tracert('mail.ru'),
              tracert('vk.com'),
              tasklist(),
              ipconfig(),
              nestats(),
              nestate(),
              check_host(),
              wlanif(),
              iperf(get_city(agr, cities)[2]),
              wireless_console()
               )


eel.start("main.html", size=(500, 600))
