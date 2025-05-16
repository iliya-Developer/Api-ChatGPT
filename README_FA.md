# ⚡️ Api-ChatGPT ⚡️  
یک وب‌سرویس ساده و رایگان برای ارتباط با ChatGPT  
ساخته‌شده با ❤️ و پایتون

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Web_Framework-lightgrey?logo=flask)
![License](https://img.shields.io/badge/Free-Yes-brightgreen?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-blue)

---

نسخه انگلیسی را از [اینجا مشاهده کنید](README.md)

---

## 🚀 ویژگی‌ها

- رایگان و بدون نیاز به احراز هویت  
- سبک و سریع  
- نصب و اجرا آسان  
- نوشته‌شده با پایتون خالص

---

## 📚 کتابخانه‌های استفاده‌شده

- flask – فریم‌ورک وب  
- requests – برای ارسال درخواست‌های HTTP  
- json – مدیریت داده‌های JSON داخلی  
- random – توابع تصادفی داخلی

---

## ⚠️ هشدار

اگر با محدودیت درخواست از سرویس اصلی مواجه شدید:

- پروکسی‌های خود را تغییر دهید  
- یا چندین گزینه پروکسی به تنظیمات خود اضافه کنید

استفاده از پروکسی‌های چرخشی (rotating proxies) برای ثبات بیشتر در استفاده‌های سنگین توصیه می‌شود.

---

## 📦 نصب
```
git clone https://github.com/your-username/Api-ChatGPT.git
cd Api-ChatGPT
pip install -r requirements.txt
python app.py
```
> اطمینان حاصل کنید که Python نسخه 3.09 یا بالاتر را نصب کرده‌اید.

---

## 💡 اندپوینت API
```
POST /chat
```
### بدنه درخواست (JSON):
```
{
  "user_id": 1,
  "message": "سلام، حالت چطوره؟"
}
```
---

## 🧪 نمونه کد

### پایتون
```
import requests

url = "http://localhost:5000/chat"
data = {
    "user_id": 1,
    "message": "سلام، حالت چطوره؟"
}

response = requests.post(url, json=data)
print(response.json())
```
### curl

curl -X POST http://localhost:5000/chat \
-H "Content-Type: application/json" \
-d '{"user_id": 1, "message": "سلام، حالت چطوره؟"}'
---

## 📬 ارتباط
http://shadowpw.com/contact


---

### ساخته‌شده با عشق و پایتون
