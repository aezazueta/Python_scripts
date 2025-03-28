# enlace para descargar la versión del chromeDriver de acuerdo a la versión de chrome
# que se esté usando: 
# https://storage.googleapis.com/chrome-for-testing-public/125.0.6422.142/win64/chromedriver-win64.zip
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
import time

# opciones para mantener el navegador abierto
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
# a partir de la V4 la carga del webdriver se hace asi
serv = Service(r"chromedriver-win64//chromedriver.exe")
driver = webdriver.Chrome(service=serv, options=chrome_options)


# diccionario para manejar los xpath de las opciones en el campo sexo
sex_dict = {
    'Hombre':'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[2]/div[3]',
    'Mujer':'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[2]/div[4]',
    'LGBT-WXYZ':'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[2]/div[5]/span'
}
# diccionario para manejar los xpath de las opciones en el campo academia
academiy_dict = {
    'Sistemas':'//*[@id="i29"]/div[3]/div',
    'Gestión':'//*[@id="i32"]/div[3]/div',
    'Industrial':'//*[@id="i35"]/div[3]/div',
    'Alimentarias':'//*[@id="i38"]/div[3]/div',
    'Innovación':'//*[@id="i41"]/div[3]/div'
} 

# leyendo la DB
df = pd.read_csv('database.csv', encoding='latin-1')

# ciclo para recorrer y capturar en el formulario cada una de las estradas de la DB
for row, datos in df.iterrows():
    # extracción de datos de cada entrada
    nombre = datos['Nombre']
    apPat_data = datos['Apellido Pat']
    apMat_data = datos['Apellido Mat']
    edad = datos['Edad']
    sex = datos['Sexo']
    correo = datos['CorreoE']
    academy = datos['Academia']
    
    # abriendo formulario
    driver.get('https://docs.google.com/forms/d/e/1FAIpQLSckbkSpiFOifgIh4Zp2ouSNFMFuRTH_ty2LoKsHI7QtvdP5Yw/viewform')
    # maximizar la ventana del navegador
    driver.maximize_window()
    #print(df)

    #Ingresar nombre
    time.sleep(2)
    input_name = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
    name = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, input_name))
    )
    name.send_keys(nombre)

    #Ingresar apellido paterno
    input_apPat = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
    apPat = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, input_apPat))
    )
    apPat.send_keys(apPat_data)

    #Ingresar apellido materno
    input_apMat = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
    apMat = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, input_apMat))
    )
    apMat.send_keys(apMat_data)

    #Ingresar edad
    input_age = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input'
    age = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, input_age))
    )
    age.send_keys(edad)



    #Ingresar Sexo (combo box)
    # Ojo: en el navegador poner el cursor en la flecha del combobox y darle inspeccionar 2 veces
    cmb_sx = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div[2]'
    combo_sex = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, cmb_sx))
    )
    combo_sex.click()

    sex = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, sex_dict[sex]))
    )
    sex.click()
    time.sleep(1)


    #Ingresar correo electrónico
    input_email = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input'
    email = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, input_email))
    )
    email.send_keys(correo)


    # Ingresar Academia (radio buttons)
    academy = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, academiy_dict[academy]))
    )
    academy.click()

    # clic en el botón registrar
    btn_submit = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span'
    submit = WebDriverWait(driver,10).until(
        EC.visibility_of_element_located((By.XPATH, btn_submit))
    )
    submit.click()