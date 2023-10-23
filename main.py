import requests
import phonenumbers
import schedule
import time


def send_message():
    resp = requests.post('https://textbelt.com/text',{
        'phone': phonenumbers,
        'message': 'Hey, Good morning Wakeup',
        'key': 'textbelt'
    })
    print(resp.json())

schedule.every().day.at('06:00').do(send_message)


while True:
    schedule.run_pending()
    time.sleep(1)