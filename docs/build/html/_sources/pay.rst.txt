Payments
========

.. toctree::
    :maxdepth: 1
    :caption: Contents
    :name: master
    :titlesonly:
    :hidden:


The Telegram Payment System
---------------------------

When first trying to figure out the payment system built into Telegram, it can be extremely daunting. My first time trying to learn how it worked wasn't extremely difficult, but still took some getting used to, as well as some custom functions to make life easier. After you figure it out for the first time though, it just clicks on how it works.

.. image:: tgpay.png

Above is the general idea of what has to happen to make a payment go through properly. It's really only 2 steps on the bot side of things if the product doesn't need delivery, so it can be super simple. Adding shipping information only requires one extra step, which is just confirming that the location can actually be shipped to (kind of important).

Vyper Payments
--------------

.. NOTE::
    If you don't have a payment provider code yet, make sure to head over to BotFather and get one, or none of this will work. 

The payments in vyper work in the same order as in the Telegram system (seeing as it's what it runs on), but I've added a few extra functions to make things easier to keep track of. When using the default system, you need to define a "payload" for the order, which took me a while to realize is just a string that can be tied to the order that's being processed. This makes it easier to keep track of the payment, but can be confusing to come up with. If you use the :py:class:`payments.Item` class, you don't have to worry about quite a bit of the information in the payment.

To make an item, all you need to do is create the item file, then pass the result of the invoice method into the sendInvoice() method. I'll be using an example for a pluginbot design.

.. IMPORTANT::
    If you don't split the result of :py:func:`invoice` into the invoice and payload, everything will break. Also, make sure to deconstruct the invoice into all the parameters using an asterisk. ``self.bot.sendInvoice(*invoice)`` This is because it's returned as a tuple of all the values needed for the invoice, so if you don't break it down, it will break horribly.

.. code:: python

    stripe = 'STRIPE TEST CODE RETRIEVED FROM BOTFATHER'
    item = payments.Item('Test Item', 'Test Description', stripe, prices=[payments.LabeledPrice('Item', 500)])

    class Pay(pluginbot.Plugin):
        def message(self, msg):
            if msg['text'] == '/pay':
                invoice, payload = item.invoice(msg)
                self.bot.sendInvoice(*invoice)
    
As you can see, the :py:class:`payments.Item` format makes it so only 4 arguments are needed to send the item, as the rest can be generated easily. Normally, it would take 8 different arguments to send an invoice to the user, but I automatically fill the currency, start_parameter, payload, and chat_id for you. The start_parameter will just be the name of the item, with spaces stripped off of it, and the currency will be defaulted to USD, but can be changed in the constructor. For the payload, I generate a string using the user's id and the start parameter, as well as appending the unix timestamp to the end, creating a payload that looks similar to ``123456789TestProduct1416667432``. This makes it both easy to identify, as well as unique for every user, so you won't have to worry about duplicates. The only way a duplicate could be created is if a user tried to send multiple orders in the exact same second, which is extremely unlikely.