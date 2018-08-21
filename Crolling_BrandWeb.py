from bs4 import BeautifulSoup
import urllib.request
import os

#base_url: 이미지를 따올 서버의 주소
#url: 접속할 URL
def get_Topten(url):
    count = 1   #웹사이트에 있는 이미지를 크롤링 한 순서번호로 파일 저장
    html = urllib.request.urlopen(url)  #url에 접속하여
    source = html.read()    #html소스코드를 source변수에 저장
    # 불러온 HTML소스를 기반으로 하여 BeautifulSoup 객체 생성 -> 파싱
    soup = BeautifulSoup(source, "html.parser")
    for div_tag in soup.find_all('div'):    #불러온 HTML에서 모든 div태그에서
        if div_tag.has_attr('data-slick-index'):
            print("bb")
            #a태그찾기
            for a_tag in soup.find_all('a'):
                st = a_tag['style']     #style속성을 받아오고
                start_idx = st.index("url(") + len("url(")  #url 뒤부터 인덱스 받아오기
                end_idx = st.index(");")    #괄호가 닫히기 전 인덱스 받기
                print(st[start_idx:end_idx])    #url string받아오기
                img_url = "http:" + st[start_idx:end_idx]   # url 풀네임 저장
                img_name = str(count) + ".jpg"  #이미지 명은 count
                urllib.request.urlretrieve(img_url, "/home/lja97/Crolling/Topten/" + img_name)
                print("이미지 url: ", img_url)
                print("이미지 명: ", img_name)
                print("\n")
                count += 1

def get_Mixxo(url):
    count = 1
    html = urllib.request.urlopen(url)
    source = html.read()
    soup = BeautifulSoup(source, "html.parser")
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
            urllib.request.urlretrieve(img_url, "/home/lja97/Crolling/Mixxo/" + img_name)
            print("이미지 url: ", img_url)
            print("이미지 명: ", img_name)
            print("\n")
            count += 1


def get_PlasticIsland(url):
    count = 1
    html = urllib.request.urlopen(url + '/plastic')
    source = html.read()
    soup = BeautifulSoup(source, "html.parser")
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
            urllib.request.urlretrieve(img_url, "/home/lja97/Crolling/PlasticIsland/" + img_name)
            print("이미지 url: ", img_url)
            print("이미지 명: ", img_name)
            print("\n")
            count += 1


def get_LuckyChouette(url):
    count = 1
    html = urllib.request.urlopen(url)
    source = html.read()
    soup = BeautifulSoup(source, "html.parser")
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
            urllib.request.urlretrieve(img_url, "/home/lja97/Crolling/LuckyChouette/" + img_name)
            print("이미지 url: ", img_url)
            print("이미지 명: ", img_name)
            print("\n")
            count += 1

def get_Tomboy(url):
    count = 1
    html = urllib.request.urlopen(url)
    source = html.read()
    soup = BeautifulSoup(source, "html.parser")
    div = soup.find_all('div', {'class': 'gridItem'})
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
                    urllib.request.urlretrieve(img_url, "/home/lja97/Crolling/Tomboy/" + img_name)
                    print("이미지 url: ", img_url)
                    print("이미지 명: ", img_name)
                    print("\n")
                    count += 1

def get_Spao(url):
    count = 1
    html = urllib.request.urlopen(url)
    source = html.read()
    soup = BeautifulSoup(source, "html.parser")
    div = soup.find_all('div', {'class': 'bnr_sub'})
    for d_tag in div:
        for img_tag in soup.find_all('img'):
            st = img_tag['src']
            if "http" in st:
                img_url = st
            else:
                img_url = "http:" + st
            print(img_url)
            filepath, fileext = os.path.splitext(img_url)
            if fileext == '.jpg' or fileext == '.jpeg':
                img_name = str(count) + str(fileext)
            urllib.request.urlretrieve(img_url, "/home/lja97/Crolling/Spao/" + img_name)
            print("이미지 url: ", img_url)
            print("이미지 명: ", img_name)
            print("\n")
            count += 1

#CLUB CAMBRIDGE
#https://www.kolonmall.com/CLUB-CAMBRIDGE -> 데이터 개별저장
get_Topten(url = "https://www.topten10.co.kr/main/main.asp")
get_Mixxo(url = "http://mixxo.elandmall.com/main/initMain.action?chnl_no=GAW&chnl_dtl_no=1803401340&_emk_keyword=MIXXO&gclid=CjwKCAjw8O7bBRB0EiwAfbrTh68VSa9JCwk3GQWI-NjCHyojwrkavrow95BQjUkifKMPFftcWZCmzRoC59EQAvD_BwE&utm_referrer=http%3A%2F%2Fwww.elandmall.com%2Fgate%2Fgate.action%3Fchnl_no%3DGAW%26chnl_dtl_no%3D1803401340%26_emk_keyword%3DMIXXO%26gclid%3DCjwKCAjw8O7bBRB0EiwAfbrTh68VSa9JCwk3GQWI-NjCHyojwrkavrow95BQjUkifKMPFftcWZCmzRoC59EQAvD_BwE")
get_PlasticIsland(url = "https://www.theamall.com")
get_LuckyChouette(url = "https://www.kolonmall.com/LUCKYCHOUETTE")
get_Tomboy(url = "http://fashion.sivillage.com/display/brandTOMBOYMain?temp=www.tomboy.co.kr")
get_Spao(url = "http://spao.elandmall.com/main/initMain.action")


#7개 완료 남은 사이트 고가 의류브랜드