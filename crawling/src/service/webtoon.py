import json
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from src.repository.webtoon_repository import saveWebtoonDataList, save, saveAuthor

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
    # 반응형 웹 페이지라 적용
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


def run5():
    # webtoonDataList 형태로 만들기
    webtoonDataList = [
        {
            "categoryName": "월",
            "webtoons": [
                {
                    "title": "참교육",
                    "author": "채용택 / 한가람",
                    "rating": 9.89,
                    "imgUrl": "https://~~~"
                },
                {
                    "title": "똑 닮은 딸",
                    "author": "이담",
                    "rating": 9.98,
                    "imgUrl": "https://~~~"
                }
            ]
        }
    ]

    webtoonDataList.clear()

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver.get("https://comic.naver.com/webtoon")
    driver.maximize_window()
    sleep(1)

    categoryList = driver.find_elements(
        by=By.CSS_SELECTOR,
        value='#wrap > header > div.SubNavigationBar__snb_wrap--A5gfM > nav > ul > li'
    )

    for category in categoryList[1:4]:
        # 내 자신 안에 들어 있는 a 태그
        categoryLink = category.find_element(by=By.CSS_SELECTOR, value='& > a')
        categoryLink.click()
        sleep(0.5)

        webtoonDataOfCategory = {
            "categoryName": categoryLink.text,
            "webtoons": []
        }

    # for i in range(1, 8):
    #     days = driver.find_elements(
    #         by=By.CSS_SELECTOR,
    #         value='#wrap > header > div.SubNavigationBar__snb_wrap--A5gfM > nav > ul > li > a'
    #     )
    #     day = days[i]
    #     driver.execute_script("arguments[0].scrollIntoView(true);", day)
    #
    #     daysAndWebtoons = {
    #         "day": day.text,
    #         "webtoons": []
    #     }
    #     day.click()
    #     print(daysAndWebtoons)

        liList = driver.find_elements(by=By.CSS_SELECTOR, value='#content > div:nth-child(1) > ul > li')
        for li in liList:
            driver.execute_script("arguments[0].scrollIntoView(true);", li)
            # nth-child 대신 nth-of-type 사용 권장!
            webtoonTitle = li.find_element(by=By.CSS_SELECTOR, value='& > div > a:nth-of-type(1) > span')
            titleText = webtoonTitle.text
            webtoonAuthor = li.find_element(by=By.CSS_SELECTOR, value='& > div .ContentAuthor__author--CTAAP')
            authorText = webtoonAuthor.text
            # 구조 상 *:nth-of-type(3) 대신 뒤에서 부터 찾아올 수 있음(바로 앞 요소가 div일 수도 있고, a일 수도 있음)
            # > div:nth-last-of-type(1)
            webtoonRating = li.find_element(by=By.CSS_SELECTOR, value='& > div > div:nth-last-of-type(1) > span > span')
            ratingText = float(webtoonRating.text)
            webtoonImg = li.find_element(by=By.CSS_SELECTOR, value="& > a > div > img")
            imgUrlSrc = webtoonImg.get_attribute('src')

            webtoon = {
                "title": titleText,
                "author": authorText,
                "rating": ratingText,
                "imgUrl": imgUrlSrc
            }
            webtoonDataOfCategory["webtoons"].append(webtoon)
        webtoonDataList.append(webtoonDataOfCategory)
        #     daysAndWebtoons["webtoons"].append(webtoonData)
        # webtoonDataList.append(daysAndWebtoons)
    print(webtoonDataList)

    # save(webtoonDataList)
    # saveWebtoonDataList(webtoonDataList)
    saveAuthor(webtoonDataList)
