from flask import Flask, request, render_template
from referat import get_referat, AVAILABLE_REFERAT_TOPICS
import random

app = Flask(__name__)


@app.route('/')
@app.route('/index.html')
def index():
    """
    TODO: при помощи get_referat получить 6 рефератов
    вывести их в шаблоне, как показано в презентации
    https://www.dropbox.com/s/dkljgo2n8z5srrg/HTTP%26HTML.pdf?dl=0 на странице 49
    В шаблоне можно использовать цикл, как показано на http://jinja.pocoo.org/
    """
    referat_list = {}

    # Get 6 unique topics
    referat_index = set()
    while len(referat_index) < 7:
        referat_index.add(random.randint(0, len(AVAILABLE_REFERAT_TOPICS) - 1))
    
    for i in referat_index:
        referat_list[AVAILABLE_REFERAT_TOPICS[i]] = get_referat(AVAILABLE_REFERAT_TOPICS[i])
        
    return render_template('index.html', referat_list=referat_list, key_list=list(referat_list.keys()))


@app.route('/buy', methods=['GET', 'POST'])
def buy():
    if request.method == 'POST':
        """
        TODO: нужно обработать данные, которые пришли от формы.
        Их можно получить как request.form.get('ИМЯ_ПОЛЯ')
        Если какое-то поле не заполнено, нужно показать шаблон с формой buy.html и
        показать в нем сообщение об ошибке "Заполните все поля!"
        Если все заполнено правильно, нужно вывести шаблон success.html
        и в нем данные, которые занес пользователь и сообщение об успехе
        """
        
        if request.form.get('first_name') == '' or request.form.get('last_name') == '' or request.form.get('email') == '' or request.form.get('topic') == '' or request.form.get('payment') == '':
            # alert и вернуть на доработку. как? 
            return render_template('buy.html')
        else:        
            data = {
                'first_name': request.form.get('first_name'),
                'last_name': request.form.get('last_name'),
                'email': request.form.get('email'),
                'topic': request.form.get('topic'),
                'payment': 'наличными' if request.form.get('payment') == 1 else 'банковской картой'
                }

            return render_template('success.html', customer = data)
    else:
        """
        TODO: нужно отобразить шаблон buy.html с формой со следюущими полями:
        first_name - Имя, поле типа text
        last_name - Фамилия, поле типа text
        email - Email, поле типа text
        topic - Тема реферата, поле типа select с вариантами выбора: 'astronomy', 'literature', 'marketing', 'mathematics', 'law', 'psychology'
        payment - Оплата, поле типа radiobutton с вариантами выбора: "Наличными" и "Банковской картой"

        """
        return render_template('buy.html')


if __name__ == "__main__":
    app.run(debug=True)
