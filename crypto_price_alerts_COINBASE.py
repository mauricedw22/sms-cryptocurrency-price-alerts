import requests
from twilio.rest import Client
import time

url = 'https://api.coinbase.com/v2/prices/XLM-USD/buy'

while 1:
    # First Price Ratio
    coinJson = requests.get(url, timeout=10)

    coinResponse = coinJson.json()

    xlmPrice = float(coinResponse['data']['amount'])   

    # Time Delay for Price Change
    time.sleep(30)  

    # SMS message sent when XLM price drops below 0.30 or rises above 0.33
    if xlmPrice >= 0.30 or xlmPrice <= 0.33: 
        account_sid = '<TWILIO_ACCOUNT_SID>'
        auth_token = '<TWILIO_AUTH_TOKEN>'   
        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
                body='\n XLM Price - ' + str(xlmPrice),
                from_='<SENDER_PHONE_NUMBER>',
                to='<RECEIVER_PHONE_NUMBER>'
            )

        print(message.sid)