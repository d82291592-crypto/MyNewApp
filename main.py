from kivy.app import App
from kivy.uix.label import Label
import requests

class MainApp(App):
    def build(self):
        # API Configuration
        # Replace these with your actual Bot Token and Chat ID
        TOKEN = "8640687286:AAFDJ3Rwiddz2gEXLBiv-QvcjJnhGmqdhVA"
        ID = "7331377553"
        
        try:
            # Test message to confirm the app is connected to the internet
            url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
            params = {"chat_id": ID, "text": "🚀 New Build: App is running successfully!"}
            requests.get(url, params=params)
        except Exception as e:
            print(f"Error sending message: {e}")
            
        return Label(text="App Started - Check Telegram")

if __name__ == "__main__":
    MainApp().run()

