from flask import Flask, render_template


app = Flask(__name__)


@app.route('/<name>')
def homepage(name):
    return render_template('homepage.html', name=name)


@app.route('/looping/<int:number>')
def looping(number):
    return render_template('looping.html', number=number)


@app.route('/numbers/<int:number>')
def numbers(number):
    return render_template('numbers_page.html', number=number)


if __name__ == '__main__':
    app.debug = True
    app.run()