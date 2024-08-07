from selenium import webdriver
from selenium.webdriver.common.by import By
import time

nav = webdriver.Chrome()

nav.get("https://www.sistemas.appa.pr.gov.br/appa/appa/frame_login.asp?")

nav.find_element(By.NAME, 'login').send_keys('noc.faturamento')
nav.find_element(By.NAME, 'passwd').send_keys('parana')
nav.find_element(By.XPATH, '/html/body/form/table/tbody/tr[2]/td[3]/input').click()

iframe = nav.find_element(By.NAME, 'principal')
nav.switch_to.frame(iframe)
nav.find_element(By.XPATH,'//*[@id="listagemcss"]/table/tbody/tr/td[1]/table/tbody/tr[7]/td/a').click()

nav.find_element(By.XPATH,'//*[@id="RECEBIMENTO_CARGA"]/div[1]/table/tbody/tr[3]/td[2]/input[1]').send_keys("FHD")
nav.find_element(By.XPATH,'//*[@id="RECEBIMENTO_CARGA"]/div[1]/table/tbody/tr[3]/td[2]/input[2]').send_keys("8798457")
nav.find_element(By.XPATH,'//*[@id="RECEBIMENTO_CARGA"]/p/input[1]').click()

#time.sleep(20)
