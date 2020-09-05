import eel
import json
import requests
from diagnostic import *

eel.init("web")


# проверка валидности номера договора
def agreement_check(agr):
    assert agr.isdigit(), "Номер договора должен быть положительным числом"
    assert len(str(agr)) == 12, "Номер договора должен состоять из 12 чисел"


# определение города Клиента по № договора
def get_city(agr):
    cities = \
    {10: ['ufa', 'st2.ufa.ertelecom.ru', 'iperf.ufa.ertelecom.ru'],
     12: ['yola', 'st2.yola.ertelecom.ru', 'iperf.yola.ertelecom.ru' ],
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
    if int(agr[:2]) in cities:
        return cities[int(agr[:2])][0]
    else:
        return 'unknown'


#Кодирование в JSON формат
def json_code(agr, city, os_name, task, ipconf, netstats, netstate, check_host, wlan):
    report_struct = {
        "agreement": agr,
        "city": city,
        "os version": os_name,
        "tasklist": task,
        "ipconfig": ipconf,
        "netstat -s": netstats,
        "netstat -e": netstate,
        "host": check_host,
        "netsh wlan": wlan
    }
    jsonData = json.dumps(report_struct)
    return jsonData


#Сохранение json в файл для отладки
def save_to_file(json_data):
    report = "report.json"
    file = open(report, mode='w', encoding='UTF-8')
    json.dump(json_data, file)
    file.close()


#запуск диагностики при клике на кнопку
@eel.expose
def diag_start(agr):
    #agreement_check(agr)
    #ping_ya()
    #ping_dns()
    #tracert_mail()
    #tracert_vk()
    #nestat()
    #wlanif()
    #print()
    #print(tracert_vk())
    print(ping_gw())
    print(json.loads
                (json_code
                              (
                               agr,
                               get_city(agr),
                               os_name(),
                               tasklist(),
                               ipconfig(),
                               nestats(),
                               nestate(),
                               check_host(),
                               wlanif()
                               )
                )
          )
    #ave_to_file(json_code(agr, city, task, ipconf, netstate))
    return agr

eel.start("main.html", size=(500, 600))
