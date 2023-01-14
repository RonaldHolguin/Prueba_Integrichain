import re
from turtle import title
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 
driver = webdriver.Chrome(executable_path=r"chromedriver")

class Test : 
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.first_element_selector="#rso > div:nth-child(1) > div > div.g h3 "
        self.second_element_selector="//*[@class = 'yuRUbf']/a"  
        self.count=0   

#escenario #1
    def test1(self,search_keyword,test_keyword):
        self.driver.get("https://www.google.com/")
        d = self.driver.find_element(By.NAME, "q")
        d.send_keys(search_keyword)
        d.send_keys(Keys.ENTER)
        result = self.driver.find_elements(By.XPATH,self.second_element_selector)
        
        for elem in result:
            if self.count==3:
                break
            if elem.text=='':
                continue
            else:
                self.count=self.count+1
                print(elem.text)
                assert test_keyword in elem.text.lower()

#escenario #2
    def test2(self,search_keyword,test_keyword):
        self.driver.get("https://www.google.com/")
        d = self.driver.find_element(By.NAME, "q")
        d.send_keys(search_keyword)
        d.send_keys(Keys.ENTER)
        result = self.driver.find_element(By.CSS_SELECTOR,self.first_element_selector)
        result.click()
        title =  self.driver.title
        assert test_keyword in title.lower()
      
test=Test()
print("Ejecutando escenario 1")
test.test1("test automation", "automation")
print("Ejecutando escenario 2")
test.test2("test automation", "automation")
time.sleep(2)
print("Finalizando Prueba")

