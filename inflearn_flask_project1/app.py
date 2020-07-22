from flask import Flask, render_template
import crawling

app = Flask(__name__)

@app.route('/')
def hello():

    list_naver, naver_href         = crawling.naver_crawling()
    list_aladin, aladin_href       = crawling.aladin_crawling()
    list_aladin_rb, rb_aladin_href = crawling.aladin_rb_crawling()
    return render_template("index.html",
                           naver     = list_naver,
                           aladin    = list_aladin,
                           aladin_rb = list_aladin_rb,
                           n_href    = naver_href,
                           a_href    = aladin_href,
                           rba_href  = rb_aladin_href,
                           len_naver = len(list_naver),
                           len_aladin = len(list_aladin),
                           len_aladin_rb = len(list_aladin_rb)
                          )

@app.route('/about')
def about():
    return "여기는 어바웃입니다"


if __name__ == '__main__':
    app.run(debug=True)
