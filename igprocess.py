def igbombingwin():
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.options import Options
    import platform
    from about import menu,about
    import time
    import os
    import sys

    ig_username = input('    |-$ Your Username > ')
    ig_password = input('    |-$ Your Password > ')
    ig_victim = input("    |-$ Victim's Username > ")
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

    print('    |-} Logging in...')

    options = Options()
    #options.headless = True
    options.add_argument("--log-level=3")

    wcr_dict = os.getcwd() + '//chromedriver.exe'

    browser = webdriver.Chrome(executable_path=wcr_dict, chrome_options=options)

    os.system('cls')
    about()
    menu()
    print(f'''    |-> 3
    |-$ Your Username > {ig_username}
    |-$ Your Password > {ig_password}
    |-$ Victim's Username > {ig_victim}
    |
    |-PRESS------------------|
    | 1] Repetitive Mode     |
    | 2] Script/Lyrical Mode |
    | Facing Problem ?       |
    |    Check out README.MD |
    |------------------------|
    |-> {mode}''')

    if mode.lower() == '1' or mode.lower() == 'repetitive mode':
        print(
f'''    |-$ Word/Sentence that you want to send Multiple Times > {reptxt}
    |-$ How many times ? > {repcount}''')

        print('    |-} Logging in...')
    
    browser.get('https://www.instagram.com/accounts/login')
    time.sleep(2)
    username_bar = browser.find_element_by_name('username')
    username_bar.send_keys(ig_username)
    password_bar = browser.find_element_by_name('password')
    password_bar.send_keys(ig_password + Keys.ENTER)
    time.sleep(7)

    if browser.current_url == 'https://www.instagram.com/':
        pass
    else:
        try:
            confirm = WebDriverWait(browser, 20).until(EC.presence_of_element_located(
                (By.CLASS_NAME, "coreSpriteKeyhole")))
        except:
            print('    |-} Log in Failed !')
            return   
        finally:
            pass

    print('    |-} Logged in Successfully !')

    browser.get('https://www.instagram.com/direct/new/')

    try:
        confirm = WebDriverWait(browser, 5).until(EC.presence_of_element_located(
            (By.CLASS_NAME, "mt3GC")))
        browser.find_element_by_class_name("mt3GC").click()
    except:
        pass

    try:
        confirm = WebDriverWait(browser, 20).until(EC.presence_of_element_located(
            (By.NAME, "queryBox")))
    finally:
        pass

    browser.find_element_by_name('queryBox').send_keys(ig_victim)

    try:
        confirm = WebDriverWait(browser, 20).until(EC.presence_of_element_located(
            (By.CLASS_NAME, "dCJp8")))
    finally:
        pass 

    time.sleep(2)

    browser.find_element_by_class_name('dCJp8').click()

    time.sleep(1)

    browser.find_element_by_class_name('rIacr').click()

    try:
        confirm = WebDriverWait(browser, 20).until(EC.presence_of_element_located(
            (By.XPATH, "//textarea")))
    finally:
        pass 

    if ig_victim == browser.find_elements_by_class_name('_7UhW9.vy6Bb.qyrsm.KV-D4.fDxYl')[1].text:
        pass
    else:
        print('    |-} no such user named ' + ig_victim)
        return

    if mode.lower() == '1' or mode.lower() == 'repetitive mode':
        for i in range(repcount):
            browser.find_element_by_xpath("//textarea").send_keys(reptxt + Keys.ENTER)

    elif mode.lower() == '2' or mode.lower() == 'script/lyrical mode':
        for words in splitedlyrics:
            browser.find_element_by_xpath("//textarea").send_keys(words + Keys.ENTER)

    time.sleep(4)

    print(
'''    |-} Done !
    |-----------------------------------------------------------''')
    browser.quit()

def igbombinglinux():
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.firefox.options import Options
    import platform
    from about import menu,about
    import time
    import os
    import sys

    ig_username = input('    |-$ Your Username > ')
    ig_password = input('    |-$ Your Password > ')
    ig_victim = input("    |-$ Victim's Username > ")
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

    print('    |-} Logging in...')

    options = Options()
    options.headless = True
    options.add_argument("--log-level=3")

    cr_dict = os.getcwd() + '/geckodriver'

    browser = webdriver.Firefox(executable_path=cr_dict , options=options)
    
    browser.get('https://www.instagram.com/accounts/login')
    time.sleep(2)
    username_bar = browser.find_element_by_name('username')
    username_bar.send_keys(ig_username)
    password_bar = browser.find_element_by_name('password')
    password_bar.send_keys(ig_password + Keys.ENTER)
    time.sleep(7)

    if browser.current_url == 'https://www.instagram.com/':
        pass
    else:
        try:
            confirm = WebDriverWait(browser, 20).until(EC.presence_of_element_located(
                (By.CLASS_NAME, "coreSpriteKeyhole")))
        except:
            print('    |-} Log in Failed !')
            return   
        finally:
            pass

    print('    |-} Logged in Successfully !')

    browser.get('https://www.instagram.com/direct/new/')

    try:
        confirm = WebDriverWait(browser, 5).until(EC.presence_of_element_located(
            (By.CLASS_NAME, "mt3GC")))
        browser.find_element_by_class_name("mt3GC").click()
    except:
        pass

    try:
        confirm = WebDriverWait(browser, 20).until(EC.presence_of_element_located(
            (By.NAME, "queryBox")))
    finally:
        pass

    browser.find_element_by_name('queryBox').send_keys(ig_victim)

    try:
        confirm = WebDriverWait(browser, 20).until(EC.presence_of_element_located(
            (By.CLASS_NAME, "dCJp8")))
    finally:
        pass 

    time.sleep(2)
 
    browser.find_element_by_class_name('dCJp8').click()

    time.sleep(1)

    browser.find_element_by_class_name('rIacr').click()

    try:
        confirm = WebDriverWait(browser, 20).until(EC.presence_of_element_located(
            (By.XPATH, "//textarea")))
    finally:
        pass 

    if ig_victim == browser.find_elements_by_class_name('_7UhW9.vy6Bb.qyrsm.KV-D4.fDxYl')[1].text:
        pass
    else:
        print('    |-} no such user named ' + ig_victim)
        return

    if mode.lower() == '1' or mode.lower() == 'repetitive mode':
        for i in range(repcount):
            browser.find_element_by_xpath("//textarea").send_keys(reptxt + Keys.ENTER)

    elif mode.lower() == '2' or mode.lower() == 'script/lyrical mode':
        for words in splitedlyrics:
            browser.find_element_by_xpath("//textarea").send_keys(words + Keys.ENTER)

    time.sleep(4)

    print(
'''    |-} Done !
    |-----------------------------------------------------------''')
    browser.quit()
