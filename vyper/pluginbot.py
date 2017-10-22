from vyper import basebot
from vyper.web import interface
import os

class PluginBot(basebot.BaseBot):

	def __init__(self, token, debug=False, start_loop=False, loop_time=.05, ping=True, list_plugins=False, web_app=None, name=None):
		if not os.path.exists('plugins'):
			os.mkdir('plugins')
		with open('plugins/__init__.py', 'w') as ini:
			ini.write("""import pkgutil 

__path__ = pkgutil.extend_path(__path__, __name__)
for importer, modname, ispkg in pkgutil.walk_packages(path=__path__, prefix=__name__+'.'):
	__import__(modname)""")
		import plugins
		Ping.enabled = ping
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
		self.plugins = list(self._get_plugins())
		if list_plugins:
			for plugin in self.plugins:
				print(plugin)
		self.web_app = web_app
		if start_loop:
			self.start_loop(loop_time)

	def _get_plugins(self):
		for plugin in Plugin.__subclasses__():
			if plugin.enabled:
				plugin.bot = self
				yield plugin()

	def test_plugins(self, msg):
		if 'text' in msg:
			for plugin in list(self.plugins):
				plugin.message(msg)

class Plugin:
	bot = None
	enabled = True
	def __repr__(self):
		return "Plugin: {0}".format(self.__class__.__name__)

	def message(self, msg):
		pass


class Ping(Plugin):
	def message(self, msg):
		if msg['text'] == '/ping':
			self.bot.sendMessage(msg['chat']['id'], 'PONG!')

