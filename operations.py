from secrets import username, password
from time import sleep
from xpath import read_xpath
from utils import wait_until_load, get_current_url

paddingtime = 0.1

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
    dr.find_element_by_xpath(read_xpath("login_user","ElementCookieAccept")).click()
    #padding
    sleep(paddingtime)
    #filling username
    dr.find_element_by_xpath(read_xpath("login_user","ElementLoginUsername")).send_keys(username)
    #padding
    sleep(paddingtime)
    #filling password
    dr.find_element_by_xpath(read_xpath("login_user","ElementLoginPassword")).send_keys(password)
    #padding
    sleep(paddingtime)
    dr.find_element_by_xpath(read_xpath("login_user","ElementLoginLoginButton")).click()
    

    wait_until_load(dr, "https://www.instagram.com/accounts/onetap/?next=%2F")
    sleep(paddingtime)
    dr.find_element_by_xpath(read_xpath("login_user","ElementSaveLoginInfoDecline")).click()
    sleep(paddingtime)
    dr.find_element_by_xpath(read_xpath("homescreen_operations","ElementTurnOnNotificationsDecline")).click()
    #just debuging if we are logged in
    if get_current_url(dr) == "https://www.instagram.com/":
        print("-----Successful login------")


    
    