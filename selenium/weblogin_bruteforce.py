#-*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By



class login_test:
    def __init__(self):
        self.wd=webdriver.Firefox()
        '''
        webdriver包含驱动
        ActionChains/Android/BlackBerry/Chrome/Edge/Firefox/Ie/Opera/Safari/
        '''
        self.wd.get("http://10.0.3.220/DVWA/login.php")
        # self.wd.maxmize_window()
        self.user_element=""
        self.passwd_element="username"
        self.login_element="password"

    def login_run(self):
        try:
            user=WebDriverWait(self.wd,timeout=10).until(EC.presence_of_element_located(By.ID,str(self.user_element)),message=u'元素加载超时')
            user.send_keys("user")
            passwd=WebDriverWait(self.wd,timeout=10).until(EC.presence_of_element_located(BY.ID,str(self.passwd_element)),message=u'元素加载超时')
            passwd.send_keys("passwd")
            self.wd.find_element_by_id(str(self.login_element)).click()
        except Exception as e:
            print e


if __name__=='__main__':
	a=login_test()
	a.login_run()
