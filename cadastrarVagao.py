from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
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

##################### Cadastrar Vagão ###########################
# Recebimento de Carga Vagão
iframe = nav.find_element(By.NAME, 'principal');
nav.switch_to.frame(iframe);
nav.find_element(By.XPATH,'//*[@id="listagemcss"]/table/tbody/tr/td[1]/table/tbody/tr[7]/td/a').click();

# Identificação do Vagão para cadastro
nav.find_element(By.XPATH,'//*[@id="RECEBIMENTO_CARGA"]/div[1]/table/tbody/tr[3]/td[2]/input[1]').send_keys(r['placaVagao'][:3]);
nav.find_element(By.XPATH,'//*[@id="RECEBIMENTO_CARGA"]/div[1]/table/tbody/tr[3]/td[2]/input[2]').send_keys(r['placaVagao'][+3:]);
nav.find_element(By.XPATH,'//*[@id="RECEBIMENTO_CARGA"]/p/input[1]').click();

# Cadastrar Carga do Vagão
codTerminal = (r['codTerminal'])
codTerminal = str(codTerminal) + ',21';
dropdown_element = nav.find_element(By.XPATH,'/html/body/form/div/center/table[1]/tbody/tr[2]/td[2]/select');
select =  Select(dropdown_element);
select.select_by_value(codTerminal);

if codTerminal != '10,21': # POOL Corredor
    for i in range (18): 
        nav.find_element(By.XPATH, '/html/body/form/div/center/table[1]/tbody/tr[3]/td[2]/input').send_keys('\ue003');
    nav.find_element(By.XPATH, '/html/body/form/div/center/table[1]/tbody/tr[3]/td[2]/input').send_keys(r['cliente']['cnpjcpf']);
    nav.find_element(By.XPATH, '/html/body/form/div/center/table[1]/tbody/tr[3]/td[2]/input').send_keys('\ue004');
else:
    print('é diferente');

nav.find_element(By.XPATH, '/html/body/form/div/center/table[1]/tbody/tr[4]/td[2]/input[3]').send_keys(r['exportador']['cnpjcpf']);
nav.find_element(By.XPATH, '/html/body/form/div/center/table[1]/tbody/tr[4]/td[2]/input[3]').send_keys('\ue004');


time.sleep(10);
dropdown_element = nav.find_element(By.XPATH,'/html/body/form/div/center/table[1]/tbody/tr[6]/td[2]/select');
select =  Select(dropdown_element);
select.select_by_value(r['codProduto']);

# # Peso
nav.find_element(By.XPATH, '//*[@id="CARGA_VAGAOcad"]/div/center/table[1]/tbody/tr[10]/td[2]/input').send_keys(r['pesoBruto']);
nav.find_element(By.XPATH, '//*[@id="CARGA_VAGAOcad"]/div/center/table[1]/tbody/tr[11]/td[2]/input').send_keys(r['tara']);

# # Informações da(s) Nota(s) Fiscal(is)
nav.find_element(By.XPATH, '//*[@id="txtNfSerie"]').send_keys('50');
# nav.find_element(By.XPATH, '//*[@id="txtNfNumero"]').send_keys('5088');
# nav.find_element(By.XPATH, '//*[@id="txtQuantidade"]').send_keys('50000');
# nav.find_element(By.XPATH, '//*[@id="CARGA_VAGAOcad"]/div/center/table[1]/tbody/tr[18]/td[2]/input[2]').click();

# Gravar Vagão
#nav.find_element(By.XPATH, '//*[@id="CARGA_VAGAOcad"]/p/input[1]').click()
# time.sleep(20)
