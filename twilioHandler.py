from twilio.rest import Client
import config

def sendText(tweet, to_phone_number):
    client = Client(config.account_sid, config.auth_token)
    message = client.messages.create(
        to=to_phone_number,
        from_=config.phone_number,
        body=tweet)
    print(message)
