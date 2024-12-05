from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from src.repository import tms_repository


def run():
    title = input("제목: ")
    info = tms_repository.findBoard(title)

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://koritbs.cafe24.com/student/index.php")
    driver.maximize_window()
    sleep(2)

    idInput = driver.find_element(by=By.CSS_SELECTOR, value="body > div > form > table > tbody > tr:nth-child(3) > td > input")
    idInput.send_keys("hay0ung")
    sleep(1)

    pwInput = driver.find_element(by=By.CSS_SELECTOR, value="body > div > form > table > tbody > tr.border-left-danger.border-right-danger.border-bottom-0.border-top-0.bg-brown > td > input")
    pwInput.send_keys("gkdud989898!!!!")
    sleep(1)

    loginBtn = driver.find_element(by=By.CSS_SELECTOR, value="body > div > form > table > tbody > tr.border-left-danger.border-right-danger.border-bottom-danger.border-top-0.bg-brown > td > div > div:nth-child(2) > button")
    loginBtn.click()
    # 위에 클릭 안 될 때
    # driver.execute_script("arguments[0].scrollIntoView(true)",loginBtn)
    # driver.execute_script("arguments[0].click();", loginBtn)
    sleep(3)

    classBtn = driver.find_element(by=By.CSS_SELECTOR, value="body > table > tbody > tr:nth-child(2) > td:nth-child(2) > table > tbody > tr.hover.pointer")
    classBtn.click()
    sleep(3)

    crawlingBtn = driver.find_element(by=By.CSS_SELECTOR, value="body > table > tbody > tr:nth-child(2) > td:nth-child(2) > ul > li:nth-child(10) > div")
    crawlingBtn.click()
    sleep(3)

    regiBtn = driver.find_element(by=By.CSS_SELECTOR, value="body > table > tbody > tr:nth-child(2) > td:nth-child(2) > form > table > caption > div > div:nth-child(2) > div > a")
    regiBtn.click()
    sleep(3)

    titleInput = driver.find_element(by=By.CSS_SELECTOR, value="body > table > tbody > tr:nth-child(2) > td:nth-child(2) > form > table > tbody > tr:nth-child(1) > td:nth-child(2) > input")
    titleInput.send_keys("선하영 (제목: 참교육)")
    sleep(2)

    descInput = driver.find_element(by=By.CSS_SELECTOR, value="body > table > tbody > tr:nth-child(2) > td:nth-child(2) > form > table > tbody > tr:nth-child(2) > td:nth-child(2) > div > div.ck.ck-editor__main > div > p")
    descInput.send_keys(f"\"webtoon_id\": \"{info['webtoon_id']}\"\n \"title\": \"{info['title']}\"\n \"author\": \"{info['author']}\"\n \"rating\": {info['rating']}\n \"imgUrl\": \"{info['img_url']}\"\n \"categoryName\": \"{info['category_name']}\"\n")
    sleep(3)

    postBtn = driver.find_element(by=By.CSS_SELECTOR, value="body > table > tbody > tr:nth-child(2) > td:nth-child(2) > form > table > tbody > tr.end > td > button")
    driver.execute_script("arguments[0].scrollIntoView(true)",postBtn)
    driver.execute_script("arguments[0].click();", postBtn)
    sleep(5)
