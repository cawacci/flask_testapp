# 必要なモジュールのインポート
from flask import Flask

# Instance
app = Flask(__name__)

# ルートパスの設定
@app.route('/')
def index():
    return 'Hello World!'

# アプリケーションの起動
if __name__ == '__main__':
    app.run()
