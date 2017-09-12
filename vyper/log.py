from vyper import types

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
				print('{0} : {1} {2} : {3}'.format(chatname, first, last, text))

			if type(p) == types.InlineQuery:
				query = p.query
				f = p.frm
				first = f.first_name
				last = f.last_name if hasattr(f, 'last_name') else '\b'
				print('Inline Query : {0} {1} : {2}'.format(first, last, query))

			if type(p) == types.ChosenInlineResult:
				result = p.result_id
				f = p.frm
				first = f.first_name
				last = f.last_name if hasattr(f, 'last_name') else '\b'
				print('Inline Query Chosen : {0} {1} : {2}'.format(first, last, result))
				
			if type(p) == types.CallbackQuery:
				id = p.id
				f = p.frm
				first = f.first_name
				last = f.last_name if hasattr(f, 'last_name') else '\b'
				print('Callback : {0} {1} : {2}'.format(first, last, id))
				
			if type(p) == types.ShippingQuery:
				payload = p.invoice_payload
				f = p.frm
				first = f.first_name
				last = f.last_name if hasattr(f, 'last_name') else '\b'
				print('Shipping : {0} {1} : {2}'.format(first, last, payload))
				
			if type(p) == types.PreCheckoutQuery:
				payload = p.invoice_payload
				f = p.frm
				first = f.first_name
				last = f.last_name if hasattr(f, 'last_name') else '\b'
				print('Pre-Checkout : {0} {1} : {2}'.format(first, last, payload))
		return func(*args, **kwargs)
	return wrapper