#-*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By



class login_test:
    def __init__(self):
        self.wd=webdriver.Chrome()
        '''
        webdriver包含驱动
        ActionChains/Android/BlackBerry/Chrome/Edge/Firefox/Ie/Opera/Safari/
        '''
        self.wd.get("")
        self.wd.maxmize_window()
        self.user_element=""
        self.passwd_element=""
        self.login_element=""

    def login_run(self):
        try:
            user=WebDriverWait(wd,timeout=10).until(EC.presence_of_element_located(By.ID,str(self.user_element)),message=u'元素加载超时')
            user.send_keys("user")
            passwd=WebDriverWait(wdtimeout=10).until(EC.presence_of_element_located(BY.ID,str(self.passwd_element)),message=u'元素加载超时')
            passwd.send_keys("passwd")
            wd.find_element_by_id(str(self.login_element)).click()
        except Exception as e:
            print e

        
            
        
