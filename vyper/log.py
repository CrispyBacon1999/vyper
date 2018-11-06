from vyper import types
from flask import Flask, render_template
from flask_socketio import SocketIO, emit, send
import threading
import requests
import json

app = Flask(__name__)
web_app = ""
def setup(bot):
	global web_app
	web_app = bot.web_app
	print(web_app)
	if web_app:
		t = threading.Thread(target=app.run)
		t.daemon = True
		t.start()

@app.route("/get-cached-log")
def cached_log():
	copy = logged_info
	global logged_info
	logged_info = []
	return json.dumps(copy)

@app.route("/")
def hello():
    return render_template('index.html', bot='Web Interface')

def log(func):
    def wrapper(*args, **kwargs):
        for p in args:
            if type(p) == dict:
                p = types.build(p)

			if type(p) == types.Message:
				if hasattr(p, 'text'):
					text = p.text
				elif hasattr(p, 'successful_payment'):
					text = 'Successful Payment - ' + p.successful_payment.currency + ' ' + str(p.successful_payment.total_amount)
					text = text[:-2] + '.' + text[-2:]
				else:
					text = 'Invalid Text'
				f = p.frm
				first = f.first_name
				last = f.last_name if hasattr(f, 'last_name') else '\b'
				chatname = p.chat.title if hasattr(p.chat, 'title') else p.chat.id
				prnt('{0} : {1} {2} : {3}'.format(chatname, first, last, text))

			if type(p) == types.InlineQuery:
				query = p.query
				f = p.frm
				first = f.first_name
				last = f.last_name if hasattr(f, 'last_name') else '\b'
				prnt('Inline Query : {0} {1} : {2}'.format(first, last, query))

			if type(p) == types.ChosenInlineResult:
				result = p.result_id
				f = p.frm
				first = f.first_name
				last = f.last_name if hasattr(f, 'last_name') else '\b'
				prnt('Inline Query Chosen : {0} {1} : {2}'.format(first, last, result))
				
			if type(p) == types.CallbackQuery:
				id = p.id
				f = p.frm
				first = f.first_name
				last = f.last_name if hasattr(f, 'last_name') else '\b'
				prnt('Callback : {0} {1} : {2}'.format(first, last, id))
				
			if type(p) == types.ShippingQuery:
				payload = p.invoice_payload
				f = p.frm
				first = f.first_name
				last = f.last_name if hasattr(f, 'last_name') else '\b'
				prnt('Shipping : {0} {1} : {2}'.format(first, last, payload))
				
			if type(p) == types.PreCheckoutQuery:
				payload = p.invoice_payload
				f = p.frm
				first = f.first_name
				last = f.last_name if hasattr(f, 'last_name') else '\b'
				prnt('Pre-Checkout : {0} {1} : {2}'.format(first, last, payload))
		return func(*args, **kwargs)
	return wrapper

logged_info = []

def prnt(msg):
	if web_app:
		global logged_info
		logged_info.append(msg)
		if len(logged_info) > 50:
			logged_info.pop(0)
	else:
		print(msg)
