import eel

eel.init("web")

# проверка номера договора
def agreement_check(agr):
    assert agr.isdigit(), "Номер договора должен быть положительным числом"
    assert len(str(agr)) == 10, "Номер договора должен состоять из 10 чисел"

#Запуск диагностики при клике на кнопку
@eel.expose
def diag_start(agr):
    agreement_check(agr)
    print(agr)
    return agr

eel.start("main.html", size=(500, 600))
