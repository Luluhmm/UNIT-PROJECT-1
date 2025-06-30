import requests

token = '8047687045:AAFdbN6MFUZzlV2_tVsQpxFchNoLYstrI7A'
id = '1242534913'



def send_alert(msg):
    print(f"Alert Test:  {msg}")
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": id,
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



