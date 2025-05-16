# ⚡️ Api-ChatGPT ⚡️  
A simple and free web service for interacting with ChatGPT  
Built with ❤️ using Python

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Web_Framework-lightgrey?logo=flask)
![License](https://img.shields.io/badge/Free-Yes-brightgreen?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-blue)

---

## 🚀 Features

- Free to use, no authentication required  
- Lightweight and fast  
- Easy to deploy  
- Written in pure Python

---

## 📚 Libraries Used

- `flask` – Web framework  
- `requests` – For making HTTP requests  
- `json` – Built-in JSON handling  
- `random` – Built-in random utilities

---

## ⚠️ Warning

If you experience request **limits** or get **rate-limited** by the upstream service:
- Change your **proxies**
- Or add **multiple proxy options** in your setup

Using **rotating proxies** is recommended for stability in heavy use cases.

---

## 📦 Installation

bash
git clone https://github.com/your-username/Api-ChatGPT.git
cd Api-ChatGPT
pip install -r requirements.txt
python app.py

> Make sure you have **Python 3.10+** installed.

---

## 💡 API Endpoint

**POST** `/chat`

**Request Body:**
```
json
{
  "user_id": 1,
  "message": "Hi, how are you?"
}
```
---

## 🧪 Code Examples

### Python
```
python
import requests

url = "http://localhost:5000/chat"
data = {
    "user_id": 1,
    "message": "Hi, how are you?"
}

response = requests.post(url, json=data)
print(response.json())
```
### curl
```
bash
curl -X POST http://localhost:5000/chat \
-H "Content-Type: application/json" \
-d '{"user_id": 1, "message": "Hi, how are you?"}'
```
---

## 🤝 Contribute

Feel free to fork the repo, create a pull request, or open an issue!

---

## 📬 Contact

For questions or feedback, open an issue or reach out on GitHub.

---

### Made with passion & Python
