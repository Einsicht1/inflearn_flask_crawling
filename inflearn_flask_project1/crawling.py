#크롤링 라이브러리 import
import requests
from bs4 import BeautifulSoup
def naver_crawling():
    url = "https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EB%89%B4%EC%8A%A4"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")

    ranks_html=soup.find_all("span",{"class":"tit"})
    ranks = [i.text for i in ranks_html]

    links_html = soup.find_all("a", {"class":"bx bx_item"})
    links = [i['href'] for i in links_html]

    return ranks, links

def aladin_crawling():
    url = "https://www.aladin.co.kr/shop/common/wbest.aspx"
    req = requests.get(url)
    soup = BeautifulSoup(req.text,"html.parser")
    rank_books = soup.find_all("a", {"class":"bo3"})
    ranks = [i.text for i in rank_books]
    links = [i['href'] for i in rank_books]

    return ranks, links

def aladin_rb_crawling():
    url = "https://www.aladin.co.kr/shop/common/wbest.aspx?BestType=Bestseller&BranchType=1&CID=1237"
    req = requests.get(url)
    soup = BeautifulSoup(req.text,"html.parser")
    rank_rbooks = soup.find_all("a", {"class":"bo3"})
    rb_ranks = [i.text for i in rank_rbooks]
    links = [i['href'] for i in rank_rbooks]

    return rb_ranks, links

