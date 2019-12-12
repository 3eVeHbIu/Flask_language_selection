from flask import Flask, render_template, request
app = Flask(__name__)


'''
    1. Простота в освоении  - is_simple
    2. Серверный язык - is_server
    3. Поддерживает ООП - is_objective
    4. Подходит для разработки игр is_gaming
    5. Компилируемый is_compiled
    6. Подходит для разробоки под телефоны is_mobile
    7. Многопоточный is_multithread
'''


@app.route('/')
def hello_world():
    return render_template('index.html', title='Форма')


@app.route('/answer', methods=['POST'])
def show_answer():
    try:
        simple = request.form['is_simple']
    except KeyError:
        simple = 'Не простой'
    try:
        server = request.form['is_server']
    except KeyError:
        server = 'Не серверный'
    try:
        an_object = request.form['is_objective']
    except KeyError:
        an_object = 'Не поддерживает ООП'
    try:
        game = request.form['is_gaming']
    except KeyError:
        game = 'Не пригоден для игр'
    try:
        compiled = request.form['is_compiled']
    except KeyError:
        compiled = 'Не компилируемый'
    try:
        mobile = request.form['is_mobile']
    except KeyError:
        mobile = 'Не подходит для мобильных'
    try:
        multithread = request.form['is_multithread']
    except KeyError:
        multithread = 'Не поддерживает многопоточность'

    user = {simple, server, an_object, game, compiled, mobile, multithread}

    swift = ('swift',  {'Простой',
                        'Не серверный',
                        'Не поддерживает ООП',
                        'Пригоден для игр',
                        'Компилируемый',
                        'Подходит для мобильных',
                        'Поддерживает многопоточность'})

    go = ('GO', {'Простой',
                 'Серверный',
                 'Не поддерживает ООП',
                 'Пригоден для игр',
                 'Компилируемый',
                 'Не подходит для мобильных',
                 'Поддерживает многопоточность'})

    php = ('PHP', {'Простой',
                   'Серверный',
                   'Не поддерживает ООП',
                   'Не пригоден для игр',
                   'Не компилируемый',
                   'Не подходит для мобильных',
                   'Не поддерживает многопоточность'})

    cpp = ('C++', {'Не простой',
                   'Не серверный',
                   'Поддерживает ООП',
                   'Пригоден для игр',
                   'Компилируемый',
                   'Не подходит для мобильных',
                   'Поддерживает многопоточность'})

    python = ('python', {'Простой',
                         'Серверный',
                         'Поддерживает ООП',
                         'Пригоден для игр',
                         'Не компилируемый',
                         'Подходит для мобильных',
                         'Поддерживает многопоточность'})

    javascript = ('javascript', {'Простой',
                                 'Cерверный',
                                 'Поддерживает ООП',
                                 'Пригоден для игр',
                                 'Не компилируемый',
                                 'Подходит для мобильных',
                                 'Не поддерживает многопоточность'})

    java = ('java', {'Не простой',
                     'Серверный',
                     'Поддерживает ООП',
                     'Пригоден для игр',
                     'Не компилируемый',
                     'Подходит для мобильных',
                     'Поддерживает многопоточность'})

    cs = ('C#', {'Не простой',
                 'Серверный',
                 'Поддерживает ООП',
                 'Пригоден для игр',
                 'Не компилируемый',
                 'Подходит для мобильных',
                 'Поддерживает многопоточность'})

    kotlin = ('kotlin', {'Простой',
                         'Не серверный',
                         'Поддерживает ООП',
                         'Пригоден для игр',
                         'Не компилируемый',
                         'Подходит для мобильных',
                         'Поддерживает многопоточность'})

    rust = ('rust', {'Не простой',
                     'Не серверный',
                     'Не поддерживает ООП',
                     'Пригоден для игр',
                     'Компилируемый',
                     'Не подходит для мобильных',
                     'Поддерживает многопоточность'})

    languages = (swift, go, php, cpp, python,
                 javascript, java, cs, kotlin, rust)

    answers = []
    for language in languages:
        if len(language[1].difference(user)) < 2:
            answers.append((language[0], language[1].difference(user)))

    return render_template('answer.html', answers=answers)


if __name__ == '__main__':
    app.run(debug=True)
