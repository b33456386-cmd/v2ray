import requests

# اطلاعات شما
TELEGRAM_TOKEN = "8551688721:AAHyFlOL5WZYjgAuswz81X_SCi898k1DOUM"
CHAT_ID = "@jdkdjjdjkf"

sources = [
    "https://raw.githubusercontent.com/yebekhe/TelegramV2rayCollector/main/sub/base64/mix",
    "https://raw.githubusercontent.com/Mahdi0024/ProxyCollector/master/sub/v2ray.txt"
]

def send_to_telegram(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    lines = [line for line in text.split('\n') if line.strip()]
    top_configs = "\n\n".join(lines[:10]) 
    message = f"🚀 **کانفیگ‌های جدید:**\n\n{top_configs}"
    payload = {"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}
    requests.post(url, data=payload)

def fetch_configs():
    all_configs = ""
    for url in sources:
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                all_configs += response.text + "\n"
        except:
            pass
    if all_configs:
        send_to_telegram(all_configs)

if __name__ == "__main__":
    fetch_configs()
