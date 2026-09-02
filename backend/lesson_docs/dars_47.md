# 🚀 47. Webhook Integratsiyasi va Serverga Deploy Qilish — Dars dokumentatsiyasi

Botni sinovdan o'tkazgach, uni kompyuter o'chiq bo'lsa ham 24/7 ishlashi uchun **VPS Serverga (Linux)** joylashtirish va **Systemd Service** sifatida sozlash kerak.

---

## Linux Systemd Service Fayli Misoli (/etc/systemd/system/mybot.service)

```ini
[Unit]
Description=Aiogram 3 Telegram Bot Service
After=network.target

[Service]
User=root
WorkingDirectory=/root/mybot
ExecStart=/root/mybot/venv/bin/python main.py
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

Keyingi **48-dars: 4-Modul Imtihoni va To'liq Aiogram Bot Loyihasi** da 12 ta darsda o'rganilgan bilimlar bo'yicha yakuniy loyihani bajaramiz.
