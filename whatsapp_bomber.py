import os
import pyfiglet
import webbrowser
from colorama import Fore
from simple_chalk import chalk
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

def wbbomber():
    driver = None  # Global variable to store the driver object
    
    def main():
        clean()
        banner()
        ans=True
        bomb()
    
    def setup_chrome():
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
    
        # Set path to the ChromeDriver executable.
        chromedriver_path = os.path.join(os.getcwd(), 'chromedriver.exe')
        service = Service(chromedriver_path)
    
        global driver  # Use the global driver variable
        driver = webdriver.Chrome(service=service, options=options)
        driver.get('https://web.whatsapp.com/')
    
        return driver  # Return the initialized driver object
    
    def setup_firefox():
        options = webdriver.FirefoxOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
    
        # Set path to the GeckoDriver executable.
        geckodriver_path = os.path.join(os.getcwd(), 'geckodriver')
        service = FirefoxService(geckodriver_path)
    
        global driver  # Use the global driver variable
        driver = webdriver.Firefox(service=service, options=options)
        driver.get('https://web.whatsapp.com/')
    
        return driver  # Return the initialized driver object
    
    
    def clean():
        # For Windows
        if os.name == 'nt':
            _ = os.system('cls')
        # For macOS and Linux
        else:
            _ = os.system('clear')
    
    def banner():
        foreground_colors = [Fore.MAGENTA, Fore.WHITE, Fore.MAGENTA, Fore.MAGENTA, Fore.WHITE, Fore.MAGENTA]
    
        f = pyfiglet.Figlet(font="stop")
        text = f.renderText('Whatsapp Bomber')
    
        lines = text.split('\n')
        cur_fore = 0
        for line in lines:
            foreground_color = foreground_colors[cur_fore]  # Get the foreground color based on the current index
            cur_fore = (cur_fore + 1) % len(foreground_colors)  # Increment the index and wrap around if it exceeds the list length
            colored_line = f"{foreground_color}{line}"  # Add the foreground color to the line
            print(colored_line)
            sleep(0.05)
    
        # Reset the colorama settings
        print(Fore.RESET)
    
    def bomb():
        name = input(chalk.green('Enter the name of user or group: '))
        msg = input(chalk.green('Enter your message: '))
        count = int(input(chalk.green('Enter the count: ')))
    
        input(chalk.green('Enter any key whenever you\'re ready!'))
    
        user = driver.find_element(By.XPATH, f'//span[@title="{name}"]')
        user.click()
    
        print(chalk.green('Waiting 4 seconds to let WhatsApp load...'))
        sleep(4)
        # The classname of message box may vary.
        msg_box = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
    
        for i in range(count):
            msg_box.send_keys(msg)
            # The classname of send button may vary.
            button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span')
            button.click()
    
        print(chalk.green('Bombing Complete!!'))
        sleep(4)
        main()
    
    # Choose the appropriate setup function based on the OS
    if os.name == 'nt':
        driver = setup_chrome()
    else:
        driver = setup_firefox()
    
    input(chalk.green('Enter any key after scanning QR code'))
    main()
    