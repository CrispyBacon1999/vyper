import json


class Item:
    def __init__(self, name, description, token, start_parameter=None, currency='USD', prices=None):
        '''
        Creates a new Item that can be sent via an invoice to a user
        If start_parameter is blank, one will be generated and returned in the start_parameter variable
        '''
        self.name = name
        self.description = description
        self.token = token
        if start_parameter:
            self.start_parameter = start_parameter
        else:
            self.start_parameter = ''.join(name.split())
        self.currency = currency
        if not prices:
            raise NoPricesError('There are no prices applied to the item. Send a list of prices.')
        else:
            self.prices = json.dumps(prices)
    def invoice(self, msg):
        chat_id = msg['chat']['id']
        payload = str(msg['from']['id']) + self.start_parameter
        return ((chat_id, self.name, self.description, payload, self.token, self.start_parameter, self.currency, self.prices), Payload(payload, self))

class Payload:
    def __new__(cls, payload, item):
        return {'payload': payload, 'item': item}

class LabeledPrice:
    def __new__(cls, label, price):
        return {'label': label, 'amount': price}
def NoPricesError(IndexError):
    pass
