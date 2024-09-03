from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
import json

tabela = pd.read_excel("Teste APPA.xlsx");

for x in tabela['JSON_ENVIADO']:

    r = json.loads(x);

    print(r['placaVagao'][:3]);
    print(r['placaVagao'][+3:]);

    nav = webdriver.Chrome();

    # Login no Carga Online
    nav.get("https://www.sistemas.appa.pr.gov.br/appa/appa/frame_login.asp?");
    nav.find_element(By.NAME, 'login').send_keys('noc.faturamento');
    nav.find_element(By.NAME, 'passwd').send_keys('parana');
    nav.find_element(By.XPATH, '/html/body/form/table/tbody/tr[2]/td[3]/input').click();

    time.sleep(5)
    #for i, cpf in enumerate(tabela['']): - Inicio do loop por vagão
    # Recebimento de Carga Vagão
    iframe = nav.find_element(By.NAME, 'principal');
    nav.switch_to.frame(iframe);
    nav.find_element(By.XPATH,'//*[@id="listagemcss"]/table/tbody/tr/td[1]/table/tbody/tr[7]/td/a').click();

    time.sleep(5)
    # Identificação do Vagão para cadastro
    nav.find_element(By.XPATH,'//*[@id="RECEBIMENTO_CARGA"]/div[1]/table/tbody/tr[3]/td[2]/input[1]').send_keys(r['placaVagao'][:3]);
    nav.find_element(By.XPATH,'//*[@id="RECEBIMENTO_CARGA"]/div[1]/table/tbody/tr[3]/td[2]/input[2]').send_keys(r['placaVagao'][+3:]);
    nav.find_element(By.XPATH,'//*[@id="RECEBIMENTO_CARGA"]/p/input[1]').click();

    time.sleep(5)
    # Cadastrar Carga de Vagão
    nav.find_element(By.XPATH, '//*[@id="cmbTerminal"]').send_keys(r['cliente']['nome']);
    nav.find_element(By.XPATH, '//*[@id="CARGA_VAGAOcad"]/div/center/table[1]/tbody/tr[4]/td[2]/input[3]').send_keys(r['pesoBruto']);
    nav.find_element(By.XPATH, '//*[@id="CARGA_VAGAOcad"]/div/center/table[1]/tbody/tr[4]/td[2]/input[3]').send_keys(r['tara']);
    nav.find_element(By.XPATH, '//*[@id="cmbProduto"]').send_keys('milho');

    time.sleep(5)
    # Peso
    nav.find_element(By.XPATH, '//*[@id="CARGA_VAGAOcad"]/div/center/table[1]/tbody/tr[10]/td[2]/input').send_keys('75320');
    nav.find_element(By.XPATH, '//*[@id="CARGA_VAGAOcad"]/div/center/table[1]/tbody/tr[11]/td[2]/input').send_keys('25320');

    time.sleep(5)
    # Informações da(s) Nota(s) Fiscal(is)
    nav.find_element(By.XPATH, '//*[@id="txtNfSerie"]').send_keys('50');
    nav.find_element(By.XPATH, '//*[@id="txtNfNumero"]').send_keys('5088');
    nav.find_element(By.XPATH, '//*[@id="txtQuantidade"]').send_keys('50000');
    nav.find_element(By.XPATH, '//*[@id="CARGA_VAGAOcad"]/div/center/table[1]/tbody/tr[18]/td[2]/input[2]').click();

    time.sleep(5)
    # Gravar Vagão
    nav.find_element(By.XPATH, '//*[@id="CARGA_VAGAOcad"]/p/input[1]').click()
    time.sleep(20)


    
# Cadastro NF
nav.find_element(By.XPATH,'/html/body/div/table/tbody/tr/td[1]/table/tbody/tr[11]/td/a').click();
nav.find_element(By.XPATH,'/html/body/form/div/center/table/tbody/tr[1]/td/a[1]/img').click();

# Preencher os dados da Nota
nav.find_element(By.XPATH, '/html/body/form/div/center/table/tbody/tr[2]/td[2]/input').send_keys('35240802003402014710550010000024691055382567');

# Fechar nova janaela
nav._switch_to.window()

#
nav.find_element(By.XPATH, '/html/body/form/div/center/table/tbody/tr[2]/td[2]/input').send_keys('35240802003402014710550010000024691055382567');
time.sleep(10)
