import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

user_agent = "Mozilla/5.0 (X11; Linux x86_64; rv:88.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
options = webdriver.FirefoxOptions()
options.headless = True
options.add_argument(f'user-agent={user_agent}')
options.add_argument("--window-size=1920,1080")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-running-insecure-content')
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--start-maximized")
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument(f'user-agent={user_agent}')
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--allow-running-insecure-content')
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--proxy-server='direct://'")
chrome_options.add_argument("--proxy-bypass-list=*")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--no-sandbox')

def get_youtube_video():
    try:
        driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
        open_browser(driver)
    except:
        driver = webdriver.Firefox(executable_path='./youtube/geckodriver', options=options)
        open_browser(driver)

def open_browser(driver):
    global title, link
    title = link = None
    wait = WebDriverWait(driver, 10)

    driver.get("https://www.youtube.com/channel/UCblA_CnykG2Dw_6IMwZ9z9A/videos")

    agreement = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/c-wiz/div/div/div/div[2]/div[1]/div[4]/form/div[1]/div/button/div[2]'))).click()
    video = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="video-title"]')))
    title = video.text

    read_checker = open('./youtube/checker.txt', 'r')
    latest_title = read_checker.readline()

    if latest_title == title:
        driver.close()
        title = link = None
        return
    else:
        update_checker = open('./youtube/checker.txt', 'w')
        update_checker.write(title)

        video.click()
        link = driver.current_url
        driver.close()

get_youtube_video()