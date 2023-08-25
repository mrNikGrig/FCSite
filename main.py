from flask import Flask, render_template, url_for
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
    print(description)
    return render_template('good.html', name_en=name_good, name_rus=names[name_good] ,path=path, description=description)


@app.route('/debug')
def template_debug():
    return render_template('good_template.html')


if __name__ == "__main__":
    app.run(debug=True)
    # good('cinesaddle')
