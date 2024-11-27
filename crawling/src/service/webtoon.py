import json
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def run():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver.get("https://comic.naver.com/webtoon")
    sleep(1)

    days = driver.find_elements(
        by=By.CSS_SELECTOR,
        value='#wrap > header > div.SubNavigationBar__snb_wrap--A5gfM > nav > ul > li > a'
    )
    for day in days[1:8]:
        # 자바 스크립트 코드 사용
        # 반복문 안에서 스크롤 할 때마다 사용해야됨 (
        driver.execute_script("arguments[0].scrollIntoView(true);", day)
        day.click()

        print(day.text)

        # 같은 구조를 가지고 있는 것들은 한꺼번에 반복을 돌릴 수 있음
        # 반드시 요소가 같은 지 확인
        webtoonTitles = driver.find_elements(by=By.CSS_SELECTOR, value='#content > div:nth-child(1) > ul > li > div > a > span')
        for webtoonTitle in webtoonTitles:
            print(webtoonTitle.text)

def run2():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://comic.naver.com/webtoon")
    sleep(1)

    days2 = driver.find_elements(
        by=By.CSS_SELECTOR,
        value='#wrap > header > div.SubNavigationBar__snb_wrap--A5gfM > nav > ul > li > a'
    )
    for day2 in days2[1:8]:
        driver.execute_script("arguments[0].scrollIntoView(true);", day2)
        day2.click()

        webtoonTitle2 = driver.find_elements(by=By.CSS_SELECTOR, value='#container > div.ListSpot__spot_wrap--Iko15 > div.content > div > ul > li > div > a > span')
        for webtoonTitle2 in webtoonTitle2:
            print(webtoonTitle2.text)

# SSR 방식으로 된 사이트 크롤링
def run3():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://kr.stussy.com/collections/new-arrivals")
    # 반응형 웹페이지라 적용
    driver.maximize_window()
    sleep(1)

    categories = driver.find_elements(
        by=By.CSS_SELECTOR,
        value='#dropdown-menu-1-shop > div > ul > li > a'
    )

    for i in range(len(categories)):
        categories = driver.find_elements(
            by=By.CSS_SELECTOR,
            value='#dropdown-menu-1-shop > div > ul > li > a'
        )
        categoryName = categories[i].text
        print(categoryName)

        driver.execute_script("arguments[0].scrollIntoView(true);", categories[i])
        driver.execute_script("arguments[0].click();", categories[i])
        sleep(1)

        products = driver.find_elements(
            by=By.CSS_SELECTOR,
            value='#shopify-section-template--14469189140535__product-grid > s-collection-grid > div.collection-grid__layout.px-sm.pt-md.pb-xl.tabletp\:px-md > ul > li'
        )

        for product in products[0:4]:
            img = product.find_element('div > a > div > img')
            name = product.find_element(by=By.CSS_SELECTOR, value='div > div > div:nth-child(1) > a')
            price = product.find_element(by=By.CSS_SELECTOR, value='div > div > div:nth-child(2) > span')
            print(f"상품 사진: {img.get_attribute('src')}, 상품명: {name.text}, 상품 가격: {price.text}")


def run4():
    productList = []

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://kr.stussy.com/collections/new-arrivals")
    # 반응형 웹페이지라 적용
    driver.maximize_window()
    sleep(1)

    categories = driver.find_elements(
        by=By.CSS_SELECTOR,
        value='#dropdown-menu-1-shop > div > ul > li > a'
    )

    for i in range(len(categories)):
        categories = driver.find_elements(
            by=By.CSS_SELECTOR,
            value='#dropdown-menu-1-shop > div > ul > li > a'
        )

        categoryName = categories[i].text
        print(categoryName)
        categoryDict = {
            "categoryName": categoryName,
            "productList": []
        }

        driver.execute_script("arguments[0].scrollIntoView(true);", categories[i])
        driver.execute_script("arguments[0].click();", categories[i])
        sleep(0.1)

        products = driver.find_elements(
            by=By.CSS_SELECTOR,
            value='#shopify-section-template--14469189140535__product-grid > s-collection-grid > div.collection-grid__layout.px-sm.pt-md.pb-xl.tabletp\:px-md > ul > li'
        )
        print(products)
        for product in products[0:4]:
            print(product)
            img = product.find_element(by=By.CSS_SELECTOR, value='div > a > div > img')
            imgSrc = img.get_attribute('src')
            name = product.find_element(by=
            By.CSS_SELECTOR, value='div > div > div:nth-child(1) > a')
            nameText = name.text
            price = product.find_element(by=By.CSS_SELECTOR, value='div > div > div:nth-child(2) > span')
            priceText = price.text

            print(f"상품 사진: {imgSrc}, 상품명: {nameText}, 상품 가격: {priceText}")
            categoryDict['productList'].append({
                "name": nameText,
                "price": priceText,
                "img": imgSrc
            })

        productList.append(categoryDict)
    with open("products.json", "w", encoding="utf-8") as f:
        json.dump(productList, f, ensure_ascii=False, indent=4)