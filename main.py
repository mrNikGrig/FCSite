from flask import Flask, render_template, url_for, request
import io

app = Flask(__name__)

names = {'applebox_seat': 'Эплбокс',
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

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/good/<string:name_good>')
def good(name_good):
    path = '../static/goods/' + name_good + '/'
    f = io.open('static/goods/' + name_good + '/description.txt', encoding='utf-8')
    description = ''
    description += f.read()
    f.close()
    return render_template('good.html', name_en=name_good, name_rus=names[name_good], path=path, description=description)


@app.route('/debug')
def template_debug():
    return render_template('good_template.html')


@app.route('/quantity')
def add_good():
    name = request.form['name']
    quantity = request.form['quantityVar']
    basket_add(str(name), str(quantity))
    return 'success'


if __name__ == "__main__":
    app.run(debug=True)
    # good('cinesaddle')
