#Importa biblioteca Selenium
from selenium import webdriver
#Importa biblioteca Sleep (Pausa processo)
from time import sleep

#Classe de condições do Chrome Driver
class ChromeAuto:
    def __init__(self):
        self.driver_path = 'chromedriver'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('user-dir=Perfil')
        self.chrome = webdriver.Chrome(
            self.driver_path,
            options=self.options
        )
        
#Função para acessar o site
    def acessa(self, site):
        self.chrome.get(site)    
        
#Localiza botão de Login do site
    def clica_sign_in(self):
        try:
            btn_sign_in = self.chrome.find_element_by_link_text('Sign in')
            btn_sign_in.click()
            
        except Exception as e:
            print('Erro ao clicar em Sign in: ', e)    

#Inserir dados de Logon (User and password)    
    def faz_login(self):
        try:
            input_login = self.chrome.find_element_by_id('login_field')
            input_password = self.chrome.find_element_by_id('password')
            btn_login = self.chrome.find_element_by_name('commit')
            
            #Digitar dados do logon
            input_login.send_keys('processosautoEdy')
            input_password.send_keys('1Processoauto*')
            sleep(5)
            btn_login.click()
        
        except Exception as e:
            print('Erro ao fazer login: ', e)     
        
#Clicar em perfil para efetuar logout
    def clicar_perfil(self):
        try:
            perfil = self.chrome.find_element_by_css_selector('body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details')
            perfil.click()
        except Exception as e:
            print('Erro ao clicar em perfil: ', e)

#Efetuar logout
    def efetuar_logout(self):
        try:
            signout = self.chrome.find_element_by_css_selector('body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details > details-menu > form > button')
            signout.click()
        except Exception as e:
            print('Erro ao clicar em Sign out: ', e)   


          
#Função para fechar Chrome Driver
    def sair(self):
        self.chrome.quit()


#Starts das declarações
if __name__ == '__main__':
    chrome = ChromeAuto()
    chrome.acessa('https://github.com/')
   
    chrome.clicar_perfil()
    sleep(5)
    chrome.efetuar_logout()   
    
    sleep(5)
        
    chrome.clica_sign_in()
    sleep(5)
    chrome.faz_login()
    
    sleep(5)
    
    chrome.clicar_perfil()
    sleep(5)
    chrome.efetuar_logout()      
    
    sleep(11)

    chrome.sair()
