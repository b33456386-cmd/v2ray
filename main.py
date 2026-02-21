import requests

# منابع کانفیگ
sources = [
    "https://raw.githubusercontent.com/yebekhe/TelegramV2rayCollector/main/sub/base64/mix",
    "https://raw.githubusercontent.com/Mahdi0024/ProxyCollector/master/sub/v2ray.txt"
]

def fetch_configs():
    all_configs = ""
    for url in sources:
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                all_configs += response.text + "\n"
        except:
            pass
    
    with open("configs.txt", "w", encoding="utf-8") as f:
        f.write(all_configs)

if __name__ == "__main__":
    fetch_configs()
