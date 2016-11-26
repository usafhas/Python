from flask import Flask
from flask import render_template, redirect, url_for, request, json
import time
import system_nmap
import platform

app = Flask(__name__)

currentTime = time.ctime()
#netOs = system_nmap.netOs()
pub = system_nmap.publicIP()
priv = system_nmap.privateIP()
fping = "|".join(system_nmap.fping())
nmap = "<br>".join(system_nmap.netOs())
dist = "".join(platform.linux_distribution())
unamevar = "".join(platform.uname())
arc = "".join(platform.python_version())
node = "".join(platform.node())
processor = "".join(platform.processor())
r = "<br>"


@app.route("/")
def start():
	return "Hello World!" + '<br>' + currentTime + '<br><br>' + "Page Hosted Through CherryPy WSGI with Flask App" + "<br>"

@app.route("/system")
def system():
	return "Server Information<br><br>" + r + "Public IP Address " + pub + "<br>" + "<br> Private IP Address " + priv + r + r + "Server Architechture - " + dist + "     " + processor + "    DNS: " + node + "  -   " + unamevar + r + "Python Version - " + arc + "<br><br>Network Hosts that are up<br>" + fping + nmap

@app.route("/hello")
def hello(name=None):
   # return "Hello World!"
   return render_template('hello.html', name=name, timec=currentTime)

@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != 'admin' or request.form['password'] != 'admin':
			error = 'Invalid Credentials. Please try again.'
		else:
			return redirect(url_for('hello'))
	return render_template('login.html', error=error)


if __name__ == "__main__":
    app.run()
