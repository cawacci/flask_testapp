# coding: utf-8

from flask import Flask, render_template

# インスタンスの生成
app = Flask(__name__)

# ルートパスの設定
@app.route('/')
def index():
    return render_template('index.html')

# アプリケーションの起動
if __name__ == '__main__':
    app.run()
