def wpbombingwin():
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.options import Options
    from about import menu,about
    import time
    import os
    import platform


    options = Options()
    options.add_argument("--log-level=3")
    wcr_dict = os.getcwd() + '//chromedriver.exe'

    browser = webdriver.Chrome(executable_path=wcr_dict, chrome_options=options)

    browser.get('https://web.whatsapp.com/')

    os.system('cls')
    about()
    menu()
    print('    |-> 4')

    try:
        confirm = WebDriverWait(browser, 600).until(EC.presence_of_element_located(
            (By.CLASS_NAME, "_3BDr5")))
    finally:
        pass

    browser.set_window_position(-10000,0)

    wp_victim = input("    |-$ Victim's Phone Number (with country code) > ")
    bad_chars = ['+', ' ', '-'] 

    for i in bad_chars : 
        wp_victim = wp_victim.replace(i, '') 

    mode = input('''    |
    |-PRESS------------------|
    | 1] Repetitive Mode     |
    | 2] Script/Lyrical Mode |
    | Facing Problem ?       |
    |    Check out README.MD |
    |------------------------|
    |-> ''')

    if mode.lower() == '1' or mode.lower() == 'repetitive mode':
        reptxt = input('    |-$ Word/Sentence that you want to send Multiple Times > ')
        repcount = int(input('    |-$ How many times ? > '))

    elif mode.lower() == '2' or mode.lower() == 'script/lyrical mode':
        lyrics = open("lyrics.txt","r+")  
        splitedlyrics = (lyrics.read().split()) 

    else:
        print('    |-} invalid input !')
        return


    browser.get(f'https://web.whatsapp.com/send?phone={wp_victim}&text&source&data&app_absent')

    try:
        confirm = WebDriverWait(browser, 60).until(EC.presence_of_element_located(
            (By.CLASS_NAME, "_2O84H")))
    finally:
        pass 

    try:
        confirm = WebDriverWait(browser, 80).until(EC.presence_of_element_located(
            (By.CLASS_NAME, "DuUXI")))
    except:
        print("    |-} please recheck victim's mobile no. ")
    finally:
        pass
 
    if mode.lower() == '1' or mode.lower() == 'repetitive mode':
        for i in range(repcount):
            browser.find_elements_by_css_selector('.DuUXI div')[2].send_keys(reptxt + Keys.ENTER)

    elif mode.lower() == '2' or mode.lower() == 'script/lyrical mode':
        for words in splitedlyrics:
            browser.find_elements_by_css_selector('.DuUXI div')[2].send_keys(words + Keys.ENTER)
            
    time.sleep(5)
    print(
    '''    |-} Done !
    |-----------------------------------------------------------''')
    browser.quit()

def wpbombinglinux():
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.firefox.options import Options
    from about import menu,about
    import time
    import os
    import platform


    options = Options()
    options.add_argument("--log-level=3")
    cr_dict = os.getcwd() + '/geckodriver'
        
    browser = webdriver.Firefox(executable_path=cr_dict , options=options)

    browser.get('https://web.whatsapp.com/')

    try:
        confirm = WebDriverWait(browser, 600).until(EC.presence_of_element_located(
            (By.CLASS_NAME, "_3BDr5")))
    finally:
        pass
  
    browser.minimize_window()

    wp_victim = input("    |-$ Victim's Phone Number (with country code) > ")
    bad_chars = ['+', ' ', '-'] 

    for i in bad_chars : 
        wp_victim = wp_victim.replace(i, '') 

    mode = input('''    |
    |-PRESS------------------|
    | 1] Repetitive Mode     |
    | 2] Script/Lyrical Mode |
    | Facing Problem ?       |
    |    Check out README.MD |
    |------------------------|
    |-> ''')

    if mode.lower() == '1' or mode.lower() == 'repetitive mode':
        reptxt = input('    |-$ Word/Sentence that you want to send Multiple Times > ')
        repcount = int(input('    |-$ How many times ? > '))

    elif mode.lower() == '2' or mode.lower() == 'script/lyrical mode':
        lyrics = open("lyrics.txt","r+")  
        splitedlyrics = (lyrics.read().split()) 

    else:
        print('    |-} invalid input !')
        return


    browser.get(f'https://web.whatsapp.com/send?phone={wp_victim}&text&source&data&app_absent')

    try:
        confirm = WebDriverWait(browser, 60).until(EC.presence_of_element_located(
            (By.CLASS_NAME, "_2O84H")))
    finally:
        pass 

    try:
        confirm = WebDriverWait(browser, 80).until(EC.presence_of_element_located(
            (By.CLASS_NAME, "DuUXI")))
    except:
        print("    |-} please recheck victim's mobile no. ")
    finally:
        pass
 
    if mode.lower() == '1' or mode.lower() == 'repetitive mode':
        for i in range(repcount):
            browser.find_elements_by_css_selector('.DuUXI div')[2].send_keys(reptxt + Keys.ENTER)

    elif mode.lower() == '2' or mode.lower() == 'script/lyrical mode':
        for words in splitedlyrics:
            browser.find_elements_by_css_selector('.DuUXI div')[2].send_keys(words + Keys.ENTER)
           
    time.sleep(5)
    print(
    '''    |-} Done !
    |-----------------------------------------------------------''')
    browser.quit()
