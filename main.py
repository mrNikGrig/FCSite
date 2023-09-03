from flask import Flask, render_template, url_for, request, redirect, make_response
import io
import json
import telebot
import threading


bot = telebot.TeleBot(open('api_for_telebot.txt', 'r').readline())
app = Flask(__name__)

names = {
    'applebox_seat': 'Эплбокс',
     'cameraID': 'Камера ID',
     'cinaesaddleCordura': 'Сисендл',
     'cinemark': 'Кинометка',
     'cinesaddle': 'Сисендл',
     'eyeBolt': 'Рым болт',
     'filters': 'Маркертабс',
     'monitorBox': 'Монитор бокс',
     'pipes': 'Чехлы для труб',
     'star': 'Сименс стар',
     'teipholder': 'Тейпхолдер'}


price = {
    'applebox_seat': 6500,
     'cameraID': 200,
     'cinaesaddleCordura': 15500,
     'cinemark': 800,
     'cinesaddle': 15000,
     'eyeBolt': 1500,
     'filters': 200,
     'monitorBox': 10000,
     'pipes': 12000,
     'star': 2100,
     'teipholder': 1500}
counter = 1
back_url = ''
message = ''
name_good = ''


def basket_add(name, quantity):
    f = open('static/dist/basket.txt', 'r')
    bask = ''
    for i in f:
        bask += i
    f.close()
    if name in bask:
        if ((name + ' - ' + quantity) in bask) == False:
            start = bask.find(name)
            end = bask.find("\n", start)
            f = open('static/dist/basket.txt', 'w')
            f.write(bask[:start])
            f.write(bask[end+1:])
            f.write(name + ' ' + quantity + ' шт\n')
        else:
            f = open('static/dist/basket.txt', 'r')
    else:
        f = open('static/dist/basket.txt', 'a')
        f.write(name + ' ' + quantity + ' шт\n')
    f.close()
    bask = ''


def message_send(message):
    bot.send_message(705989551,  message)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/good/<string:_name_good>', methods=['post', 'get'])
def good(_name_good):
    global back_url, counter, name_good
    name_good = names[_name_good]
    try:
        if _name_good != back_url[back_url.rfind('/')+1:]:
            counter = 1
    except:
        pass
    back_url = '/good/' + _name_good
    path = '../static/goods/' + _name_good + '/'
    f = io.open('static/goods/' + _name_good + '/description.txt', encoding='utf-8')
    description = ''
    description += f.read()
    f.close()
    return render_template('good.html', name_en=_name_good, name_rus=names[_name_good], path=path, description=description, counter = counter)


@app.route('/reduce_good', methods=['post', 'get'])
def reduce_good():
    global back_url
    global counter
    if counter > 0:
        counter -= 1
    return redirect(back_url)


@app.route('/increment_good', methods=['post', 'get'])
def increment_good():
    global back_url
    global counter
    counter += 1
    return redirect(back_url)


@app.route('/add_good', methods=['post', 'get'])
def add_good():
    global back_url, message, counter, name_good
    name = back_url[back_url.rfind('/')+1:] #получаю имя товара из URL
    message += name + ' ' + str(counter)
    return redirect('/add_good/getnsend_data')


@app.route('/add_good/getnsend_data')
def getnsend_data():
    global counter, message, name_good
    message = 'Поступил новый заказ\nЭто:' + name_good + ' в количестве: ' + str(counter) + " шт"+ '\n\n'
    counter = 1
    return render_template('getnsend_data.html')


@app.route('/add_good/getnsend_data/thanks', methods=['POST', 'GET'])
def thanks():
    global message
    message += 'Заказчик: ' + str(request.form['name']) + ' ' + str(request.form['phone']) + ' ' + str(request.form['address'])
    message_send(message)
    return redirect('/')


if __name__ == "__main__":
    # bot.polling()
    bot_treahed = threading.Thread(target=bot.polling)
    app.run(debug=True)
    # site_treahed = threading.Thread(target=app.run)

