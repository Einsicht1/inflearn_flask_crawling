from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
from selenium import webdriver

app = Flask(__name__)
write_wb = Workbook()
write_ws = write_wb.active



@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def result():

    if request.method == 'POST':
        keyword = request.form['input1']
        page    = request.form['input2']

        daum_list = []

        for i in range(1, int(page) + 1):
            url = "https://search.daum.net/search?nil_suggest=btn&w=news&DA=PGD&cluster=y&q=" + keyword + "&p=" +str(i)
            req = requests.get(url)
            soup = BeautifulSoup(req.text, "html.parser")
            title_html = soup.find_all("a", {"class" : "f_link_b"})
            for i in title_html:
                daum_list.append(i.text)
        for i in range(1, len(daum_list)+1):
            write_ws.cell(i,1, daum_list[i-1])
            
        write_wb.save("static/result.xlsx")
        return render_template("result.html", daum_list = daum_list)


@app.route('/naver_shopping')
def naver_shopping():
    driver = webdriver.Chrome('/Users/anna/crawling/chromedriver')
    url = "https://search.shopping.naver.com/search/all?query=%EA%B3%B5%EA%B8%B0%EC%B2%AD%EC%A0%95%EA%B8%B0"
    driver.get(url)
    driver.implicitly_wait(3)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    item_html = soup.find_all("li", {"class":"basicList_item__2XT81"})
    for i in item_html:
        print(i.find("a", {"class":"basicList_link__1MaTN"}).text)

    driver.find_element_by_css_name("subFilter_filter__3Y-uy").click()

    return render_template('shopping.html')
    



    

if __name__ == '__main__':
    app.run(debug=True)


