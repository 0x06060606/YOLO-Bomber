import json, requests, socket, urllib3, os, random
from flask import Flask, request, jsonify, render_template, Markup, send_from_directory
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps, loads, dumps
from re import search
from os import name, system
from sys import argv
from threading import Thread
from random import seed, random, randint
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.proxy import Proxy, ProxyType
from time import sleep
app = Flask(__name__, template_folder='./html')
api = Api(app)
def banner(a, b):
    system('cls' if name=='nt' else 'clear')
    # print("""
    # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    # XXXXXXXXXXXXXXXXKKXXXXXXXXXXKXXXXXXXXXXXKKKKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXKKKKXXXXXXXXXXXXXXXXXXXXX
    # XXXXXXXXXXXXXKx:;;;ckXXXXkc;;;ckXXXKOoc;,'',;cdOXXXXXOl;;;:xXXXXXXXXXXKOdc;,'',;cdOKXXXXXXXXXXXXXXXX
    # XXXXXXXXXXXXXXO;    ,kXXk,   .:0XKk:.          .:kXXXk'   .lKXXXXXXXXk:.          .:kXXXXXXXXXXXXXXX
    # XXXXXXXXXXXXXXXO;    ;OO:    :OXKx'    .:ol:.    'ckXk'   .lKXXXXXXXx'    .:ll:.    'xXXXXXXXXXXXXXX
    # XXXXXXXXXXXXXXXXO;   .,,.  .:0XXO;    ,kXXXXk'     :0k'   .lKXXXXXXO;    'xXXXXk'    ;OXXXXXXXXXXXXX
    # XXXXXXXXX====================================================================================XXXXXXX
    # XXXXXXXXXXXXXXXXXXO;     .:OXXXXk'    cKXXXXK:     'kx'   .lKXXXXXXk'    :0XXXX0c    .xXXXXXXXXXXXXX
    # XXXXXXXXXXXXXXXXXXXk'    ,OXXXXX0:    .oKXX0o.    .cKk'   .l0XKKKXX0c    .o0XX0o.    :0XXXXXXXXXXXXX
    # XXXXXXXXXXXXXXXXXXXO;    :0XXXXXXO;     ';;.    .:xOXk'    .',,,,;dKO:.    .;;'    .;OXXXXXXXXXXXXXX
    # XXXXXXXXXXXXXXXXXXXO;    :0XXXXXXX0d,.        .;dKXXXk'          .lKX0d;.        .;d0XXXXXXXXXXXXXXX
    # XXXXXXXXXXXXXXXXXXXKkdoodkKXXXXXXXXXKOdolccloxOKXXXXX0xoooooooooodOXXXXKOxolccloxOKXXXXXXXXXXXXXXXXX
    # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX""")
    if(b=='flooder'):
        print("""     [!] Flooding...   """+str(a))
    elif(b=='loader'):
        print("""     [!] Loading...    """)
def proxFox(a):
	capabilities = webdriver.DesiredCapabilities().FIREFOX
	capabilities["marionette"] = False
	optFox = Options()
	optFox.headless = a
	proFox = webdriver.FirefoxProfile()
	proFox.set_preference("general.useragent.override", "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1")
	proFox.update_preferences()
	binary = FirefoxBinary(r'/usr/bin/firefox')
        return webdriver.Firefox(capabilities=capabilities, firefox_binary=binary, options=optFox, firefox_profile=proFox)
def engine(a, b, c, d):
    try:
        if(d==True):
            banner(0, 'loader')
            driver = proxFox(False)
        else:
            driver = proxFox(True)
        yoloMessage=(a)
        yolo=(b)
        driver.get("https://onyolo.com/m/"+str(yolo))
        #driver.execute_script('var iframe = document.createElement(\'iframe\');iframe.style.display = "none";iframe.src = "about:blank";document.body.appendChild(iframe);')
        count=(0)
        while(int(count)<int(c)):
            if(d==True):
                banner(count, 'flooder')
            sleep(0.25)
            message = driver.find_element_by_xpath("/html/body/div[4]/form/textarea")
            message.send_keys(str(randint(int(random()), 999999))+str("  |   ")+str(yoloMessage)+str("   |  ")+str(randint(int(random()), 999999)))
            driver.find_element_by_xpath("/html/body/div[4]/form/div[1]").click()
            driver.refresh()
            count+=(1)
        driver.close()
        system('taskkill /IM "firefox.exe" /F' if name=='nt' else 'pkill "geckodriver"')
        return("{'msg': 'done'}")
    except Exception as uwu:
        if("list index out of range" in str(uwu)):
            print("     [!] "+argv[0]+" <message> <user_id>         ")
            system('taskkill /IM "firefox.exe" /F' if name=='nt' else 'pkill "geckodriver"')
            return("{'error': 'arg'}")
        if("Reached error page" in str(uwu)):
            print("     [!] Server did not connect!                 ")
            driver.close()
            system('taskkill /IM "firefox.exe" /F' if name=='nt' else 'pkill "geckodriver"')
            return("{'error': 'server'}")
        if("TypeError" in str(uwu)):
            print("     [!] Browser did not cleanup correctly!      ")
            driver.close()
            system('taskkill /IM "firefox.exe" /F' if name=='nt' else 'pkill "geckodriver"')
            return("{'error': 'cleanup'}")
        if("Traceback" in str(uwu)):
            print("     [!] Bye-Bye!                                ")
            driver.close()
            system('taskkill /IM "firefox.exe" /F' if name=='nt' else 'pkill "geckodriver"')
            return("{'error': 'exit'}")
        print("     [!] OwO we made a oopsie whoopsie :(    ")
        print("     [?] "+str(uwu))
        driver.close()
        system('taskkill /IM "firefox.exe" /F' if name=='nt' else 'pkill "geckodriver"')
        return("{'error': 'unknown', 'msg': '"+str(uwu)+"'}")
@app.route('/bomb')
def run(labelname=None):
    goKill=(0)
    error=("{'need': '")
    if(request.args.get('msg')==None or request.args.get('msg')==''):
        goKill=(1)
        error+=('msg ')
    else:
        msg=(str(request.args.get('msg')))
    if(request.args.get('user')==None or request.args.get('user')==''):
        goKill=(1)
        error+=('user ')
    else:
        user=(str(request.args.get('user')))
    if(request.args.get('count')==None or request.args.get('count')==''):
        goKill=(1)
        error+=('count ')
    else:
        count=(str(request.args.get('count')))
    error+=("'}")
    if(goKill==0):
        return (engine(msg, user, count, False))
    else:
        return (error)
@app.route('/')
def index():
    return render_template('home.html')
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
class null(Resource):
    def get(self):
        return ('bruh')
api.add_resource(null, '/favicon.ico')
if __name__ == '__main__':
     app.run(host='0.0.0.0')
