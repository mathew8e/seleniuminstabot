

def get_current_url(browser):
    """ Get URL of the loaded webpage """
    try:
        current_url = browser.execute_script("return window.location.href")

    except WebDriverException:
        try:
            current_url = browser.current_url

        except WebDriverException:
            current_url = None

    return current_url

def wait_until_load(dr, url):
    while url != get_current_url(dr):
        #this looks like shit but i dont know how to make it differently
        pass

def wait():
    #simple stalling the program
    while 1:
        pass
