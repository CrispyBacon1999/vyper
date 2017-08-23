import basebot

class PluginBot(basebot.BaseBot):

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
		self.plugins = self._get_plugins()
		if start_loop:
			self.start_loop(loop_time)

	def _get_plugins(self):
		for plugin in Plugin.__subclasses__():
			plugin.bot = self
			yield plugin()

	def test_plugins(self, msg):
		for plugin in self.plugins:
			plugin.execute(msg)

class Plugin:
	bot = None
	def __repr__(self):
		return "Vyper Plugin: {0}".format(self.__class__.__name__)

	def execute(self, msg):
		pass

class Ping(Plugin):
	def execute(self, msg):
		if msg['text'] == '/ping':
			self.bot.sendMessage(msg['chat']['id'], 'PONG!')

