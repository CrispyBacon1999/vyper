import requests, json, sys, os
from vyper import vyperconfig


# @title Vyper Bot
# @author Josh Bacon

class API():
	_token = ''
	_debug = False
	_functions = None
	def configure(self, token, functions=None,debug=False):
		if not token or not isinstance(token, str):
			raise ValueError("Provide a valid token. Can be retrieved from @BotFather!")
		self._token = token
		self._debug = debug
		self._functions = functions
		return self

	def request(self, endpoint, parameters=None, file=None):
		if not endpoint or type(endpoint) is not str:
			sys.exit("Tried to make invalid request.")
		# Make Request
		req = json.loads(requests.get(vyperconfig.apiurl % (self._token, endpoint), params=parameters, files=file).text)
		if req['ok']:
			return req['result']
		else:
			print("Tried to make invalid request: %s" % endpoint)
			print(parameters)

	def getMe(self):
		return self.request('getMe')

	def getUpdates(self):
		if os.path.isfile(vyperconfig.lastupdatefile):
			lastupdate = open(vyperconfig.lastupdatefile, 'r')
		else:
			lastupdate = open(vyperconfig.lastupdatefile, 'a+')
		lastup = lastupdate.read()
		if(lastup):
			offset = int(lastup)+1
			updates = self.request('getUpdates', parameters={'offset': offset})
		else:
			updates = self.request('getUpdates')
		for update in updates:
			for key, value in self._functions.items():
				if key in update:
					value(update)
		if(len(updates) > 0):
			lastupdate = open(vyperconfig.lastupdatefile, 'w')
			lastupdate.write(str(updates[-1]['update_id']))
			lastupdate.close()

	def _mapupdate(update):

		class Message:
			def __init__(self, update):
				self._update = update
				self.message_id = update['message_id']
				self.date = update['date']
				self.chat = Chat(update['chat'])


		if 'message' in update:
			update['message'] = Message(update)


	def sendMessage(self, chat_id, text, parse_mode=None, disable_web_page_preview=False, disable_notification=False, reply_to_message_id=None, reply_markup=None):
		params = {
			'chat_id': chat_id,
			'text': text,
			'parse_mode': parse_mode,
			'disable_web_page_preview': disable_web_page_preview,
			'disable_notification': disable_notification,
			'reply_to_message_id': reply_to_message_id,
			'reply_markup': reply_markup
			}
		paramscleaned = {k: v for k, v in params.items() if v}
		return self.request('sendMessage', parameters=paramscleaned)

	def forwardMessage(self, chat_id, from_chat_id, message_id, disable_notification=False):
		params = {
			'chat_id': chat_id,
			'from_chat_id': from_chat_id,
			'message_id': message_id,
			'disable_notification': disable_notification
			}
		paramscleaned = {k: v for k, v in params.items() if v}
		return self.request('forwardMessage', parameters=paramscleaned)

	def sendPhoto(self, chat_id, photo, caption='', disable_notification=False, reply_to_message_id=None, reply_markup=None):
		params = {
			'chat_id': chat_id,
			'caption': caption,
			'disable_notification': disable_notification,
			'reply_to_message_id': reply_to_message_id,
			'reply_markup': reply_markup
			}
		paramscleaned = {k: v for k, v in params.items() if v}
		return self.request('sendPhoto', parameters=paramscleaned, file={'photo': photo})

	def sendAudio(self, chat_id, audio, caption='', duration=None, performer='', title='', disable_notification=False, reply_to_message_id=None, reply_markup=None):
		params = {
			'chat_id': chat_id,
			'caption': caption,
			'duration': duration,
			'performer': performer,
			'title': title,
			'disable_notification': disable_notification,
			'reply_to_message_id': reply_to_message_id,
			'reply_markup': reply_markup
			}
		paramscleaned = {k: v for k, v in params.items() if v}
		return self.request('sendAudio', parameters=paramscleaned, file={'audio': audio})

	def sendDocument(self, chat_id, document, caption='', disable_notification=False, reply_to_message_id=None, reply_markup=None):
		params = {
			'chat_id': chat_id,
			'caption': caption,
			'disable_notification': disable_notification,
			'reply_to_message_id': reply_to_message_id,
			'reply_markup': reply_markup
			}
		paramscleaned = {k: v for k, v in params.items() if v}
		return self.request('sendDocument', parameters=paramscleaned, file={'document': document})

	def sendSticker(self, chat_id, sticker, disable_notification=False, reply_to_message_id=None, reply_markup=None):
		params = {
			'chat_id': chat_id,
			'disable_notification': disable_notification,
			'reply_to_message_id': reply_to_message_id,
			'reply_markup': reply_markup
			}
		paramscleaned = {k: v for k, v in params.items() if v}
		return self.request('sendSticker', parameters=paramscleaned, file={'sticker': sticker})

	def sendVideo(self, chat_id, video, duration=None, width=None, height=None, caption='', disable_notification=False, reply_to_message_id=None, reply_markup=None):
		params = {
			'chat_id': chat_id,
			'duration': duration,
			'width': width,
			'height': height,
			'caption': caption,
			'disable_notification': disable_notification,
			'reply_to_message_id': reply_to_message_id,
			'reply_markup': reply_markup
			}
		paramscleaned = {k: v for k, v in params.items() if v}
		return self.request('sendVideo', parameters=paramscleaned, file={'video': video})

	def sendVoice(self, chat_id, voice, caption=None, duration=None, disable_notification=False, reply_to_message_id=None, reply_markup=None):
		params = {
			'chat_id': chat_id,
			'duration': duration,
			'caption': caption,
			'disable_notification': disable_notification,
			'reply_to_message_id': reply_to_message_id,
			'reply_markup': reply_markup
			}
		paramscleaned = {k: v for k, v in params.items() if v}
		return self.request('sendVoice', parameters=paramscleaned, file={'voice': voice})

	def sendVideoNote(self, chat_id, video_note, length=None, duration=None, disable_notification=False, reply_to_message_id=None, reply_markup=None):
		params = {
			'chat_id': chat_id,
			'duration': duration,
			'length': caption,
			'disable_notification': disable_notification,
			'reply_to_message_id': reply_to_message_id,
			'reply_markup': reply_markup
			}
		paramscleaned = {k: v for k, v in params.items() if v}
		return self.request('sendVideoNote', parameters=paramscleaned, file={'video_note': voice})
		
	def sendLocation(self, chat_id, latitude, longitude, disable_notification=False, reply_to_message_id=None, reply_markup=None):
		params = {
			'chat_id': chat_id,
			'latitude': latitude,
			'longitude': longitude,
			'disable_notification': disable_notification,
			'reply_to_message_id': reply_to_message_id,
			'reply_markup': reply_markup
			}
		paramscleaned = {k: v for k, v in params.items() if v}
		return self.request('sendLocation', parameters=paramscleaned)
		
	def sendVenue(self, chat_id, latitude, longitude, title, address, foursquare_id='', disable_notification=False, reply_to_message_id=None, reply_markup=None):
		params = {
			'chat_id': chat_id,
			'latitude': latitude,
			'longitude': longitude,
			'title': title,
			'address': address,
			'foursquare_id': foursquare_id,
			'disable_notification': disable_notification,
			'reply_to_message_id': reply_to_message_id,
			'reply_markup': reply_markup
			}
		paramscleaned = {k: v for k, v in params.items() if v}
		return self.request('sendVenue', parameters=paramscleaned)

	def sendContact(self, chat_id, phone_number,first_name, last_name, disable_notification=False, reply_to_message_id=None, reply_markup=None):
		params = {
			'chat_id': chat_id,
			'phone_number': phone_number,
			'first_name': first_name,
			'last_name': last_name,
			'disable_notification': disable_notification,
			'reply_to_message_id': reply_to_message_id,
			'reply_markup': reply_markup
			}
		paramscleaned = {k: v for k, v in params.items() if v}
		return self.request('sendContact', parameters=paramscleaned)

	def sendChatAction(self, chat_id, action):
		params = {
			'chat_id': chat_id,
			'action': action
			}
		return self.request('sendChatAction', parameters=params)

	def getUserProfilePhotos(self, user_id, offset=None, limit=None):
		params = {
			'user_id': user_id,
			'offset': offset,
			'limit': limit
			}
		paramscleaned = {k: v for k, v in params.items() if v}
		return self.request('getUserProfilePhotos', parameters=paramscleaned)

	def getFile(self, file_id):
		params = {
			'file_id': file_id
			}
		return self.request('getFile', parameters=params)

	def kickChatMember(self, chat_id, user_id, until_date=0):
		params = {
			'chat_id': chat_id,
			'user_id': user_id,
			'until_date': until_date
			}
		return self.request('kickChatMember', parameters=params)

	def unbanChatMember(self, chat_id, user_id):
		params = {
			'chat_id': chat_id,
			'user_id': user_id
			}
		return self.request('unbanChatMember', parameters=params)

	def restrictChatMember(self, chat_id, user_id, until_date=0, can_send_messages=True, can_send_media_messages=True, can_send_other_messages=True, can_add_web_page_previews=True):
		params = {
			'chat_id': chat_id,
			'user_id': user_id,
			'until_date': until_date,
			'can_send_messages': can_send_messages,
			'can_send_media_messages': can_send_media_messages,
			'can_send_other_messages': can_send_other_messages,
			'can_add_web_page_previews': can_add_web_page_previews
			}
		paramscleaned = {k: v for k, v in params.items() if v}
		return self.request('restrictChatMember', parameters=paramscleaned)

	def leaveChat(self, chat_id):
		params = {
			'chat_id': chat_id
			}
		return self.request('leaveChat', parameters=params)

		
	def getChat(self, chat_id):
		params = {
			'chat_id': chat_id
			}
		return self.request('getChat', parameters=params)

	def getChatAdministrators(self, chat_id):
		params = {
			'chat_id': chat_id
			}
		return self.request('getChatAdministrators', parameters=params)

	def getChatMembersCount(self, chat_id):
		params = {
			'chat_id': chat_id
			}
		return self.request('getChatMembersCount', parameters=params)

	def getChatMember(self, chat_id, user_id):
		params = {
			'chat_id': chat_id,
			'user_id': user_id
			}
		return self.request('getChatMember', parameters=params)

	def answerCallbackQuery(self, callback_query_id, text='', show_alert=False, url='', cache_time=None):
		params = {
			'callback_query_id': callback_query_id,
			'text': text,
			'show_alert': show_alert,
			'url': url,
			'cache_time': cache_time
			}
		paramscleaned = {k: v for k, v in params.items() if v}
		return self.request('answerCallbackQuery', parameters=paramscleaned)

	def editMessageText(self, text, chat_id=None, message_id=None, inline_message_id=None, parse_mode=None, disable_web_page_preview=False, reply_markup=None):
		params = {
			'text': text,
			'chat_id': chat_id,
			'message_id': message_id,
			'inline_message_id': inline_message_id,
			'parse_mode': parse_mode,
			'disable_web_page_preview': disable_web_page_preview,
			'reply_markup': reply_markup
			}
		paramscleaned = {k: v for k, v in params.items() if v}
		return self.request('editMessageText', parameters=paramscleaned)

	def editMessageCaption(self, chat_id=None, message_id=None, inline_message_id=None, caption=None, reply_markup=None):
		params = {
			'caption': caption,
			'chat_id': chat_id,
			'message_id': message_id,
			'inline_message_id': inline_message_id,
			'reply_markup': reply_markup
			}
		paramscleaned = {k: v for k, v in params.items() if v}
		return self.request('editMessageCaption', parameters=paramscleaned)

	def editMessageReplyMarkup(self, chat_id=None, message_id=None, inline_message_id=None, reply_markup=None):
		params = {
			'chat_id': chat_id,
			'message_id': message_id,
			'inline_message_id': inline_message_id,
			'reply_markup': reply_markup
			}
		paramscleaned = {k: v for k, v in params.items() if v}
		return self.request('editMessageReplyMarkup', parameters=paramscleaned)

	def deleteMessage(self, chat_id, message_id):
		params = {
			'chat_id': chat_id,
			'message_id': message_id
			}
		paramscleaned = {k: v for k, v in params.items() if v}
		return self.request('deleteMessage', parameters=paramscleaned)

	def answerInlineQuery(self, inline_query_id, results, cache_time=None, is_personal=False, next_offset='', switch_pm_text='', switch_pm_parameter=''):
		params = {
			'inline_query_id': inline_query_id,
			'results': results,
			'cache_time': cache_time,
			'is_personal': is_personal,
			'next_offset': next_offset,
			'switch_pm_text': switch_pm_text,
			'switch_pm_parameter': switch_pm_parameter
			}
		paramscleaned = {k: v for k, v in params.items() if v}
		return self.request('answerInlineQuery', parameters=paramscleaned)

	# Payments
	def sendInvoice(self, chat_id, title, description, payload, provider_token, start_parameter, currency, prices, photo_url='',
					photo_size=None, photo_height=None, photo_width=None, need_name=False, need_phone_number=False, need_email=False, need_shipping_address=False,
					is_flexible=False, disable_notification=False, reply_to_message_id=None, reply_markup=None):
		params = {
			'chat_id': chat_id,
			'title': title,
			'description': description,
			'payload': payload,
			'provider_token': provider_token,
			'start_parameter': start_parameter,
			'currency': currency,
			'prices': prices,
			'photo_url': photo_url,
			'photo_size': photo_size,
			'photo_width': photo_width,
			'photo_height': photo_height,
			'need_name': need_name,
			'need_phone_number': need_phone_number,
			'need_email': need_email,
			'need_shipping_address': need_shipping_address,
			'is_flexible': is_flexible,
			'disable_notification': disable_notification,
			'reply_to_message_id': reply_to_message_id,
			'reply_markup': reply_markup
			}
		paramscleaned = {k: v for k, v in params.items() if v}
		return self.request('sendInvoice', parameters=paramscleaned)
	
	def answerShippingQuery(self, shipping_query_id, ok, shipping_options=None, error_message=''):
		params = {
			'shipping_query_id': shipping_query_id,
			'ok': ok,
			'shipping_options': shipping_options,
			'error_message': error_message
			}
		paramscleaned = {k: v for k, v in params.items() if v}
		return self.request('answerShippingQuery', parameters=paramscleaned)

	def answerPreCheckoutQuery(self, pre_checkout_query_id, ok, error_message=''):
		params = {
			'pre_checkout_query_id': pre_checkout_query_id,
			'ok': ok,
			'error_message': error_message
			}
		paramscleaned = {k: v for k, v in params.items() if v}
		return self.request('answerPreCheckoutQuery', parameters=paramscleaned)

	#Games
	def sendGame(self, chat_id, game_short_name, disable_notification=False, reply_to_message_id=None, reply_markup=None):
		params = {
			'chat_id': chat_id,
			'game_short_name': game_short_name,
			'disable_notification': disable_notification,
			'reply_to_message_id': reply_to_message_id,
			'reply_markup': reply_markup
			}
		paramscleaned = {k: v for k, v in params.items() if v}
		return self.request('sendGame', parameters=paramscleaned)

	

	def promoteChatMember(self, chat_id, user_id, can_change_info=False, can_post_messages=False, can_edit_messages=False, can_delete_messages=False, can_invite_users=False, can_restrict_members=False, can_pin_messages=False, can_promote_members=False):
		params = {
			'chat_id': chat_id,
			'user_id': user_id,
			'can_change_info': can_change_info,
			'can_post_messages': can_post_messages,
			'can_edit_messages': can_edit_messages,
			'can_delete_messages': can_delete_messages,
			'can_invite_users': can_invite_users,
			'can_restrict_members': can_restrict_members,
			'can_pin_messages': can_pin_messages
			}
		paramscleaned = {k: v for k, v in params.items() if v}
		return self.request('promoteChatMember', parameters=paramscleaned)

	def exportChatInviteLink(self, chat_id):
		params = {
			'chat_id': chat_id
			}
		paramscleaned = {k: v for k, v in params.items() if v}
		return self.request('exportChatInviteLink', parameters=paramscleaned)
		
	def setChatPhoto(self, chat_id, photo):
		params = {
			'chat_id': chat_id,
			'photo': photo
			}
		paramscleaned = {k: v for k, v in params.items() if v}
		return self.request('setChatPhoto', parameters=paramscleaned)
		
	def deleteChatPhoto(self, chat_id):
		params = {
			'chat_id': chat_id
			}
		paramscleaned = {k: v for k, v in params.items() if v}
		return self.request('deleteChatPhoto', parameters=paramscleaned)
		
	def setChatTitle(self, chat_id, title):
		params = {
			'chat_id': chat_id,
			'title': title
			}
		paramscleaned = {k: v for k, v in params.items() if v}
		return self.request('setChatTitle', parameters=paramscleaned)
		
	def setChatDescription(self, chat_id, description):
		params = {
			'chat_id': chat_id,
			'description': description
			}
		paramscleaned = {k: v for k, v in params.items() if v}
		return self.request('setChatDescription', parameters=paramscleaned)
		
	def pinChatMessage(self, chat_id, message_id, disable_notification=False):
		params = {
			'chat_id': chat_id,
			'message_id': message_id,
			'disable_notification': disable_notification
			}
		paramscleaned = {k: v for k, v in params.items() if v}
		return self.request('pinChatMessage', parameters=paramscleaned)
	
	def unpinChatMessage(self, chat_id):
		params = {
			'chat_id': chat_id
			}
		paramscleaned = {k: v for k, v in params.items() if v}
		return self.request('unpinChatMessage', parameters=paramscleaned)
		
	# Sticker Sets
	def getStickerSet(self, name):
		params = {
			'name': name
			}
		paramscleaned = {k: v for k, v in params.items() if v}
		return self.request('getStickerSet', parameters=paramscleaned)
	
	def uploadStickerFile(self):
		params = {
			'user_id': user_id
			}
		paramscleaned = {k: v for k, v in params.items() if v}
		return self.request('uploadStickerFile', parameters=paramscleaned, file={'png_sticker': png_sticker})
	
	def createNewStickerSet(self, user_id, name, title, png_sticker, emojis, contains_masks=False, mask_position=None):
		params = {
			'user_id': user_id,
			'name': name,
			'title': title,
			'emojis': emojis,
			'contains_masks': contains_masks,
			'mask_position': mask_position
			}
		paramscleaned = {k: v for k, v in params.items() if v}
		return self.request('createNewStickerSet', parameters=paramscleaned, file={'png_sticker': png_sticker})

	def addStickerToSet(self, user_id, name, png_sticker, emojis, mask_position=None):
		params = {
			'user_id': user_id,
			'name': name,
			'emojis': emojis,
			'mask_position': mask_position
			}
		paramscleaned = {k: v for k, v in params.items() if v}
		return self.request('addStickerToSet', parameters=paramscleaned, file={'png_sticker': png_sticker})
	
	def setStickerPositionInSet(self, sticker, position):
		params = {
			'sticker': sticker,
			'position': position
		}
		paramscleaned = {k: v for k, v in params.items() if v}
		return self.request('setStickerPositionInSet', parameters=paramscleaned)
	
	def deleteStickerFromSet(self, sticker):
		params = {
			'sticker': sticker
		}
		paramscleaned = {k: v for k, v in params.items() if v}
		return self.request('deleteStickerFromSet', parameters=paramscleaned)
		
from enum import Enum
class ChatAction(Enum):
	TYPING = 'typing',
	PHOTO = 'upload_photo'
	UVIDEO = 'upload_video'
	RVIDEO = 'record_video'
	UAUDIO = 'upload_audio'
	RAUDIO = 'record_audio'
	DOCUMENT = 'upload_document'
	LOCATION = 'find_location'
	UVIDNOTE = 'upload_video_note'
	RVIDNOTE = 'record_video_note'
	
	
