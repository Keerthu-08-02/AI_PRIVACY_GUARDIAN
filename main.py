from detection import detect_screen_capture
from alerts import send_alert

def main():
    print("🛡️ AI Privacy Guardian Running...")
    if detect_screen_capture():
        send_alert()

if __name__ == "__main__":
    main()
