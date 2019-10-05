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

        name = "名前"

        ret_code = ""
        df_name = request.form['df_name']

        p_sort_col1 = request.form['df_column']
        p_sort_jun1 = request.form['df_sort']

        #0:昇順/1:降順
        sort_val = "True" if p_sort_jun1 == 0 else "False"

        ret_code = "df_sort = {}.sort_values('{}', ascending={})".format(df_name,p_sort_col1,sort_val)
        
        #TEST------------------------------------------------------------
        return render_template('index.html',
                               name=name, title=title,ret_code=ret_code)
        #TEST------------------------------------------------------------
    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
