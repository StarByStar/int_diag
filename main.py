import eel

eel.init("web")


# проверка валидности номера договора
def agreement_check(agr):
    assert agr.isdigit(), "Номер договора должен быть положительным числом"
    assert len(str(agr)) == 12, "Номер договора должен состоять из 12 чисел"


# определение города Клиента по № договора
def get_city(agr):
    cities = \
    {10: 'ufa',
     12: 'yola',
     16: 'kazan',
     17: 'chel',
     18: 'izhevsk',
     21: 'cheb',
     22: 'barnaul',
     23: 'krd',
     24: 'krsk',
     27: 'mgn',
     30: 'ulu',
     32: 'bryansk',
     34: 'volgograd',
     36: 'voronezh',
     38: 'irkutsk',
     43: 'kirov',
     45: 'kurgan',
     46: 'kursk',
     48: 'lipetsk',
     52: 'nn',
     54: 'nsk',
     55: 'omsk',
     56: 'oren',
     58: 'penza',
     59: 'perm',
     61: 'rostov',
     62: 'ryazan',
     63: 'samara',
     64: 'saratov',
     66: 'ekat',
     69: 'tver',
     70: 'tomsk',
     71: 'tula',
     72: 'tmn',
     73: 'ulsk',
     76: 'yar',
     77: 'msk',
     78: 'spb'
     }
    if int(agr[:2]) in cities:
        return cities[int(agr[:2])]
    else:
        return 'unknown'


#Запуск диагностики при клике на кнопку
@eel.expose
def diag_start(agr):
    agreement_check(agr)
    city = get_city(agr)
    print(agr)
    print(city)
    return agr

eel.start("main.html", size=(500, 600))
