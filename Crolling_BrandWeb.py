from bs4 import BeautifulSoup
import urllib.request
import os
from selenium import webdriver
#PATH = 사진 저장 경로
#CHROME_PATH = 크롬드라이브의 경로 (.exe)
PATH = "/home/lja97/Crolling/"
CHROME_PATH = '/home/lja97/다운로드/chromedriver'

#크롬창을 따로 키지않아도 실행되게 해주는 코드
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")

#폴더가 존재하지 않으면 자동으로 만들어주는 함수
def check_dir_and_make(brand_name):
    dirname = PATH + brand_name
    if not os.path.isdir(dirname):
        os.mkdir(dirname)


def get_Topten(url, brand):
    count = 1   #웹사이트에 있는 이미지를 크롤링 한 순서번호로 파일 저장
    driver = webdriver.Chrome(CHROME_PATH, chrome_options=options)  #창을 키지않아도 해당하는 주소를 가져옴
    driver.get(url) #url을 가져온다
    html = driver.page_source   #해당 페이지의 소스를 따온다
    soup = BeautifulSoup(html) #방식은 html
    check_dir_and_make(brand)
    driver.quit()
    for a_tag in soup.find_all('a'):
        if a_tag.has_attr('style') and "background-image" in a_tag['style']:
            st = a_tag['style']     #style속성을 받아오고
            start_idx = st.index("url(") + len("url(")  #url 뒤부터 인덱스 받아오기
            end_idx = st.index(");")    #괄호가 닫히기 전 인덱스 받기
            print(st[start_idx:end_idx])    #url string받아오기
            img_url = "http:" + st[start_idx:end_idx]   # url 풀네임 저장
            img_name = str(count) + ".jpg"  #이미지 명은 count
            urllib.request.urlretrieve(img_url, PATH + brand + "/" + img_name)
            print("이미지 url: ", img_url)
            print("이미지 명: ", img_name)
            print("\n")
            count += 1

def get_Mixxo(url, brand):
    count = 1
    html = urllib.request.urlopen(url)
    source = html.read()
    soup = BeautifulSoup(source, "html.parser")
    check_dir_and_make(brand)
    for li_tag in soup.find_all("li"):
        if li_tag.has_attr('style') and "background-image" in li_tag['style'] :
            st = li_tag['style']
            start_idx = st.index("url(") + len("url(")
            end_idx = st.index(");")
            img_url = "http:" + st[start_idx + 1:end_idx - 1]
            print(img_url)
            filepath, fileext = os.path.splitext(img_url)
            if fileext != '.jpg': continue
            img_name = str(count) + ".jpg"
            urllib.request.urlretrieve(img_url, PATH + brand + "/" + img_name)
            print("이미지 url: ", img_url)
            print("이미지 명: ", img_name)
            print("\n")
            count += 1


def get_PlasticIsland(url, brand):
    count = 1
    html = urllib.request.urlopen(url + '/plastic')
    source = html.read()
    soup = BeautifulSoup(source, "html.parser")
    check_dir_and_make(brand)
    for img_tag in soup.find_all("img"):
        if not img_tag.has_attr('usemap'):
            continue
        if img_tag.has_attr('src'):
            use_map = img_tag['usemap']
            if (not "brand-top-plastic" in use_map):
                continue
            st = img_tag['src']
            if "http://" in st:
                img_url = st
            else:
                img_url = url + st
            filepath, fileext = os.path.splitext(img_url)
            if fileext == '.jpg' or fileext == '.jpeg' :
                img_name = str(count) + str(fileext)
            else : continue
            urllib.request.urlretrieve(img_url, PATH + brand + "/" + img_name)
            print("이미지 url: ", img_url)
            print("이미지 명: ", img_name)
            print("\n")
            count += 1


def get_LuckyChouette(url, brand):
    count = 1
    html = urllib.request.urlopen(url)
    source = html.read()
    soup = BeautifulSoup(source, "html.parser")
    check_dir_and_make(brand)
    div = soup.find_all('div', {'class': 'fix-ratio-106 bg-image'})
    for d_tag in div:
        if d_tag.has_attr('style'):
            st = d_tag['style']
            start_idx = st.index("url(") + len("url(")
            end_idx = st.index(")")
            img_url = st[start_idx + 1:end_idx - 1]
            print(img_url)
            filepath, fileext = os.path.splitext(img_url)
            if fileext == '.jpg' or fileext == '.jpeg':
                img_name = str(count) + str(fileext)
            else : continue
            urllib.request.urlretrieve(img_url, PATH + brand + "/" + img_name)
            print("이미지 url: ", img_url)
            print("이미지 명: ", img_name)
            print("\n")
            count += 1

def get_Tomboy(url, brand):
    count = 1
    html = urllib.request.urlopen(url)
    source = html.read()
    soup = BeautifulSoup(source, "html.parser")
    div = soup.find_all('div', {'class': 'gridItem'})
    check_dir_and_make(brand)
    for d_tag in div:
        for img_tag in soup.find_all('img'):
            if img_tag.has_attr('src') and "http://" in img_tag['src']:
                st = img_tag['src']
                start_idx = st.index("http://") + len("http://")
                end_idx = len(st)
                img_url = "http://" + urllib.parse.quote(st[start_idx:end_idx])
                print(img_url)
                filepath, fileext = os.path.splitext(img_url)
                if fileext == '.jpg' or fileext == '.jpeg':
                    img_name = str(count) + str(fileext)
                    urllib.request.urlretrieve(img_url, PATH + brand + "/" + img_name)
                    print("이미지 url: ", img_url)
                    print("이미지 명: ", img_name)
                    print("\n")
                    count += 1

def get_Spao(url, brand):
    count = 1
    driver = webdriver.Chrome(CHROME_PATH, chrome_options=options)
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html)
    check_dir_and_make(brand)
    driver.quit()

    div = soup.find_all('div', {'class': 'box_promotion_bnr '})
    for d_tag in div:
        for li_tag in soup.find_all('li'):
            if li_tag.has_attr('style') and "background-image" in li_tag['style']:
                st = li_tag['style']
                start_idx = st.index("url(") + len("url(")  # url 뒤부터 인덱스 받아오기
                end_idx = st.index(");")  # 괄호가 닫히기 전 인덱스 받기
                if "http" in st:
                    img_url = st[start_idx+1:end_idx-1]
                else:
                    img_url = "http:" + st[start_idx+1:end_idx-1]
                print(img_url)
                filepath, fileext = os.path.splitext(img_url)
                if fileext == '.jpg' or fileext == '.jpeg':
                    img_name = str(count) + str(fileext)
                    urllib.request.urlretrieve(img_url, PATH + brand + "/" + img_name)
                    print("이미지 url: ", img_url)
                    print("이미지 명: ", img_name)
                    print("\n")
                    count += 1

def get_8seconds(url, brand):
    count = 1
    driver = webdriver.Chrome(CHROME_PATH, chrome_options=options)
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html)
    check_dir_and_make(brand)
    driver.quit()

    div = soup.find_all('div', {'class': 'lSSlideOuter '})
    for d in div:
        print("AA")
        for img_tag in soup.find_all('img'):
            if img_tag.has_attr('src') and "http://" in img_tag['src']:
                st = img_tag['src']
                start_idx = st.index("http://") + len("http://")
                end_idx = len(st)
                img_url = "http://" + urllib.parse.quote(st[start_idx:end_idx])
                print(img_url)
                filepath, fileext = os.path.splitext(img_url)
                if fileext == '.jpg' or fileext == '.jpeg':
                    img_name = str(count) + str(fileext)
                    urllib.request.urlretrieve(img_url, PATH + brand + "/" + img_name)
                    print("이미지 url: ", img_url)
                    print("이미지 명: ", img_name)
                    print("\n")
                    count += 1

def get_ALAND(url, brand):
    count = 1
    driver = webdriver.Chrome(CHROME_PATH, chrome_options=options)
    driver.implicitly_wait(3)
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html)
    check_dir_and_make(brand)
    driver.quit()

    div = soup.find_all('div', {'class':'wrap-index-mpromotion main-banner'})
    for img_tag in soup.find_all('img'):
        st = img_tag['src']
        if "http" in st:
            img_url = st
        else:
            img_url = url + st
        print(img_url)
        filepath, fileext = os.path.splitext(img_url)
        if fileext == 'jpg' or fileext == '.jpeg' or fileext == '.png':
            img_name = str(count) + str(fileext)
            urllib.request.urlretrieve(img_url, PATH + brand + "/" + img_name)
            print("이미지 url: ", img_url)
            print("이미지 명: ", img_name)
            print("\n")
            count += 1


#CLUB CAMBRIDGE
#따로 폴더 만들기!
#https://www.kolonmall.com/CLUB-CAMBRIDGE -> 데이터 개별저장
get_Topten(url = "https://www.topten10.co.kr/main/main.asp", brand = "Topten")
get_Mixxo(url = "http://mixxo.elandmall.com/main/initMain.action?chnl_no=GAW&chnl_dtl_no=1803401340&_emk_keyword=MIXXO&gclid=CjwKCAjw8O7bBRB0EiwAfbrTh68VSa9JCwk3GQWI-NjCHyojwrkavrow95BQjUkifKMPFftcWZCmzRoC59EQAvD_BwE&utm_referrer=http%3A%2F%2Fwww.elandmall.com%2Fgate%2Fgate.action%3Fchnl_no%3DGAW%26chnl_dtl_no%3D1803401340%26_emk_keyword%3DMIXXO%26gclid%3DCjwKCAjw8O7bBRB0EiwAfbrTh68VSa9JCwk3GQWI-NjCHyojwrkavrow95BQjUkifKMPFftcWZCmzRoC59EQAvD_BwE", brand = "Mixxo")
get_PlasticIsland(url = "https://www.theamall.com", brand = "PlasticIsland")
get_LuckyChouette(url = "https://www.kolonmall.com/LUCKYCHOUETTE", brand = "LuckyChouette")
get_Tomboy(url = "http://fashion.sivillage.com/display/brandTOMBOYMain?temp=www.tomboy.co.kr", brand = "Tomboy")
get_Spao(url = "http://spao.elandmall.com/main/initMain.action", brand = "Spao")
get_8seconds(url = "http://www.ssfshop.com/8Seconds/main?dspCtgryNo=&brandShopNo=BDMA07A01&brndShopId=8SBSS&leftBrandNM=", brand = "8seconds")
get_ALAND(url = "http://www.a-land.co.kr", brand = "ALAND")