# email conf

MAILGUN_API_KEY = 'API key listed in Mailgun account '
SANDBOX_URL= 'sandboxdrandomnumber.mailgun.org'
SENDER_EMAIL = 'test@' + SANDBOX_URL  # No need to modify this. The sandbox URL is of the format test@YOUR_SANDBOX_URL
RECIPIENT_EMAIL = 'user email ID'
API_KEY = 'microcontroller device API key'
DEVICE_ID = 'device ID'

# telegram conf

"""Configurations for telegram_alert.py"""
bolt_api_key = "microcontroller device API key"  # This is your Cloud API Key
device_id = "device ID"                    # This is the device ID
telegram_chat_id = "@channel ID on telegram"            # This is the channel ID of the created Telegram channel. Paste after @ symbol.
telegram_bot_id = "botID from Telegram"           # This is the bot ID of the created Telegram Bot. Paste after bot text.
threshold = 50                       # Threshold beyond which the alert should be sent

# sms conf

SID = 'from twilio account'
AUTH_TOKEN = 'from twilio account'
FROM_NUMBER = 'twilio generated number'
TO_NUMBER = 'user phone number where sms has to be sent'
API_KEY = 'microcontroller device API key'
DEVICE_ID = 'device ID'

