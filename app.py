from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def calc():
    num1 = request.form['num1']
    num2 = request.form['num2']
    op = request.form['operation']


    if op=="+":
        result=int(num1)+int(num2)

    elif op=="-":
        result=int(num1)-int(num2)

    elif op=="*":
        result=int(num1)*int(num2)

    elif op=="/":
        result=int(num1)/int(num2)

    return  render_template('index.html', num1= num1, num2=num2, result=result)


if __name__ == '__main__':
    app.run(debug=True)