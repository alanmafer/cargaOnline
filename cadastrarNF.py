from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import json

with open('testes.json') as arquivo:
    r = json.load(arquivo)

servico = Service(ChromeDriverManager().install());

# Login no Carga Online
nav = webdriver.Chrome(service=servico);
nav.get("https://www.sistemas.appa.pr.gov.br/appa/appa/frame_login.asp?");
nav.find_element(By.NAME, 'login').send_keys('noc.faturamento');
nav.find_element(By.NAME, 'passwd').send_keys('parana');
nav.find_element(By.XPATH, '/html/body/form/table/tbody/tr[2]/td[3]/input').click();

################ Cadastrar NF #######################
iframe = nav.find_element(By.NAME, 'principal');
nav.switch_to.frame(iframe);
nav.find_element(By.XPATH,'/html/body/div/table/tbody/tr/td[1]/table/tbody/tr[11]/td/a').click();
nav.find_element(By.XPATH,'/html/body/form/div/center/table/tbody/tr[1]/td/a[1]/img').click();

# Preencher Dados da NF
if 'notaFiscalPrincipal' in r:
    for idx, r in enumerate(r['notaFiscalPrincipal'], 1):
        if 'chaveAcesso' in r:         
            nav.find_element(By.XPATH, '/html/body/form/div/center/table/tbody/tr[2]/td[2]/input').send_keys({r['chaveAcesso']});
            nav.find_element(By.XPATH, '/html/body/form/div/center/table/tbody/tr[2]/td[2]/input').send_keys('\ue004');
            nav.find_element(By.XPATH, '/html/body/form/div/center/table/tbody/tr[8]/td[2]/input').send_keys({r['destinatario']['cnpjcpf']});
            nav.find_element(By.XPATH, '/html/body/form/div/center/table/tbody/tr[9]/td[2]/input').send_keys({r['emissao']});
            nav.find_element(By.XPATH, '/html/body/form/div/center/table/tbody/tr[10]/td[2]/input').send_keys({r['saida']});
            nav.find_element(By.XPATH, '/html/body/form/div/center/table/tbody/tr[11]/td[2]/input').send_keys({r['valorIPI']});
            nav.find_element(By.XPATH, '/html/body/form/div/center/table/tbody/tr[12]/td[2]/input').send_keys({r['valorICMS']});
            nav.find_element(By.XPATH, '/html/body/form/div/center/table/tbody/tr[13]/td[2]/input[1]').send_keys({r['quantidade']});
            nav.find_element(By.XPATH, '/html/body/form/div/center/table/tbody/tr[14]/td[2]/input').send_keys({r['valorTotal']});
            nav.find_element(By.XPATH, '/html/body/form/div/center/table/tbody/tr[14]/td[2]/input').send_keys('\ue012');
            nav.find_element(By.XPATH, '/html/body/form/div/center/table/tbody/tr[14]/td[2]/input').send_keys('\ue012');
            nav.find_element(By.XPATH, '/html/body/form/div/center/table/tbody/tr[14]/td[2]/input').send_keys(',');

            # Gravar
            nav.find_element(By.XPATH, '/html/body/form/p/input[1]').click();
            nav.find_element(By.XPATH, '/html/body/center/div/table/tbody/tr[3]/td/p/a').click();