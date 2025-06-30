import requests
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="/Users/lulualmogbil/python-bootcamp/Yaqeth-UNIT-PROJECT-1/.env")

token = os.getenv("TOKEN")
chat_id = int(os.getenv("CHAT_ID")) 


def send_alert(msg):
    print(f"Alert Test:  {msg}")
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": msg
    }
    
    try:
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            print("Telegram alert sent successfully to the Doctor")
        else:
            print(f"Failed to send alert. Status: {response.status_code}")
            
    except Exception as e:
        print(f"Error sending Telegram alert: {e}")



