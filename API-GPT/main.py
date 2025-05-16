from flask import Flask, request, jsonify
import requests as req
import random
import json

app = Flask(__name__)

user_histories = {}

proxies = [
    # Format 1: ip:port:username:password
    "198.23.239.134:6540:ijkhwzwk:ze5ym8dkas73",
    "207.244.217.165:6712:ijkhwzwk:ze5ym8dkas73",
    "107.172.163.27:6543:ijkhwzwk:ze5ym8dkas73",
    "64.137.42.112:5157:ijkhwzwk:ze5ym8dkas73",
    "173.211.0.148:6641:ijkhwzwk:ze5ym8dkas73",
    "216.10.27.159:6837:ijkhwzwk:ze5ym8dkas73",
    "154.36.110.199:6853:ijkhwzwk:ze5ym8dkas73",
    "45.151.162.198:6600:ijkhwzwk:ze5ym8dkas73",
    "188.74.210.21:6100:ijkhwzwk:ze5ym8dkas73",
    
    # Format 2: username:password:host:port
    
    # Format 3: ip:port
    
]

def get_random_proxy():
    proxy = random.choice(proxies)
    parts = proxy.split(':')
    
    if len(parts) == 2:
        # Format 3: ip:port
        ip, port = parts
        proxy_url = f"http://{ip}:{port}"
    elif len(parts) == 4:
        if parts[2].endswith('.pyproxy.io'):
            # Format 2: username:password:host:port
            username, password, host, port = parts
            proxy_url = f"http://{username}:{password}@{host}:{port}"
        else:
            # Format 1: ip:port:username:password
            ip, port, username, password = parts
            proxy_url = f"http://{username}:{password}@{ip}:{port}"
    else:
        raise ValueError("فرمت پروکسی نامعتبر است")
        
    return {'http': proxy_url, 'https': proxy_url}

def ask_gpt(message, history):
    try:
        api = "https://gpt.lovetoome.com/api/openai/v1/chat/completions"
        
        history.append({"role": "user", "content": message})
        trimmed_history = history[-7:]
        payload = {
            "messages": [
                {
                    "role": msg["role"],
                    "content": msg["content"],
                    "parts": [
                        {"type": "text", "text": msg["content"]}
                    ]
                }
                for msg in history
            ],
            "stream": True,
            "model": "gpt-4o-mini",
            "temperature": 0.5,
            "presence_penalty": 0,
            "frequency_penalty": 0,
            "top_p": 1,
            "key": "123dfnbjds%!@%123DSasda"
        }

        headers = {
            "Accept": "application/json, text/event-stream",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "en-US,en;q=0.9",
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
            "Origin": "https://gpt.lovetoome.com",
            "Referer": "https://gpt.lovetoome.com/",
            "Cookie": '_ga=GA1.1.1956560479.1747133170; FCCDCF=%5Bnull%2Cnull%2Cnull%2C%5B%22CQRWXMAQRWXMAEsACBENBqFoAP_gAEPgAARoINJD7C7FbSFCyD5zaLsAMAhHRsAAQoQAAASBAmABQAKQIAQCgkAYFASgBAACAAAAICRBIQIECAAAAUAAQAAAAAAEAAAAAAAIIAAAgAEAAAAIAAACAIAAEAAIAAAAEAAAmAgAAIIACAAAgAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAQNVSD2F2K2kKFkHCmwXYAYBCujYAAhQgAAAkCBMACgAUgQAgFJIAgCIFAAAAAAAAAQEiCQAAQABAAAIACgAAAAAAIAAAAAAAQQAABAAIAAAAAAAAEAQAAIAAQAAAAIAABEhAAAQQAEAAAAAAAQAAA%22%2C%222~70.89.93.108.122.149.184.196.236.259.311.313.314.323.358.415.442.486.494.495.540.574.609.864.981.1029.1048.1051.1095.1097.1126.1205.1276.1301.1365.1415.1449.1514.1570.1577.1598.1651.1716.1735.1753.1765.1870.1878.1889.1958.1960.2072.2253.2299.2373.2415.2506.2526.2531.2568.2571.2575.2624.2677.2778~dv.%22%2C%22D3F47E04-C383-4F59-BA10-E3B5162C6A3C%22%5D%5D; _clck=yk8zp5%7C2%7Cfvw%7C0%7C1959; _ga_TT172QJHGK=GS2.1.s1747393668$o10$g1$t1747393669$j0$l0$h0; _ga_89WN60ZK2E=GS2.1.s1747393668$o10$g1$t1747393669$j0$l0$h0; FCNEC=%5B%5B%22AKsRol-WtXraDX2-rxoAZrfhhu5kdKzR1_9JtfjwL-plCWbVieTeo_zrt_ATw2QrJtDXWl0-s0IXv0jyre3LctpnveeSq4b0DuPzZyql4I3bqoap0DbjoS1cv1btqs0lqEDt8m06BgWt7BvSa-tidQD560mp4LyPMg%3D%3D%22%5D%5D; __gads=ID=4902d0b371c02e51:T=1747133174:RT=1747393672:S=ALNI_MYOOIjJ3qGn564UVeNWS2Bi5C4c6A; __gpi=UID=000010abf2094f44:T=1747133174:RT=1747393672:S=ALNI_MZX2J4CZ8DMWBbP472aH5uFgEo31g; __eoi=ID=92dfc2f19ef6bf55:T=1747133174:RT=1747393672:S=AA-AfjaKj2zZmjFjQyhL5CI2gWCy'
        }

        proxy = get_random_proxy()
        print(f"Using proxy: {proxy['http']}")

        try:
            response = req.post(api, headers=headers, json=payload, stream=True, proxies=proxy, timeout=30)
            answer = ""
            for line in response.iter_lines():
                if line:
                    try:
                        decoded_line = line.decode('utf-8')
                        if decoded_line.startswith("data: "):
                            data = decoded_line[6:]
                            if data == "[DONE]":
                                break
                            try:
                                obj = json.loads(data)
                                delta = obj.get("choices", [{}])[0].get("delta", {})
                                content = delta.get("content")
                                if content:
                                    answer += content
                            except Exception:
                                pass
                        else:
                            answer += decoded_line
                    except Exception:
                        pass
            trimmed_history.append({"role": "assistant", "content": answer})
            return answer, trimmed_history
        except Exception as e:
            print(f"Error in API request: {str(e)}")
            return "Sorry, there was a problem connecting to the server", history

    except Exception as e:
        print(f"Error in ask_gpt: {str(e)}")
        return "Sorry, there was a problem processing your request", history

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_id = data.get('user_id')
        message = data.get('message')
        if not user_id or not message:
            return jsonify({'error': 'user_id and message required'}), 400

        history = user_histories.get(user_id, [])
        answer, new_history = ask_gpt(message, history)
        user_histories[user_id] = new_history

        return jsonify({'result': answer}), 200
    except Exception as e:
        print(f"Error in chat endpoint: {str(e)}")
        return jsonify({'result': "Sorry, something went wrong"}), 200

@app.route('/')
def index():
    return jsonify({"result" : 'Flask is working!'}), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)