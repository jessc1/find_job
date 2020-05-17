from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup
from time import sleep

class Find_job():
    def __init__(self):
        self.driver = webdriver.Chrome()
        dataframe = pd.DataFrame(
            columns = ["Título", "Local","Salário", "Descrição", "Empresa"])
        
        for cnt in range(0, 50, 10):
            self.driver.get("https://www.indeed.com.br/empregos?q=python+junior&l=S%C3%A3o+Paulo%2C+Sp&ts=1589730447627&rs=1" + str(cnt))
        
            sleep(10)

            try:
                pop_up = 'None'
                jobs = self.driver.find_element_by_class_name('result')

                for job in jobs:
                    result = job.get_attribute('innerHTML')
                    soup = BeautifulSoup(result, 'html.parser')
                    titulo = soup.find(
                        "a", class_="jobtitle").text.replace('\n', '')
                    local = soup.find(class_="local").text
                    empresa = soup.find(
                        class_="empresa").text.replace('\n', '').strip()
                    try:
                        salario = soup.find(class_="salario").text.replace(
                            '\n', '').strip()
                    except:
                        salario = 'None'

                    print(titulo, local, empresa, salario)

                    summ = job.find_elements_by_class_name("summary")[0]
                    summ.click()
                    sleep(1)
                    job_desc = self.driver.find_element_by_id('vjs-desc').text

                    dataframe = dataframe.append(
                        {'Título': title, 'Local': local, 'Empresa': empresa, 'Descrição': job_desc}, ignore_index=True)
            except:
                pop_up = self.driver.find_element_by_xpath(
                    '/html/body/table[2]/tbody/tr/td/div[2]/div[2]/div[4]/div[3]/div[2]/a')
                pop_up.click()
            dataframe.to_csv("jobs.csv", index=False)

#j = Find_job()