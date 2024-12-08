from flask import Flask, render_template, request
from api import API

app = Flask(__name__)

api_key = 'uAcd5AjbGMNkcrcihvy1ZS8QXSzhVUS5'

@app.route('/', methods=['GET', 'POST'])
def main_page():
    if request.method == 'POST':
        try:
            form = request.form
            start_point = form.get('startPoint', '').strip()
            end_point = form.get('endPoint', '').strip()

            if not start_point or not end_point:
                return render_template('error.html', error_message='Пожалуйста, заполните оба поля')

        except Exception as e:
            print(e)
            return render_template('error.html', error_message='Ошибка данных из формы')

        api = API(api_key=api_key)

        try:
            start_point_weather = api.weather(start_point)
            end_point_weather = api.weather(end_point)

        except IndexError:
            return render_template('error.html', error_message='Не найдена такая точка')
        except Exception as e:
            print(e)
            return render_template('error.html', error_message='Ошибка доступа к API')

        return render_template('view.html',
                               start_points=start_point_weather,
                               end_points=end_point_weather,
                               day_format={'Day': 'День', 'Night': 'Ночь'})

    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
