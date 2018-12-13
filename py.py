from flask import Flask, render_template
from flask_bootstrap import Bootstrap

# 引入必要的模块
app = Flask(__name__)
bootstrap=Bootstrap(app)
# 定义一个函数，它将响应并返回一个html描述的页面，这里我们是：sketch.html
@app.route('/')

def hello():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
