import random
import pyfiglet
import webbrowser
import os
from colorama import Fore
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# Import the WebDriverWait and expected_conditions from the selenium.webdriver.support.ui library
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# impprt the TimeoutException from the selenium.common.exceptions library
from selenium.common.exceptions import TimeoutException

driver = None  # Global variable to store the driver object

def main():
    clean()
    banner()
    ans=True
    while ans:
        print("""
        1. Start bombing
        2. Support original creator
        3. Exit/Quit
        """)
        ans=input("What would you like to do? ")
        if ans=="1":
            clean()
            bomb()
        elif ans=="2":
            webbrowser.open('https://github.com/bhattsameer/Bombers/')
            print("\n Thanks for supporting the original creator!")
            sleep(0.3)
            main()
        elif ans=="3":
            print("\n Goodbye")
            ans = None
            exit()
        else:
            print("\n Not a valid choice. Try again.")
            sleep(0.3)
            main()

def setup():
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    # Set path to the ChromeDriver executable.
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

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
    text = f.renderText('WB0MB')

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
    name = input('Enter the name of user or group: ')
    msg = input('Enter your message: ')
    count = int(input('Enter the count: '))

    input('Enter any key whenever you\'re ready!')

    user = driver.find_element(By.XPATH, f'//span[@title="{name}"]')
    user.click()

    print('Waiting 4 seconds to let WhatsApp load...')
    sleep(4)
    # The classname of message box may vary.
    for i in range(count):
        try:
            msg_box = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p'))
            )
            msg_box.send_keys(msg)
            button = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button')
            button.click()
        except TimeoutException:
            print("Couldn't find the message box. The page might have changed or not fully loaded.")
            return

    for i in range(count):
        msg_box.send_keys(msg)
        # The classname of send button may vary.
        button = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button')
        button.click()

    print('Bombing Complete!!')
    sleep(4)
    main()

driver = setup()
input('Enter any key after scanning QR code')
main()