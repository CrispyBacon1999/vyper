Plugin Bots
===========

.. toctree::
    :maxdepth: 1
    :caption: Contents
    :name: master
    :titlesonly:
    :hidden:

If you want to make a bot using a plugin system, :py:class:`PluginBot` is the way to go. Rather than having to develop a system to decide which command to use, you can just create a class that extends :py:class:`Plugin` and it will be automatically detected. If you run a bot using the :py:class:`PluginBot` base, it will automatically create a folder called plugins, which will detect any file and plugin within that folder. What this means is that you won't have to import any files and it will find them for you. I've found that this saves a lot of grief trying to figure out why a command won't be detected properly, as it should be detected no matter what.

.. code:: python

    from vyper import pluginbot

    class TutorialBot(pluginbot.PluginBot):
        def message(self, msg):
            msg = msg['message']
		    self.test_plugins(msg)
    
    if __name__ == '__main__':
        bot = VyperBot('123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11', start_loop=True, list_plugins=True)

.. code:: python

    from vyper import pluginbot

    class Help(pluginbot.Plugin):
        def message(self, msg):
            if msg['text'] == '/help':
                self.bot.sendMessage(msg['chat']['id'], 'This is the help command')

.. class:: pluginbot.PluginBot(token, debug=False, start_loop=False, loop_time=.05, ping=True, list_plugins=False)

    Inherits :py:class:`pluginbot.BaseBot`, allowing you to use any of the API methods from within the bot.

    :members: start_message

    .. method:: start_loop(loop_time)
        
        This method will provide an easier way to create the update loop.

        :param float loop_time: The time in between cycles of the loop
    
    .. method:: set_functions(functions)

        Sets the functions that will run when an update is received. Defaults to the functions that are setup already, which are designed to be overwritten.

        :param dict functions: The dictionary of functions that will be run 
        

    .. method:: test_plugins(msg)

        Tests all the plugins and runs the :py:func:`message()` method in them to scan them. This is bound to be changed in a future update to automatically test for a plugin based on a custom variable, but it doesn't do that yet.
    
        :param msg: The message object that will be passed to the other end of the function. Can be a dictionary or a :py:class:`types.Message` object, depending on personal preference. Note that the :py:class:`types.Message` object must be created by calling ``msg = types.build(msg)`` and will return a dot operator seperated object.

    .. method:: _get_plugins()

        Gets a list of all the plugins that are found in the bot. You shouldn't need to run this, but it gets run when testing the plugins automatically. Returns as a generator, so the plugins can be easily iterated over.

        :return: The plugins
        :rtype: Generator

    .. method:: message(msg)

        Called when a message is received. Overwrite this in your child bot.

    .. method:: edited_message(msg)

        Called when a message is edited. Overwrite this in your child bot.

    .. method:: channel_post(msg)

        Called when a message is posted to a channel. Overwrite this in your child bot.

    .. method:: edited_channel_post(msg)

        Called when a message is edited in a channel. Overwrite this in your child bot.

    .. method:: inline_query(msg)

        Called when an inline query is received. Overwrite this in your child bot.

    .. method:: chosen_inline_result(msg)

        Called when an inline query result is is chosen. Overwrite this in your child bot.

    .. method:: callback_query(msg)

        Called when a callback is received. Overwrite this in your child bot.

    .. method:: shipping_query(msg)

        Called when a shipping query is received. Overwrite this in your child bot.

    .. method:: pre_checkout_query(msg)

        Called when a pre-checkout query is received. Overwrite this in your child bot.
