import requests

# اطلاعات شما
TELEGRAM_TOKEN = "8551688721:AAHyFlOL5WZYjgAuswz81X_SCi898k1DOUM"
CHAT_ID = "@jdkdjjdjkf"

def send_to_telegram(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    # گرفتن فقط چند خط اول برای تست
    lines = [line for line in text.split('\n') if line.strip()][:5]
    top_configs = "\n\n".join(lines)
    
    message = f"✅ **تست نهایی ربات:**\n\n{top_configs}"
    payload = {"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}
    
    response = requests.post(url, data=payload)
    
    # چاپ وضعیت در کنسول گیت‌هاب برای عیب‌یابی
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")

def fetch_configs():
    # لینک‌های تست
    url = "https://raw.githubusercontent.com/yebekhe/TelegramV2rayCollector/main/sub/base64/mix"
    try:
        response = requests.get(url, timeout=15)
        if response.status_code == 200:
            send_to_telegram(response.text)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    fetch_configs()
