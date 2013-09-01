#-*-coding:utf-8-*- 
from bottle import Bottle, run
from bottle import route, request
import sae
import urllib2
import urllib
import cookielib
import re
from urllib import urlencode

app = Bottle()

@app.route('/hello')
def hello():
    return "Hello, world! - Bottle"

@app.route('/2345checkin' , method='GET')
def checkin():
    
    cmd="login"
    forward="http://jifen.2345.com/"
    password="92141273039346a34670c6c869216646"  #抓包得来
    username="xxxxx@126.com"                     #用户名
    vTime="7776000"                              #貌似写死的
    weakpass="0"
    
    # Init
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookielib.CookieJar()))
    urllib2.install_opener(opener)
        
    # Login
    login_url = 'http://jifen.2345.com/jifenLogin.php'
    login_data = urllib.urlencode({ 'cmd':cmd,'forward':forward,'password':password,'username':username,'vTime':vTime,'weakpass':weakpass})
    login_headers = {'Referer':'http://jifen.2345.com/', 'User-Agent':' Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)'}
    login_request = urllib2.Request(login_url, login_data, login_headers)
    login_response = urllib2.urlopen(login_request).read()
    
    # Checkin
    checkin_url = 'http://jifen.2345.com/jifen/every_day_signature_new.php'
    checkin_headers = {'Referer':'http://jifen.2345.com/', 'User-Agent':' Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)'}
    checkin_request = urllib2.Request(checkin_url, None, checkin_headers)
    checkin_response = urllib2.urlopen(checkin_request).read()
    
    message="whatever its done!"
    
    if checkin_response=="error" : message="you already checked in or something just went wrong!"
       
    return message

application = sae.create_wsgi_app(app)