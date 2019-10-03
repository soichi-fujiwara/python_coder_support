# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect, url_for
import numpy as np


app = Flask(__name__)

# Main
def picked_up():
    messages = [
        "こんにちは、あなたの名前を入力してください",
        "やあ！お名前は何ですか？",
        "あなたの名前を教えてね"
    ]
    return np.random.choice(messages)

# Routing
@app.route('/')
def index():
    title = "ようこそ！"
    message = picked_up()
    return render_template('index.html',
                           message=message, title=title)

@app.route('/post', methods=['POST', 'GET'])
def post():
    title = "こんにちは！"
    
    if request.method == 'POST':

        ret_code = ""
        name = "名前"
        p_sort_jun1 = 0
        p_sort_jun2 = ""
        
        df_name = "df"
        p_sort_col1 = request.form['name'] + "1"
        p_sort_col2 = request.form['name'] + "2"

        #0:昇順/1:降順
        df_sort_jun1 = "True" if p_sort_jun1 == 0 else "False"
        df_sort_jun2 = "True" if p_sort_jun2 == 0 else "False"

        if p_sort_col1 != "" and p_sort_col2 != "":
          ret_code = "df_sort = {}.sort_values(['{}', '{}'], ascending=[{}, {}])".format(df_name,p_sort_col1,p_sort_col2,p_sort_jun1,p_sort_jun2)
        else:
          ret_code = "df_sort = {}.sort_values('{}', ascending={})".format(df_name,p_sort_col1,p_sort_col2)
        
        #TEST------------------------------------------------------------
        return render_template('index.html',
                               name=name, title=title,ret_code=ret_code)
        #TEST------------------------------------------------------------
    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
