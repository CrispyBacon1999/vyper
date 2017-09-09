.. Vyper-Bot documentation master file, created by
   sphinx-quickstart on Tue Aug 15 16:26:24 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Vyper-Bot's documentation!
=====================================

.. toctree::
    :maxdepth: 0
    :caption: Contents
    :name: master
    :titlesonly:
    :hidden:

    API <api>
    BaseBot <basebot>
    PluginBot <pluginbot>
    Payments <pay>


Installation
------------

To install using pip, simply run

``pip3 install vyper-bot``

in a terminal. If you already have it installed but want to check for a new version, run

``pip3 install vyper-bot --upgrade``

.. NOTE::
    If you get an error saying that pip3 is not recognized as an internal or external command, try running ``py -m -3 pip install vyper-bot``.
    This can occur if python isn't installed correctly or if it isn't added to the $PATH on windows.

Getting Started
---------------

When first starting to get your bot up and running, you must start by getting a bot key from the |bf|.
This key can be retrieved by sending ``/newbot`` in a message to |bf|_. After answering a few questions,
you will be rewarded with a key that will look very similar to ``123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11``.

The most simple program that you can make is one that only has an object representing the API.
I prefer to name this object ``bot`` as this makes it easier to reference later when making calls.

.. code:: python

    from vyper import vyper

    bot = vyper.API()

This API object is fully functional, but won't do anything for a few reasons.
First of all, we aren't asking it to do anything, but also, the bot key isn't put into the API yet.
All you have to do to make the key part of the bot is to take this line 

.. code:: python

    bot = vyper.API()

and turn it into

.. code:: python

    bot = vyper.API().configure('botkey')

where ``botkey`` is your key that you got from |bf|.

.. IMPORTANT::
    Make sure you change the botkey or your code WILL NOT WORK!

Now, you can run any of the methods from the |tgapi|_ using the following code as an example.

.. code:: python

    # Sends a message to the chat id or chat username.
    bot.sendMessage(chat_id, 'Test message')

This will send the message ``Test Message`` to the chat that you specify.

.. |botkey| replace:: 123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11
.. |bf| replace:: BotFather
.. _bf: https://t.me/BotFather
.. |tgapi| replace:: Telegram API
.. _tgapi: https://core.telegram.org/bots/api#available-methods

Getting Updates
---------------

One of the biggest requirements of a telegram bot is the ability to get the messages that are sent to a group
so that it can send a message back in response to commands.
I've made the process of getting updates extremely simple, just modifying one of the existing lines.
All that needs to be done is to create a method that will be run from a message being sent.

.. code:: python

    from vyper import vyper
    import time
    
    def on_message(msg):
        msg = msg['message']
        bot.sendMessage(msg['chat']['id'], 'I have recieved your message')

    bot = vyper.API().configure('123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11', functions={'message': on_message})

    while True:
        bot.getUpdates()
        time.sleep(.05)

.. NOTE::
    You can use any of the following as a key in the functions dictionary:
        :py:const:`message`
        :py:const:`edited_message`
        :py:const:`channel_post`
        :py:const:`edited_channel_post`
        :py:const:`inline_query`
        :py:const:`chosen_inline_result`
        :py:const:`callback_query`
        :py:const:`shipping_query`
        :py:const:`pre_checkout_query`