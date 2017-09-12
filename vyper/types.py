import json

def build(msg):
	new = None
	for k, v in msg.items():
		if 'message' == k:
			return Message(v)
		if 'edited_message' == k:
			return Message(v)
		if 'channel_post' == k:
			return Message(v)
		if 'edited_channel_post' == k:
			return Message(v)
		if 'inline_query' == k:
			return InlineQuery(v)
		if 'chosen_inline_result' == k:
			return ChosenInlineResult(v)
		if 'callback_query' == k:
			return CallbackQuery(v)
		if 'shipping_query' == k:
			return ShippingQuery(v)
		if 'pre_checkout_query' == k:
			return PreCheckoutQuery(v)

class Message:
	def __init__(self, msg):
		for k, v in msg.items():
			if k in ['from', 'forward_from', 'new_chat_member', 'left_chat_member']:
				setattr(self, k if k != 'from' else 'frm', User(v))
			elif k in ['chat', 'forward_from_chat']:
				setattr(self, k, Chat(v))
			elif k in ['reply_to_message', 'pinned_message']:
				setattr(self, k, Message(v))
			elif k == 'entities':
				setattr(self, k, [MessageEntity(entity) for entity in v])
			elif k == 'audio':
				setattr(self, k, Audio(v))
			elif k == 'document':
				setattr(self, k, Document(v))
			elif k == 'game':
				setattr(self, k, Game(v))
			elif k in ['photo', 'new_chat_photo']:
				setattr(self, k, [PhotoSize(photosize) for photosize in v])
			elif k == 'sticker':
				setattr(self, k, Sticker(v))
			elif k == 'video':
				setattr(self, k, Video(v))
			elif k == 'voice':
				setattr(self, k, Voice(v))
			elif k == 'video_note':
				setattr(self, k, VideoNote(v))
			elif k == 'new_chat_members':
				setattr(self, k, [User(member) for member in v])
			elif k == 'contact':
				setattr(self, k, Contact(v))
			elif k == 'location':
				setattr(self, k, Location(v))
			elif k == 'venue':
				setattr(self, k, Venue(v))
			elif k == 'invoice':
				setattr(self, k, Invoice(v))
			elif k == 'successful_payment':
				setattr(self, k, SuccessfulPayment(v))
			else:
				setattr(self, k, v)


class InlineQuery:
	def __init__(self, msg):
		for k, v in msg.items():
			if k == 'from':
				setattr(self, 'frm', User(v))
			elif k == 'location':
				setattr(self, k, Location(v))
			else:
				setattr(self, k, v)

class ChosenInlineResult:
	def __init__(self, msg):
		for k, v in msg.items():
			if k == 'from':
				setattr(self, 'frm', User(v))
			elif k == 'location':
				setattr(self, k, Location(v))
			else:
				setattr(self, k, v)

class CallbackQuery:
	def __init__(self, msg):
		for k, v in msg.items():
			if k == 'from':
				setattr(self, 'frm', User(v))
			elif k == 'message':
				setattr(self, k, Message(v))
			else:
				setattr(self, k, v)

class ShippingQuery:
	def __init__(self, msg):
		for k, v in msg.items():
			if k == 'from':
				setattr(self, 'frm', User(v))
			elif k == 'shipping_address':
				setattr(self, k, ShippingAddress(v))
			else:
				setattr(self, k, v)

class PreCheckoutQuery:
	def __init__(self, msg):
		for k, v in msg.items():
			if k == 'from':
				setattr(self, 'frm', User(v))
			elif k == 'order_info':
				setattr(self, k, OrderInfo(v))
			else:
				setattr(self, k, v)

class ShippingAddress:
	def __init__(self, msg):
		for k, v in msg.items():
			setattr(self, k, v)

class SuccessfulPayment:
	def __init__(self, msg):
		for k, v in msg.items():
			if k == 'order_info':
				setattr(self, k, OrderInfo(v))
			else:
				setattr(self, k, v)

class OrderInfo:
	def __init__(self, msg):
		for k, v in msg.items():
			if k == 'from':
				setattr(self, 'frm', User(v))
			elif k == 'order_info':
				setattr(self, k, ShippingAddress(v))
			else:
				setattr(self, k, v)

class Invoice:
	def __init__(self, msg):
		for k, v in msg.items():
			setattr(self, k, v)

class User:
	def __init__(self, msg):
		for k, v in msg.items():
			setattr(self, k, v)

class Chat:
	def __init__(self, msg):
		for k, v in msg.items():
			if k == 'photo':
				setattr(self, k, ChatPhoto(v))
			elif k == 'pinned_message':
				setattr(self, k, Message(v))
			else:
				setattr(self, k, v)

class MessageEntity:
	def __init__(self, msg):
		for k, v in msg.items():
			if k == 'user':
				setattr(self, k, User(v))
			else:
				setattr(self, k, v)

class PhotoSize:
	def __init__(self, msg):
		for k, v in msg.items():
			setattr(self, k, v)

class Audio:
	def __init__(self, msg):
		for k, v in msg.items():
			setattr(self, k, v)

class Document:
	def __init__(self, msg):
		for k, v in msg.items():
			if k == 'thumb':
				setattr(self, k, PhotoSize(v))
			else:
				setattr(self, k, v)

class Video:
	def __init__(self, msg):
		for k, v in msg.items():
			if k == 'thumb':
				setattr(self, k, PhotoSize(v))
			else:
				setattr(self, k, v)

class Voice:
	def __init__(self, msg):
		for k, v in msg.items():
			setattr(self, k, v)

class VideoNote:
	def __init__(self, msg):
		for k, v in msg.items():
			if k == 'thumb':
				setattr(self, k, PhotoSize(v))
			else:
				setattr(self, k, v)

class Contact:
	def __init__(self, msg):
		for k, v in msg.items():
			setattr(self, k, v)

class Location:
	def __init__(self, msg):
		for k, v in msg.items():
			setattr(self, k, v)

class Venue:
	def __init__(self, msg):
		for k, v in msg.items():
			if k == 'location':
				setattr(self, k, Location(v))
			else:
				setattr(self, k, v)

class UserProfilePhotos:
	def __init__(self, msg):
		for k, v in msg.items():
			if k == 'photos':
				setattr(self, k, [[PhotoSize(size) for size in photo] for photo in v])
			else:
				setattr(self, k, v)

class File:
	def __init__(self, msg):
		for k, v in msg.items():
			setattr(self, k, v)

class ReplyKeyboardMarkup:
	def __init__(self, msg):
		for k, v in msg.items():
			if k == 'keyboard':
				setattr(self, k, [[KeyboardButton(button) for button in row] for row in v])
			else:
				setattr(self, k, v)

class KeyboardButton:
	def __init__(self, msg):
		for k, v in msg.items():
			setattr(self, k, v)

class ReplyKeyboardRemove:
	def __init__(self, msg):
		for k, v in msg.items():
			setattr(self, k, v)

class InlineKeyboardMarkup:
	def __init__(self, msg):
		for k, v in msg.items():
			if k == 'inline_keyboard':
				setattr(self, k, [[InlineKeyboardButton(button) for button in row] for row in v])
			else:
				setattr(self, k, v)

class InlineKeyboardButton:
	def __init__(self, msg):
		for k, v in msg.items():
			if k == 'callback_game':
				setattr(self, k, CallbackGame(v))
			else:
				setattr(self, k, v)

class CallbackQuery:
	def __init__(self, msg):
		for k, v in msg.items():
			if k == 'from':
				setattr(self, 'frm', PhotoSize(v))
			elif k == 'message':
				setattr(self, k, Message(v))
			else:
				setattr(self, k, v)

class ForceReply:
	def __init__(self, msg):
		for k, v in msg.items():
			setattr(self, k, v)

class ChatPhoto:
	def __init__(self, msg):
		for k, v in msg.items():
			setattr(self, k, v)

class ChatMember:
	def __init__(self, msg):
		for k, v in msg.items():
			if k == 'user':
				setattr(self, k, User(v))
			else:
				setattr(self, k, v)

class ResponseParameters:
	def __init__(self, msg):
		for k, v in msg.items():
			setattr(self, k, v)
