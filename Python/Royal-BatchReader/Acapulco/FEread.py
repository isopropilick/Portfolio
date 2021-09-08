from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from seleniumwire import webdriver
from seleniumwire.utils import decode
import time
import json


def run():
    # Constant data
    sala = 'D-SR MX  Park Royal Acapulco'
    finaldata = dict()
    outdir = "Out/"

    # Data import
    f = open(outdir + 'availabledata.json', )
    data = json.load(f)
    f.close()
    print("\n\033[92mData available:")
    for i in data['files']:
        print("\033[93m- " + str(i['file']))

    # Data manipulation
    searches = dict()
    print("\n\033[92mSearches to perform:")
    for i in data['files']:
        searches[data['files'].index(i)] = str(i['data']).split("-")
    for x in searches:
        print("\033[93m" +
              str(x + 1) + " - From: " +
              str(searches[x][0]) + "/" +
              str(searches[x][2]) + "/" +
              str(searches[x][3]) + " To: " +
              str(searches[x][1]) + "/" +
              str(searches[x][2]) + "/" +
              str(searches[x][3]) + " For site: " +
              str(sala)
              )
    # Driver setup
    print("\n\033[96m* Launching chrome...")
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome('chromedriver', chrome_options=options)

    # Login
    print("\033[96m* Loading page...")
    driver.get("http://agile-qk.com:50004/login")
    driver.find_element_by_class_name("inputUsuario").send_keys("appComVtaMkt")
    driver.find_element_by_class_name("inputPassword").send_keys("r0y41QK20")
    driver.find_element_by_class_name("entrarButton").click()
    print("\033[96m* Login successful..")

    # Profile type modal
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "title-modal"))
    )
    driver.find_element(By.XPATH, "//input[contains(@ng-reflect-value,'15')]").click()
    driver.find_element(By.XPATH, "//button[contains(text(),'Aceptar')]").click()
    print("\033[96m* Profile selected...")

    # Navigation menu
    driver.find_element(By.XPATH, "//*[@id=\"navbarNav\"]/ul[2]/button").click()
    driver.find_element(By.XPATH, "//*[@id=\"adminUsuarios\"]/ul[6]/a").click()
    time.sleep(2)
    print("\033[96m* Report page loaded...")
    del driver.requests
    print("\033[96m* Clearing HTTP requests...")

    # Filter report for each available file
    for x in searches:
        dataname = str(searches[x][0]) + "-" + str(searches[x][1]) + "-" + str(searches[x][2]) + "-" + str(
            searches[x][3])
        sdate = (str(searches[x][3]) + "-" + str(searches[x][2]) + "-" + str(searches[x][0]))
        fdate = (str(searches[x][3]) + "-" + str(searches[x][2]) + "-" + str(searches[x][1]))
        print("\033[93m* Starting search #" + str(x + 1) + "...")
        driver.find_element(By.XPATH, "//select[contains(@formcontrolname,'systemId')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//option[contains(text(), 'Ventas')]").click()
        driver.find_element(By.XPATH, "//select[contains(@formcontrolname,'saleRoomId')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//option[contains(text(), '" + sala + "')]").click()
        driver.find_element(By.XPATH, "//input[contains(@formcontrolname,'startDate')]").clear()
        driver.find_element(By.XPATH, "//input[contains(@formcontrolname,'startDate')]").send_keys(sdate)
        driver.find_element(By.XPATH, "//input[contains(@formcontrolname,'finalDate')]").clear()
        driver.find_element(By.XPATH, "//input[contains(@formcontrolname,'finalDate')]").send_keys(fdate)
        driver.find_element(By.XPATH, "//button[contains(text(),'Buscar')]").click()
        time.sleep(1)
        for request in driver.requests:
            if request.response:
                if 'application/json' in request.response.headers['Content-Type'] and '/income/filter' in request.url:
                    body = decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity'))
                    body = body.decode("utf-8", "replace")
        del driver.requests
        print("\033[96m   * Sucsesful...\n\033[96m   * Clearing HTTP requests...")
        finaldata[dataname] = str(body)
    driver.quit()
    # Result dict manipulation
    print("\033[96m* Response data manipulation...")
    finalstring = "{\"searches\":{"
    for x in finaldata:
        finaldata[x] = "[" + str(finaldata[x][2:-2]) + "]"
        prestring = str(finaldata[x])
        prestring = prestring.replace("[", "{").replace("]", "}")
        finalstring = finalstring + "\"" + str(x) + "\":[" + prestring + "],"
    finalstring = finalstring[:-1] + "}}"

    # Write out file
    print("\033[92m* Writing files...")
    finaljson = json.loads(finalstring)
    for i in finaljson['searches']:
        with open(str(outdir) + "FE-" + str(i) + ".json", "w", encoding='utf-8') as out:
            json.dump(finaljson['searches'][i], out, ensure_ascii=False, indent=4)
        print("\033[93m* Search results for: " + str(i) + " Saved as: " + str(outdir) + "FE-" + str(i) + ".json")
