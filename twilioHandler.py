from twilio.rest import Client
import config

def sendText(tweet, to_phone_number):
    client = Client(config.account_sid, config.auth_token)
    message = client.messages.create(
        to=to_phone_number,
        from_=config.phone_number,
        body=tweet)
    print(message)

# from each retweet, set example_message = message details
# send messages to church and non-registered phone numbers
def send_to_multiple(phone_numbers, message):
    for phone_number in phone_numbers:
        sendText(message, phone_number)
