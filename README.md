# vyper-bot
***

A telegram bot API library designed for Python 3.5. Works seamlessly with API v3.0 and will be updated as the bot API updates. This was created by [Josh](https://t.me/Floodie_Wowers). Make sure to send me a message on telegram if something doesn't work properly.

|   Contents   |
|--------------|
| [Installation](#Installation) |
|  [Setup](#Setup)  |
|     [Docs](#Documentation)     |

# Installation
***
To intall this library using pip, just run
```
pip3 install vyper-bot
```
To upgrade to a newer version, use 
```
pip3 install --upgrade vyper-bot
```


# Setup
***
Now that the module is downloaded and installed, create a new python file and put the following code in it, replacing the ```123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11``` with the bot token recieved from [@BotFather](https://t.me/BotFather).
```python
from vyper import vyper

bot = vyper.API().configure('123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11')
```
This is the most simple way to create a bot, but it won't run an update loop. However, you are able to run any of the bot API functions, such as [sendMessage()](###sendMessage). 
```python
from vyper import vyper

bot = vyper.API().configure('123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11')
bot.sendMessage(chat_id, 'This is a message that will be sent to the chat specified by the chat_id variable!', disable_notification=True)
```
If your replace `chat_id` with the chat ID of the group you want to send a message to, it will send the message that is in the second argument to that group. Since `disable_notification` is True, it will not send a notification to the people in that group telling them there's a new message.

In order to recieve messages, you must run the [getUpdates()](###getUpdates) function in a loop. The easiest way to do this is to use
```python
import time
while(True):
	bot.getUpdates()
    time.sleep(.05)
```
This will check for updates 20 times a second, which is far more than necessary, but will give very fast response times. In order for the messages to be handled, the configuration needs an extra argument, giving a function for every type of message that could be sent.

```python
def on_message(msg):
	# Put Message Handling Code Here

bot = vyper.API().configure('123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11', functions={'message':on_message})
```
This will pass the `on_message` function to the bot, so every time a message is received, it will run that function, passing the message as a parameter. From there, the program can handle each message as it is told to.

# Documentation
***
The following section is the documentation for each function available through the bot. It is separated by things from the Telegram Bot API, and specific things to vyper.
## Vyper Specific

### configure
|Parameters|Type|Required|Description|
|-|-|-|-|
|token|String|Yes|Sets the bot token to be used when making requests through the API. Necessary when creating the bot.|
|functions|Dictionary of functions for each type of message|No|Sets the function that gets called for each type of message the bot can recieve.|
|debug|Boolean|No|Not fully implemented yet. Will set program into debug mode so more values are printed out.|

## Bot API

### getMe
No parameters, returns User object with information about the bot.

### getUpdates
No parameters, gets updates from Telegram and runs the appropriate function, as setup by [configure()](###configure).

### sendMessage
|Parameters|Type|Required|Description|
|-|-|-|-|
|chat_id|Integer or String|Yes|A chat ID value as a number, or the chat username, such as @channelusername.|
|text|String|Yes|The text that is sent when the function is run.|
|parse_mode|String|No|The message parse mode, such as Markdown or HTML that applies formatting to the message in telegram.|
|disable_web_page_preview|Boolean|No|Tells telegram whether or not to display the preview of the webpage if there's a link present.|
|disable_notification|Boolean|No|Tells telegram whether or not to show a notification to group members when the message sends.|
|reply_to_message_id|Integer|No|The message ID that the sent message will be in reply to.|
|reply_markup|InlineKeyboardMarkup or ReplyKeyboardMarkup or ReplyKeyboardRemove or ForceReply|No|Dictionary of values used to give telegram information on additional items to add to the message, such as an inline keyboard.|

### forwardMessage
|Parameters|Type|Required|Description|
|-|-|-|-|
|chat_id|Integer or String|Yes|The chat ID that the message will be sent to.|
|from_chat_id|Integer or String|Yes|The chat ID that the message is coming from.|
|message_id|Integer|Yes|The message ID from the chat the message is coming from.|
|disable_notification|Boolean|No|Tells telegram whether or not to show a notification to group members when the message sends.|

### sendPhoto
|Parameters|Type|Required|Description|
|-|-|-|-|
|chat_id|Integer or String|Yes|A chat ID value as a number, or the chat username, such as @channelusername.|
|photo|Photo Object|Yes|The photo that will be sent. Open the file with mode 'rb' when passing the argument.|
|caption|String|No|The text that is attached when the photo sends.|
|disable_notification|Boolean|No|Tells telegram whether or not to show a notification to group members when the message sends.|
|reply_to_message_id|Integer|No|The message ID that the sent photo will be in reply to.|
|reply_markup|InlineKeyboardMarkup or ReplyKeyboardMarkup or ReplyKeyboardRemove or ForceReply|No|Dictionary of values used to give telegram information on additional items to add to the message, such as an inline keyboard.|

### sendAudio
|Parameters|Type|Required|Description|
|-|-|-|-|
|chat_id|Integer or String|Yes|A chat ID value as a number, or the chat username, such as @channelusername.|
|audio|Audio Binary Object|Yes|The audio file that will be sent. Open the file with mode 'rb' when passing the argument.|
|caption|String|No|The text that is attached when the audio sends.|
|duration|Integer|No|The duration of the audio clip in seconds|
|performer|String|No|Performer|
|title|String|No|Title|
|disable_notification|Boolean|No|Tells telegram whether or not to show a notification to group members when the message sends.|
|reply_to_message_id|Integer|No|The message ID that the sent photo will be in reply to.|
|reply_markup|InlineKeyboardMarkup or ReplyKeyboardMarkup or ReplyKeyboardRemove or ForceReply|No|Dictionary of values used to give telegram information on additional items to add to the message, such as an inline keyboard.|

### sendDocument
|Parameters|Type|Required|Description|
|-|-|-|-|
|chat_id|Integer or String|Yes|A chat ID value as a number, or the chat username, such as @channelusername.|
|document|File Object|Yes|The file that will be sent. Open the file with mode 'rb' when passing the argument.|
|caption|String|No|The text that is attached when the document sends.|
|disable_notification|Boolean|No|Tells telegram whether or not to show a notification to group members when the message sends.|
|reply_to_message_id|Integer|No|The message ID that the sent photo will be in reply to.|
|reply_markup|InlineKeyboardMarkup or ReplyKeyboardMarkup or ReplyKeyboardRemove or ForceReply|No|Dictionary of values used to give telegram information on additional items to add to the message, such as an inline keyboard.|

### sendSticker
|Parameters|Type|Required|Description|
|-|-|-|-|
|chat_id|Integer or String|Yes|A chat ID value as a number, or the chat username, such as @channelusername.|
|sticker|Photo Object|Yes|The sticker that will be sent. Open the file with mode 'rb' when passing the argument. File must be a .webp format.|
|disable_notification|Boolean|No|Tells telegram whether or not to show a notification to group members when the message sends.|
|reply_to_message_id|Integer|No|The message ID that the sent photo will be in reply to.|
|reply_markup|InlineKeyboardMarkup or ReplyKeyboardMarkup or ReplyKeyboardRemove or ForceReply|No|Dictionary of values used to give telegram information on additional items to add to the message, such as an inline keyboard.|

### sendVideo
|Parameters|Type|Required|Description|
|-|-|-|-|
|chat_id|Integer or String|Yes|A chat ID value as a number, or the chat username, such as @channelusername.|
|video|Video Object|Yes|The video that will be sent. Open the file with mode 'rb' when passing the argument.|
|duration|Integer|No|The length of the video in seconds|
|width|Integer|No|Video Width|
|height|Integer|No|Video Height|
|caption|String|No|The text that is attached when the video sends.|
|disable_notification|Boolean|No|Tells telegram whether or not to show a notification to group members when the message sends.|
|reply_to_message_id|Integer|No|The message ID that the sent photo will be in reply to.|
|reply_markup|InlineKeyboardMarkup or ReplyKeyboardMarkup or ReplyKeyboardRemove or ForceReply|No|Dictionary of values used to give telegram information on additional items to add to the message, such as an inline keyboard|

### sendVoice
|Parameters|Type|Required|Description|
|-|-|-|-|
|chat_id|Integer or String|Yes|A chat ID value as a number, or the chat username, such as @channelusername.|
|audio|Audio Binary Object|Yes|The audio file that will be sent. Open the file with mode 'rb' when passing the argument. Must be in .ogg format|
|caption|String|No|The text that is attached when the audio sends.|
|duration|Integer|No|The duration of the audio clip in seconds|
|disable_notification|Boolean|No|Tells telegram whether or not to show a notification to group members when the message sends.|
|reply_to_message_id|Integer|No|The message ID that the sent photo will be in reply to.|
|reply_markup|InlineKeyboardMarkup or ReplyKeyboardMarkup or ReplyKeyboardRemove or ForceReply|No|Dictionary of values used to give telegram information on additional items to add to the message, such as an inline keyboard.|

### sendVideoNote
|Parameters|Type|Required|Description|
|-|-|-|-|
|chat_id|Integer or String|Yes|A chat ID value as a number, or the chat username, such as @channelusername.|
|video_note|Video Object|Yes|The video file that will be sent. Open the file with mode 'rb' when passing the argument.|
|length|Integer|No|The size of the video.|
|duration|Integer|No|The duration of the audio clip in seconds|
|disable_notification|Boolean|No|Tells telegram whether or not to show a notification to group members when the message sends.|
|reply_to_message_id|Integer|No|The message ID that the sent photo will be in reply to.|
|reply_markup|InlineKeyboardMarkup or ReplyKeyboardMarkup or ReplyKeyboardRemove or ForceReply|No|Dictionary of values used to give telegram information on additional items to add to the message, such as an inline keyboard.|

### sendLocation
|Parameters|Type|Required|Description|
|-|-|-|-|
|chat_id|Integer or String|Yes|A chat ID value as a number, or the chat username, such as @channelusername.|
|latitude|Float Value|Yes|The latitude of the position|
|longitude|Float Value|Yes|The longitude of the position|
|disable_notification|Boolean|No|Tells telegram whether or not to show a notification to group members when the message sends.|
|reply_to_message_id|Integer|No|The message ID that the sent photo will be in reply to.|
|reply_markup|InlineKeyboardMarkup or ReplyKeyboardMarkup or ReplyKeyboardRemove or ForceReply|No|Dictionary of values used to give telegram information on additional items to add to the message, such as an inline keyboard.|

### sendVenue
|Parameters|Type|Required|Description|
|-|-|-|-|
|chat_id|Integer or String|Yes|A chat ID value as a number, or the chat username, such as @channelusername.|
|latitude|Float Value|Yes|The latitude of the position.|
|longitude|Float Value|Yes|The longitude of the position.|
|title|String|Yes|The title of the venue.|
|address|String|Yes|The address of the venue.|
|disable_notification|Boolean|No|Tells telegram whether or not to show a notification to group members when the message sends.|
|reply_to_message_id|Integer|No|The message ID that the sent photo will be in reply to.|
|reply_markup|InlineKeyboardMarkup or ReplyKeyboardMarkup or ReplyKeyboardRemove or ForceReply|No|Dictionary of values used to give telegram information on additional items to add to the message, such as an inline keyboard.|

### sendContact
|Parameters|Type|Required|Description|
|-|-|-|-|
|chat_id|Integer or String|Yes|A chat ID value as a number, or the chat username, such as @channelusername.|
|phone_number|String|Yes|The phone number of the contact.|
|first_name|String|Yes|The first name of the contact.|
|last_name|String|Yes|The last name of the contact.|
|disable_notification|Boolean|No|Tells telegram whether or not to show a notification to group members when the message sends.|
|reply_to_message_id|Integer|No|The message ID that the sent photo will be in reply to.|
|reply_markup|InlineKeyboardMarkup or ReplyKeyboardMarkup or ReplyKeyboardRemove or ForceReply|No|Dictionary of values used to give telegram information on additional items to add to the message, such as an inline keyboard.|

### sendChatAction
|Parameters|Type|Required|Description|
|-|-|-|-|
|chat_id|Integer or String|Yes|A chat ID value as a number, or the chat username, such as @channelusername.|
|action|String or ChatAction|Yes|The action that is sent to the chat.|

### getUserProfilePhotos
|Parameters|Type|Required|Description|
|-|-|-|-|
|user_id|Integer|Yes|User ID to get pictures from.|
|offset|Integer|No|Sequential number of the first photo to be returned. By default, all photos are returned.|
|limit|Integer|No|Limits the number of photos to be retrieved. Values between 1—100 are accepted. Defaults to 100.|

### getFile
|Parameters|Type|Required|Description|
|-|-|-|-|
|file_id|Integer|Yes|The file ID stored on the telegram servers.|

### kickChatMember
|Parameters|Type|Required|Description|
|-|-|-|-|
|chat_id|Integer or String|Yes|A chat ID value as a number, or the chat username, such as @channelusername.|
|user_id|Integer|Yes|User ID to kick from group.|

### unbanChatMember
|Parameters|Type|Required|Description|
|-|-|-|-|
|chat_id|Integer or String|Yes|A chat ID value as a number, or the chat username, such as @channelusername.|
|user_id|Integer|Yes|User ID to unban from group.|

### leaveChat
|Parameters|Type|Required|Description|
|-|-|-|-|
|chat_id|Integer or String|Yes|A chat ID value as a number, or the chat username, such as @channelusername.|

### getChat
|Parameters|Type|Required|Description|
|-|-|-|-|
|chat_id|Integer or String|Yes|A chat ID value as a number, or the chat username, such as @channelusername.|

### getChatAdministrators
|Parameters|Type|Required|Description|
|-|-|-|-|
|chat_id|Integer or String|Yes|A chat ID value as a number, or the chat username, such as @channelusername.|

### getChatMembersCount
|Parameters|Type|Required|Description|
|-|-|-|-|
|chat_id|Integer or String|Yes|A chat ID value as a number, or the chat username, such as @channelusername.|

### getChatMember
|Parameters|Type|Required|Description|
|-|-|-|-|
|chat_id|Integer or String|Yes|A chat ID value as a number, or the chat username, such as @channelusername.|
|user_id|Integer|Yes|User ID to return information on.|

### answerCallbackQuery
|Parameters|Type|Required|Description|
|-|-|-|-|
|callback_query_id|Integer|Yes|The ID of the specific callback query.|
|text|String|No|The text shown on the answer of the callback query.|
|show_alert|Boolean|No|If true, an alert will be shown by the client instead of a notification at the top of the chat screen. Defaults to false.|
|url|String|No|URL that will be opened by the user's client. If you have created a Game and accepted the conditions via @Botfather, specify the URL that opens your game – note that this will only work if the query comes from a callback_game button. Otherwise, you may use links like `telegram.me/your_bot?start=XXXX` that open your bot with a parameter.|
|cache_time|Integer|No|The maximum amount of time in seconds that the result of the callback query may be cached client-side. Telegram apps will support caching starting in version 3.14. Defaults to 0.|

### editMessageText
|Parameters|Type|Required|Description|
|-|-|-|-|
|||||

### editMessageCaption
|Parameters|Type|Required|Description|
|-|-|-|-|
|||||

### editMessageReplyMarkup
|Parameters|Type|Required|Description|
|-|-|-|-|
|||||

### deleteMessage
|Parameters|Type|Required|Description|
|-|-|-|-|
|||||

### answerInlineQuery
|Parameters|Type|Required|Description|
|-|-|-|-|
|||||

### sendInvoice
|Parameters|Type|Required|Description|
|-|-|-|-|
|||||

### answerShippingQuery
|Parameters|Type|Required|Description|
|-|-|-|-|
|||||

### answerPreCheckoutQuery
|Parameters|Type|Required|Description|
|-|-|-|-|
|||||

### sendGame
|Parameters|Type|Required|Description|
|-|-|-|-|
|||||


