import requests
from twilio.rest import Client
import time


url = 'https://api.kraken.com/0/public/Ticker?pair=ETHUSD'

while 1:

    # First Price
    coinResponse1 = requests.get(url, timeout=10)

    coinJson1 = coinResponse1.json()

    price1 = float(coinJson1['result']['XETHZUSD']['c'][0])  

    # Time Delay for Price Change
    time.sleep(60)

    # Second Price    
    coinResponse2 = requests.get(url, timeout=10)

    coinJson2 = coinResponse2.json()

    price2 = float(coinJson2['result']['XETHZUSD']['c'][0])    

    priceDelta = price2-price1     

    # Text Message info
    coinText1 = 'ETHUSD1'
    coinText2 = 'ETHUSD2'

    if priceDelta >= 5.0 or priceDelta <= -3.0: 
        account_sid = '<TWILIO_ACCOUNT_SID>'
        auth_token = '<TWILIO_AUTH_TOKEN>'  
        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
                body=str(priceDelta) + '\n\n' + coinText1 + ' - ' + str(price1) + '\n' + coinText2 + ' - ' + str(price2),
                from_='<SENDER_PHONE_NUMBER>',
                to='<RECEIVER_PHONE_NUMBER>'
            )

        print(message.sid)