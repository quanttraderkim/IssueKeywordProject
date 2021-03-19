from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')
driver.get('https://auto.naver.com/bike/mainList.nhn')

print("+" * 100)
print(driver.title)
print(driver.current_url)
print("바이크 브랜드 크롤링")
print("-" * 100)

# 바이크 제조사 전체 페이지 버튼 클릭
bikeCompanyAllBtn = driver.find_element_by_css_selector("#container > div.spot_main > div.spot_aside > div.tit > a")
bikeCompanyAllBtn.click()

time.sleep(3)

# 바이크 제조사 1번 페이지 진입해서 바이크 리스트 추출
allBikeCompanyElement = driver.find_elements_by_css_selector(
    "#_vendor_select_layer > div > div.maker_group div.emblem_area > ul > li")

# 바이크 첫 페이지 크롤링
for item in allBikeCompanyElement:
    bikeComName = item.find_element_by_tag_name("span").text
    if (bikeComName != ''):
        print("바이크 회사명:" + bikeComName)
        ahref = item.find_element_by_tag_name("a").get_attribute("href")
        print('네이버 자동차 바이크제조사 홈 sub url:', ahref)
        imgUrl = item.find_element_by_tag_name("img").get_attribute("src")
        print('바이크 회사 엠블럼:', imgUrl)

time.sleep(3)

# 바이크 제조사 리스트의 다음 페이지 버튼을 찾아서 클릭하자.
nextBtn = driver.find_element_by_css_selector(
    "#_vendor_select_layer > div > div.maker_group > div.rolling_btn > button.next")
# 다음 바이크 제조사 페이지 버튼이 활성화 여부
isExistNextPage = nextBtn.is_enabled()

if (isExistNextPage == True):
    print("다음 페이지 존재함=======================================>")
    nextBtn.click()
    allBikeCompanyElement = driver.find_elements_by_css_selector(
        "#_vendor_select_layer > div > div.maker_group div.emblem_area > ul > li")
    for item in allBikeCompanyElement:
        bikeComName = item.find_element_by_tag_name("span").text
        if (bikeComName != ''):
            print("바이크 회사명:" + bikeComName)
            ahref = item.find_element_by_tag_name("a").get_attribute("href")
            print('네이버 자동차 바이크제조사 홈 sub url:', ahref)
            imgUrl = item.find_element_by_tag_name("img").get_attribute("src")
            print('바이크 회사 엠블럼:', imgUrl)

# 크롤링이 끝나면 webdriver 브라우저를 종료한다.
# driver.quit()