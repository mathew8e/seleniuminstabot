from secrets import username, password
from time import sleep

paddingtime = 0.1

#element assigments
ElementCookieAccept = "/html/body/div[2]/div/div/div/div[2]/button[1]"
ElementLoginUsername = '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input'
ElementLoginPassword = '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input'
ElementLoginLoginButton = '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]'

def operations(dr):
    dr.get("https://www.instagram.com/")
    #padding
    sleep(paddingtime)
    #starting the login operations
    login_operation(dr)

    #waiting for debug
    while 1:
        pass

    print("ending...")
    dr.quit()

def login_operation(dr):
    #clicking on accept cookies
    dr.find_element_by_xpath(ElementCookieAccept).click()
    #padding
    sleep(paddingtime)
    #filling username
    dr.find_element_by_xpath(ElementLoginUsername).send_keys(username)
    #padding
    sleep(paddingtime)
    #filling password
    dr.find_element_by_xpath(ElementLoginPassword).send_keys(password)
    #padding
    sleep(paddingtime)
    dr.find_element_by_xpath(ElementLoginLoginButton).click()
    