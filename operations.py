ElementCookieAccept = "/html/body/div[2]/div/div/div/div[2]/button[1]"


def operations(dr):
    dr.get("https://www.instagram.com/")

    login_operation(dr)

    while 1:
        pass

    print("ending...")
    dr.quit()

def login_operation(dr):
    dr.find_element_by_xpath(ElementCookieAccept).click()