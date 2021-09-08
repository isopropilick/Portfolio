from os import listdir
from os.path import *
import os.path
import shutil


def run():
    if os.path.isdir('Out/'):
        print("\033[92mOutput directory exist, cleaning..")
        shutil.rmtree('Out/')
        os.mkdir('Out/')
    else:
        print("\033[92mOutput directory does not exist, creating..")
        os.mkdir('Out/')
    files = [f for f in listdir('Data/') if isfile(join('Data/', f))]
    data = []
    meses = [
        "ENERO", "FEBRERO", "MARZO", "ABRIL", "MAYO", "JUNIO",
        "JULIO", "AGOSTO", "SEPTIEMBRE", "OCTUBRE", "NOVIEMBRE", "DICIEMBRE"]
    for x in files:
        for mes in meses:
            if mes in x:
                mi = str(meses.index(mes) + 1)
                m = mes
                if len(mi) == 1:
                    mi = "0" + mi
        data.append(
            x
            .replace("NOMINA", "")
            .replace("AL", "-")
            .replace("DE", "")
            .replace(m, "-"+mi+"-")
            .replace(" ", "")
            .replace(".xlsx", "")
            )
    json = "{\"files\":["
    for x in files:
        json = json + "{\"file\":\"" + str(x) + "\",\"data\":\"" + str(data[files.index(x)]) + "\"},"
    json = json[:-1] + "]}"
    with open('Out/availabledata.json', 'w') as f:
        f.write(json)
