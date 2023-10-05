import flask
from flask import Flask, request, render_template

from althgram import Decry
from althgram import Encry

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/S_DES', methods=['GET','POST'])
def S_DES():
    message = ""
    plaintext = request.args.get('plaintext')
    print(plaintext)
    key = request.args.get('key')
    print(key)
    ciphertext = request.args.get('ciphertext')
    print(ciphertext)
    if key != '':
        if plaintext is not '' and ciphertext is '':
            get_ciphertext = Encry(plaintext, key)
            print(get_ciphertext)
            message = "完成明文加码！密文为:" + get_ciphertext
            return render_template('index.html', message=message)
        elif ciphertext is not '' and plaintext is '':
            get_plaintext = Decry(ciphertext, key)
            message = "完成密文解码！明文为:" + get_plaintext
            return render_template('index.html', message=message)
        elif plaintext is '' and ciphertext is '':
            message = "必须输入明文或密文！"
            return render_template('index.html', message=message)
    if key is '':
        message = "密钥不能为空！"
        return render_template('index.html', message=message)
    print(message)


if __name__ == '__main__':
    app.run()
    print('run')
