from vyper import vyper
import time

class BaseBot(vyper.API):

	start_message = 'Starting bot. Break the loop by using Ctrl-C on Windows, or Command+C on Mac.'

	def __init__(self, token, debug=False, start_loop=False, loop_time=.05):
		self.functions = {
			'message': self.message, 
			'edited_message': self.edited_message,
			'channel_post': self.channel_post,
			'edited_channel_post': self.edited_channel_post,
			'inline_query': self.inline_query,
			'chosen_inline_result': self.chosen_inline_result,
			'callback_query': self.callback_query,
			'shipping_query': self.shipping_query,
			'pre_checkout_query': self.pre_checkout_query
		}
		self.configure(token, functions=self.functions, debug=debug)
		if start_loop:
			self.start_loop(loop_time)

	def start_loop(self, loop_time):
		print(self.start_message)
		while True:
			self.getUpdates()
			time.sleep(loop_time)

	def set_functions(self, functions):
		self.functions = functions

	def message(self, msg):
		print('Create a message(self, msg) method in order to handle this update!')

	def edited_message(self, msg):
		print('Create an edited_message(self, msg) method in order to handle this update!')

	def channel_post(self, msg):
		print('Create a channel_post(self, msg) method in order to handle this update!')

	def edited_channel_post(self, msg):
		print('Create an edited_channel_post(self, msg) method in order to handle this update!')

	def inline_query(self, msg):
		print('Create an inline_query(self, msg) method in order to handle this update!')

	def chosen_inline_result(self, msg):
		print('Create a chosen_inline_result(self, msg) method in order to handle this update!')

	def callback_query(self, msg):
		print('Create a callback_query(self, msg) method in order to handle this update!')

	def shipping_query(self, msg):
		print('Create a shipping_query(self, msg) method in order to handle this update!')

	def pre_checkout_query(self, msg):
		print('Create a pre_checkout_query(self, msg) method in order to handle this update!')