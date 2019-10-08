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
@app.route('/', methods=['POST', 'GET'])
def index():

  ret_code = ""
  sv_df_name = ""
  sv_column_name = ""
        
  title = "ようこそ！"
  message = picked_up()

  if request.method == 'POST':

    name = "名前"

    df_name = request.form['df_name']

    p_sort_col1 = request.form['df_column']
    p_sort_jun1 = request.form['df_sort']

    #0:昇順/1:降順
    #sort_val = p_sort_jun1
    if p_sort_jun1 == "0": 
      sort_val = "True"
    else:
      sort_val = "False"
            
    ret_code = "df_sort = {}.sort_values('{}', ascending={})".format(df_name,p_sort_col1,sort_val)
                
    return render_template('index.html',
                           message=message,
                           name=name,
                           title=title,
                           sv_df_name=df_name,
                           sv_column_name=p_sort_col1,
                           sv_sort_jun=p_sort_jun1,
                           ret_code=ret_code)
  else:
    return render_template('index.html',
                           message=message, title=title)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
