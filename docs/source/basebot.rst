Basebot
=======

.. toctree::
    :maxdepth: 1
    :caption: Contents
    :name: master
    :titlesonly:
    :hidden:


As of ``version 3.3``, vyper-bot comes with template bots to make getting started easier. The most basic one being :py:class:`basebot`.
It provides a very simple framework for your bot.

Simple Setup
------------

.. code:: python

    from vyper import basebot

    class MyBot(basebot.Basebot):
        def message(self, msg):
            msg = msg['message']
            if msg['text'] == '/ping':
                self.sendMessage(msg['chat']['id'], 'PONG')
    
    bot = MyBot('123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11', start_loop=True)

This is perfectly valid code, which will run the message function when a message is sent, and will reply with ``PONG``  if the message is ``/ping``.
Using this style of bot makes the setup slightly less tedious than it would be by using only the base API, as it does all the background work for you.

.. class:: basebot.Basebot(token, debug=False, start_loop=False, loop_time=0.05)

    Inherits :py:class:`vyper.API`, allowing you to use any of the API methods from within the bot.

    :members: start_message

    .. method:: start_loop(loop_time)
        
        This method will provide an easier way to create the update loop.

        :param float loop_time: The time in between cycles of the loop
    
    .. method:: set_functions(functions)

        Sets the functions that will run when an update is received. Defaults to the functions that are setup already, which are designed to be overwritten.

        :param dict functions: The dictionary of functions that will be run 
        
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
