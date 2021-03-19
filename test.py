from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

# 크롬 드라이버로 크롬 실행
driver = webdriver.Chrome('./chromedriver')
# zum 검색페이지 이동
driver.get('https://search.zum.com/search.zum?method=uni&option=accu&qm=f_typing&rd=1&query=%EB%8D%94%EB%AF%B8')

print("+" * 100)
print("실시간 이슈 크롤링 _ 출처 : ZUM")
print("-" * 100)

# 기준 시간 크롤링
time = driver.find_element_by_xpath('//*[@id="issue_time"]').text

# 실시간 이슈 크롤링

# 우선 이슈키워드들을 리스트에 담고
issueKeywordLs = []
for i in list(range(1, 11)):
    selector = '//*[@id="issue_wrap"]/ol/li[{}]/div/div[2]/a/span[2]'.format(i)
    issueKeyword = driver.find_element_by_xpath(selector)
    issueKeywordLs.append(issueKeyword)

#print(issueKeywordLs)

# 텍스트만 추출하여 다시 리스트에 담아둠
issueKeywordTextLs = []
for keyword in issueKeywordLs:
    issueKeywordTextLs.append(keyword.text)

# 현재시간과 검색어 순위와 함께 검색어 텍스트 출력함
print('현재시간 : {}'.format(time))
for i in list(range(1, 11)):
    if issueKeywordTextLs[i - 1] != '':
        print('{}. {}'.format(i, issueKeywordTextLs[i-1]))

# 드라이버 종료함
driver.quit()

#현재시간
