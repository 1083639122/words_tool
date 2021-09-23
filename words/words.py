from flask import Flask,render_template
import os
from config import APP_STATIC_TXT
app = Flask(__name__)

def open_words_list(words_list_name):
    with open(os.path.join(APP_STATIC_TXT, words_list_name))as f:
        words_list=f.read().split("\n")
    return words_list

@app.route('/')
def words():
    words_info_list=open_words_list('words_info.txt')

    m=0
    for i in words_info_list:
        words_info_list[m]=i.split('#')[:3]
        m+=1
    print(words_info_list)
    return render_template('words.html',words_number="words1",words_info_list=words_info_list)


if __name__ == '__main__':
    app.run()
