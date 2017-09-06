Api Documentation
=================

.. toctree::
    :maxdepth: 1
    :caption: Contents
    :name: master
    :titlesonly:
    :hidden:


.. class:: API

    **Vyper Methods**

    .. method:: configure(token, functions={}, debug=False)

        Configures the bot with the token and functions to run on updates.

        :param str token: The token of the bot retrieved from the BotFather
        :param dict functions: A dictionary that has the message types and functions
        :param boolean debug: An experimental value that doesn't have a use yet, but will in later versions
        :raises ValueError: if token is blank or not a string

    .. method:: request(endpoint, parameters=None, file=None)

        Requests the endpoint from the telegram API. Shouldn't need to be called as the other functions run this more effectively.

        :param str endpoint: The endpoint to be requested
        :param dict parameters: The parameters attached to the request
        :param file file: A file that is sent with the request
        :return: Value retrieved from API, usually updates or a success dictionary
        :rtype: :py:obj:`dict`

        Valid parameter keys for ``parameters``:
        :py:const:`message`
        :py:const:`edited_message`
        :py:const:`channel_post`
        :py:const:`edited_channel_post`
        :py:const:`inline_query`
        :py:const:`chosen_inline_result`
        :py:const:`callback_query`
        :py:const:`shipping_query`
        :py:const:`pre_checkout_query`

    **Telegram Commands**

    .. method:: getMe(self)

        Retrieves the user object for the bot.

        :return: The bot
        :rtype: User Object

    .. method:: getUpdates(self)

        Gets the updates that are pending an update. Will store the current update value in the file ``lastupdate.vyper``.

        :return: Doesn't return a value, but instead runs the corresponding function

    .. method:: sendMessage(chat_id, text, parse_mode=None, disable_web_page_preview=False, disable_notification=False, reply_to_message_id=None, reply_markup=None)

        Sends a message to the chat specified.

        :param int chat_id: Chat id of the target chat
        :param str text: Text to send in the message
        :param str parse_mode: `Markdown` or `HTML`, depending on which formatting style is preferred
        :param boolean disable_web_page_preview: Whether to show a preview of the webpage on the message
        :param boolean disable_notification: Whether to disable the notification for the message
        :param int reply_to_message_id: The message id to make the message reply to
        :param dict reply_markup: The custom markup applied to the message, such as inline keyboards

    .. method:: forwardMessage(chat_id, from_chat_id, message_id, disable_notification=False)

        Forwards a message from one chat to another.

        :param int chat_id: Chat id of the target chat
        :param int from_chat_id: Chat id of the original chat
        :param int message_id: Message id of the message from the original chat
        :param boolean disable_notification: Whether to disable the notification for the message        

    .. method:: sendPhoto(chat_id, photo, caption='', disable_notification=False, reply_to_message_id=None, reply_markup=None)

        Sends a photo to the chat specified.

        :param int chat_id: Chat id of the target chat
        :param file photo: Photo to send
        :param str caption: The text displayed with the photo
        :param boolean disable_notification: Whether to disable the notification for the message
        :param int reply_to_message_id: The message id to make the message reply to
        :param dict reply_markup: The custom markup applied to the message, such as inline keyboards

    .. method:: sendAudio(chat_id, audio, caption='', duration=None, performer='', title='', disable_notification=False, reply_to_message_id=None, reply_markup=None)

        Sends an audio track to the chat specified.

        :param int chat_id: Chat id of the target chat
        :param file audio: Audio track to send
        :param str caption: The text displayed with the audio
        :param int duration: The duration of the track
        :param str performer: Performer of the track
        :param str title: Title of the track
        :param boolean disable_notification: Whether to disable the notification for the message
        :param int reply_to_message_id: The message id to make the message reply to
        :param dict reply_markup: The custom markup applied to the message, such as inline keyboards

    .. method:: sendDocument(chat_id, document, caption='', disable_notification=False, reply_to_message_id=None, reply_markup=None)

        Sends a document to the chat specified.

        :param int chat_id: Chat id of the target chat
        :param file document: Audio track to send
        :param str caption: The text displayed with the audio
        :param boolean disable_notification: Whether to disable the notification for the message
        :param int reply_to_message_id: The message id to make the message reply to
        :param dict reply_markup: The custom markup applied to the message, such as inline keyboards

    .. method:: sendVideo(self, chat_id, video, duration=None, width=None, height=None, caption='', disable_notification=False, reply_to_message_id=None, reply_markup=None)

        Sends a video to the chat specified.

        :param int chat_id: Chat id of the target chat
        :param file audio: Audio track to send
        :param int duration: The duration of the video
        :param int width: Width of the video
        :param int height: Height of the video
        :param str caption: The text displayed with the video
        :param boolean disable_notification: Whether to disable the notification for the message
        :param int reply_to_message_id: The message id to make the message reply to
        :param dict reply_markup: The custom markup applied to the message, such as inline keyboards

    .. method:: sendVoice(self, chat_id, voice, caption=None, duration=None, disable_notification=False, reply_to_message_id=None, reply_markup=None)

        Sends a voice message to the chat specified.

        :param int chat_id: Chat id of the target chat
        :param file voice: Audio to send (.ogg)
        :param str caption: The text displayed with the audio
        :param int duration: The duration of the message
        :param boolean disable_notification: Whether to disable the notification for the message
        :param int reply_to_message_id: The message id to make the message reply to
        :param dict reply_markup: The custom markup applied to the message, such as inline keyboards

    .. method:: sendVideoNote(self, chat_id, video_note, length=None, duration=None, disable_notification=False, reply_to_message_id=None, reply_markup=None)

        Sends a video note to the chat specified.

        :param int chat_id: Chat id of the target chat
        :param file video_note: Video to send
        :param int duration: The duration of the track
        :param int length: Video width and height
        :param boolean disable_notification: Whether to disable the notification for the message
        :param int reply_to_message_id: The message id to make the message reply to
        :param dict reply_markup: The custom markup applied to the message, such as inline keyboards

    .. method:: sendLocation(chat_id, latitude, longitude, disable_notification=False, reply_to_message_id=None, reply_markup=None)

        Sends a location to the chat specified.

        :param int chat_id: Chat id of the target chat
        :param float latitude: Latitude of the location
        :param float longitude: Longitude of the location
        :param boolean disable_notification: Whether to disable the notification for the message
        :param int reply_to_message_id: The message id to make the message reply to
        :param dict reply_markup: The custom markup applied to the message, such as inline keyboards

    .. method:: sendVenue(chat_id, latitude, longitude, title, address, foursquare_id='', disable_notification=False, reply_to_message_id=None, reply_markup=None)

        Sends a venue to the chat specified.

        :param int chat_id: Chat id of the target chat
        :param float latitude: Latitude of the venue
        :param float longitude: Longitude of the venue
        :param str title: Name of the venue
        :param str address: Address of the venue
        :param str foursquare_id: Foursquare id of the venue
        :param boolean disable_notification: Whether to disable the notification for the message
        :param int reply_to_message_id: The message id to make the message reply to
        :param dict reply_markup: The custom markup applied to the message, such as inline keyboards

    .. method:: sendContact(chat_id, phone_number, first_name, last_name='', disable_notification=False, reply_to_message_id=None, reply_markup=None)

        Sends a contact to the chat specified.

        :param int chat_id: Chat id of the target chat
        :param str phone_number: Latitude of the contact
        :param str first_name: Longitude of the contact
        :param str last_name: Name of the contact
        :param boolean disable_notification: Whether to disable the notification for the message
        :param int reply_to_message_id: The message id to make the message reply to
        :param dict reply_markup: The custom markup applied to the message, such as inline keyboards

    .. method:: sendChatAction(chat_id, action)

        Sends the bot's current status to the chat.

        :param int chat_id: Chat id of the target chat
        :param ChatAction action: Type of action to broadcast

    .. method:: getUserProfilePhotos(user_id, offset=None, limit=None)

        Returns an array of profile photos from the target user

        :param int user_id: The user id of the target user
        :param int offset: The first photo to be returned
        :param int limit: The maximum number of photos to be retrieved

    .. method:: getFile(file_id)

        Gets simple file information to be downloaded from ``https://api.telegram.org/file/bot<token>/<file_path>``.

        :param str file_id: File identifier

    **Administrative Commands**

    .. method:: kickChatMember(chat_id, user_id, until_date=0)

        Kicks a chat member until the date specified or until unbanned.

        :param int chat_id: The id of the target chat
        :param int user_id: The id of the target user
        :param int until_date: The date in unix time that the user will be unbanned 

    .. method:: unbanChatMember(chat_id, user_id)

        Unbans a chat member from a chat.

        :param int chat_id: The id of the target chat
        :param int user_id: The id of the target user

    .. method:: restrictChatMember(chat_id, user_id, until_date=0, can_send_messages=True, can_send_media_messages=True, can_send_other_messages=True, can_add_web_page_previews=True)

        Restricts a chat member's permissions in a chat.

        :param int chat_id: The id of the target chat
        :param int user_id: The id of the target user
        :param int until_date: The date in unix time that the user will be unbanned
        :param boolean can_send_messages: Whether a user can send messages
        :param boolean can_send_media_messages: Whether a user can send media messages
        :param boolean can_send_other_messages: Whether a user can send other messages
        :param boolean can_add_web_page_previews: Whether a user can create web page previews

    .. method:: promoteChatMember(chat_id, user_id, can_change_info=False, can_post_messages=False, can_edit_messages=False, can_delete_messages=False, can_invite_users=False, can_restrict_members=False, can_pin_messages=False, can_promote_members=False)  

        Promotes a chat member

        :param int chat_id: The id of the target chat
        :param int user_id: The id of the target user
        :param boolean can_change_info: Whether a user can change group info
        :param boolean can_post_messages: Whether a user can make channel posts
        :param boolean can_edit_messages: Whether a user can edit other messages in a channel
        :param boolean can_delete_messages: Whether a user can delete other users' messages
        :param boolean can_invite_users: Whether a user can invite members to the group
        :param boolean can_restrict_members: Whether a user can restrict members in the group
        :param boolean can_pin_messages: Whether a user can pin messages
        :param boolean can_promote_members: Whether a user can promote users


    .. method:: leaveChat(chat_id)

        Makes the bot leave the target chat

        :param int chat_id: The id of the target chat

    .. method:: getChat(chat_id)

        Returns information on the target chat

        :param int chat_id: The id of the target chat

    .. method:: getChatAdministrators(chat_id)

        Returns list of administrators in the target chat

        :param int chat_id: The id of the target chat

    .. method:: getChatMembersCount(chat_id)

        Returns number of members in the target chat

        :param int chat_id: The id of the target chat

    .. method:: getChatMember(chat_id, user_id)

        Returns information on the target chat member

        :param int chat_id: The id of the target chat
        :param int user_id: The id of the target user

    .. method:: answerCallbackQuery(callback_query_id, text='', show_alert=False, url='', cache_time=None)

        Sends an answer to a callback query from an inline keyboard.

        :param str callback_query_id: Callback query id
        :param str text: Text for the notification
        :param boolean show_alert: Shows an alert instead of a notification
        :param str url: Url of game or to open bot with parameter
        :param str cache_time: Time to cache the query on the client

    .. method:: editMessageText(text, chat_id=None, message_id=None, inline_message_id=None, parse_mode=None, disable_web_page_preview=False, reply_markup=None)

        Edits a message from a chat.

        :param str text: New text for the message
        :param int chat_id: Chat id of the target chat
        :param int message_id: Message id in the target chat
        :param str inline_message_id: Inline message id in the target chat
        :param str parse_mode: `Markdown` or `HTML`, depending on which formatting style is preferred
        :param boolean disable_notification: Whether to disable the notification for the message
        :param dict reply_markup: The custom markup applied to the message, such as inline keyboards

    .. method:: editMessageCaption(chat_id=None, message_id=None, inline_message_id=None, caption=None, reply_markup=None)

        Edits a caption from a chat.

        :param int chat_id: Chat id of the target chat
        :param int message_id: Message id in the target chat
        :param str inline_message_id: Inline message id in the target chat
        :param str parse_mode: `Markdown` or `HTML`, depending on which formatting style is preferred
        :param dict reply_markup: The custom markup applied to the message, such as inline keyboards

    .. method:: editMessageReplyMarkup(chat_id=None, message_id=None, inline_message_id=None, reply_markup=None)

        Edits the reply markup on a message.

        :param int chat_id: Chat id of the target chat
        :param int message_id: Message id in the target chat
        :param str inline_message_id: Inline message id in the target chat
        :param dict reply_markup: The custom markup applied to the message, such as inline keyboards

    .. method:: deleteMessage(chat_id, message_id)

        Deletes a message from a chat.

        :param int chat_id: Chat id of the target chat
        :param int message_id: Message id in the target chat

    .. method:: answerInlineQuery(inline_query_id, results, cache_time=None, is_personal=False, next_offset='', switch_pm_text='', switch_pm_parameter='')

        Answers an inline query

        :param str inline_query_id: The id of the inline query
        :param results: The results to send to the user
        :param integer cache_time: The time to cache the results on the server
        :param boolean is_personal: Should results be cached server side only for that user
        :param str next_offset: Offset a client should send in the next query to recieve more results
        :param str switch_pm_text: Clients display button with specified text that switches to private chat
        :param str switch_pm_parameter: The parameter for the /start message sent when the button is pressed

    .. method:: sendInvoice(chat_id, title, description, payload, provider_token, start_parameter, currency, prices, photo_url='', photo_size=None, photo_height=None, photo_width=None, need_name=False, need_phone_number=False, need_email=False, need_shipping_address=False, is_flexible=False, disable_notification=False, reply_to_message_id=None, reply_markup=None)

        Sends an invoice to the user.

        :param int chat_id: Private chat id
        :param str title: Product name
        :param str description: Product description
        :param str payload: Invoice payload
        :param str provider_token: Payment token from BotFather
        :param str start_parameter: Deep linking parameter when used as a /start parameter
        :param str currency: Three letter `currency code`_
        :param list prices: Array of prices
        :param str photo_url: Product photo
        :param int photo_size: Photo size
        :param int photo_width: Photo width
        :param int photo_height: Photo height
        :param boolean need_name: Needs full name to complete order
        :param boolean need_phone_number: Needs phone number to complete order
        :param boolean need_email: Needs email to complete order
        :param boolean need_shipping_address: Needs shipping address to complete order
        :param boolean is_flexible: Final price depends on shipping method
        :param boolean disable_notification: Disable the notification
        :param int reply_to_message_id: Message id to reply to
        :param dict reply_markup: The inline keyboard applied to the message


    .. _currency code: https://core.telegram.org/bots/payments#supported-currencies

    .. method:: answerShippingQuery(shipping_query_id, ok, shipping_options=None, error_message='')

        If ``is_flexible`` and ``need_shipping_address`` are in the invoice, sends an update.

        :param str shipping_query_id: The shipping query id
        :param boolean ok: Is the address ok
        :param list shipping_options: Sends the shipping options
        :param str error_message: The error message to send to the user as a reason for the shipping to fail.

    .. method:: answerPreCheckoutQuery(pre_checkout_query_id, ok, error_message='')

        After shipping and payment details are confirmed, send a confirmation.

        :param str pre_checkout_query_id: The precheckout query id
        :param boolean ok: Is the order ok
        :param str error_message: The error message to send to the user as a reason for the order to fail.

    .. method:: sendGame(chat_id, game_short_name, disable_notification=False, reply_to_message_id=None, reply_markup=None)

        Sends a game to users in a chat.

        :param int chat_id: The id of the target chat
        :param str game_short_name: The id of the target chat
        :param boolean disable_notification: Disable the notification
        :param int reply_to_message_id: Message id to reply to
        :param dict reply_markup: The inline keyboard applied to the message

    .. method:: exportChatInviteLink(chat_id)

        Exports an invite link

        :param int chat_id: The id of the target chat

    .. method:: setChatPhoto(chat_id, photo)

        Sets the chat photo

        :param int chat_id: The id of the target chat
        :param file photo: The photo to set as the chat photo

    .. method:: deleteChatPhoto(chat_id)

        Deletes a chat photo

        :param int chat_id: The id of the target chat

    .. method:: setChatTitle(chat_id, title)

        Sets the chat title

        :param int chat_id: The id of the target chat
        :param str title: The text to set as the chat title

    .. method:: setChatDescription(chat_id, description)

        Sets the chat description

        :param int chat_id: The id of the target chat
        :param str description: The text to set as the chat description

    .. method:: pinChatMessage(chat_id, message_id, disable_notification=False)

        Sets the chat description

        :param int chat_id: The id of the target chat
        :param int message_id: The id of the target message
        :param boolean disable_notification: Disable the notification

    .. method:: unpinChatMessage(chat_id)

        Unpins the message in the target chat

        :param int chat_id: The id of the target chat

    .. method:: getStickerSet(name)

        Returns the sticker set with the name specified

        :param str name: The name of the sticker set

    .. method:: sendSticker(chat_id, sticker, disable_notification=False, reply_to_message_id=None, reply_markup=None)

    .. method:: uploadStickerFile(self)
    
        Uploads a new sticker

        :param int user_id: The user id of the sticker owner
        :param file png_sticker: The png file with at least one side of 512px

    .. method:: createNewStickerSet(user_id, name, title, png_sticker, emojis, contains_masks=False, mask_position=None)

        Uploads a new sticker

        :param int user_id: The user id of the sticker owner
        :param str name: The short name of the sticker set
        :param str title: The title of the sticker set
        :param file png_sticker: The png file with at least one side of 512px
        :param str emojis: Emoji to correspond to a sticker
        :param boolean contains_masks: Set of mask stickers should be created
        :param dict mask_position: Position of the mask

    .. method:: addStickerToSet(user_id, name, png_sticker, emojis, mask_position=None)

        Adds sticker to set

        :param int user_id: The user id of the sticker owner
        :param str name: The short name of the sticker set
        :param file png_sticker: The png file with at least one side of 512px
        :param str emojis: Emoji to correspond to a sticker
        :param dict mask_position: Position of the mask

    .. method:: setStickerPositionInSet(sticker, position)

        Moves sticker to position in the set

        :param str sticker: File id of sticker
        :param int position: New sticker position, zero-based

    .. method:: deleteStickerFromSet(sticker)

        Deletes sticker from set.

        :param str sticker: File id of sticker

.. class:: ChatAction(Enum)

    .. attribute:: TYPING
    .. attribute:: PHOTO
    .. attribute:: UVIDEO
    .. attribute:: RVIDEO
    .. attribute:: UAUDIO
    .. attribute:: RAUDIO
    .. attribute:: DOCUMENT
    .. attribute:: LOCATION
    .. attribute:: UVIDNOTE
    .. attribute:: RVIDNOTE


