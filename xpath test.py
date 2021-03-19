

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

# 크롬 드라이버로 크롬 실행
driver = webdriver.Chrome('./chromedriver')
# zum 검색페이지 이동
driver.get('https://search.zum.com/search.zum?method=uni&option=accu&qm=f_typing&rd=1&query=%EB%8D%94%EB%AF%B8')

issueKeywordLs = []
for i in list(range(1, 11)):
    selector = '//*[@id="issue_wrap"]/ol/li[{}]/div/div[2]/a/span[2]'.format(i)
    issueKeyword = driver.find_element_by_xpath(selector)
    issueKeywordLs.append(issueKeyword)

print(issueKeywordLs)
for keyword in issueKeywordLs:
    issueKeywordText = keyword.text
    if issueKeywordText != '':
        print("실시간 이슈 키워드" + issueKeywordText)



