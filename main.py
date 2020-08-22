import eel

eel.init("web")

@eel.expose
def diag_start(agr):
    print(agr)
    return agr

eel.start("main.html", size=(500, 600))
