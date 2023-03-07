from flask import Flask, request

app_net = Flask(__name__)


@app_net.route('/api')
def api():
    contact = request.args.get('contact')
    content = request.args.get('content')
    time = request.args.get('time')

    # 在实际应用中，这里可以进行更复杂的处理，例如将信息保存到数据库中
    # 然后将保存结果添加到响应中返回给客户端
    response_text = f'联系人：{contact}\n发送内容：{content}\n发送时间：{time}'

    return response_text


if __name__ == '__main__':
    app_net.run()
