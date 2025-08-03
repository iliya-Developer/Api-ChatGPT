#!/bin/bash

BLUE='\033[0;34m'
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'

apt-get update -qq
apt-get install -y tor

TOR_PASSWORD=$(openssl rand -base64 16)
HASHED_PASSWORD=$(tor --hash-password "$TOR_PASSWORD" | tail -1)

cp /etc/tor/torrc /etc/tor/torrc.bak
cat > /etc/tor/torrc <<EOL
SocksPort 9050
ControlPort 9051
HashedControlPassword $HASHED_PASSWORD
DataDirectory /var/lib/tor
User debian-tor
Group debian-tor
EOL

systemctl restart tor
systemctl enable tor

sleep 5
if systemctl is-active --quiet tor; then
    echo -e "${GREEN}# Tor service started successfully${NC}"
else
    echo -e "${RED}# Failed to start Tor service${NC}"
    exit 1
fi

apt-get install -y python3 python3-pip git

mkdir -p /opt/chatgpt-web
cd /opt/chatgpt-web

git clone https://github.com/ishadow-dev/Api-Chatgpt.git
cd Api-Chatgpt/API-GPT
pip install -r requirements.txt

sed -i "s/TOR_PASSWORD = \"your_tor_password\"/TOR_PASSWORD = \"$TOR_PASSWORD\"/" main.py


cat > /etc/systemd/system/chatgpt-web.service <<EOL
[Unit]
Description=ChatGPT WebService
After=network.target tor.service

[Service]
User=root
WorkingDirectory=/opt/chatgpt-web/Api-Chatgpt/API-GPT
ExecStart=/usr/bin/python3 main.py
Restart=always

[Install]
WantedBy=multi-user.target
EOL

systemctl daemon-reload
systemctl enable chatgpt-web
systemctl start chatgpt-web

sleep 3
if systemctl is-active --quiet chatgpt-web; then
    echo -e "${GREEN}# Application started successfully${NC}"
else
    echo -e "${RED}# Failed to start application${NC}"
    systemctl status chatgpt-web
    exit 1
fi

echo -e "${GREEN}# Installation completed successfully${NC}"
echo -e "${BLUE}# Tor password: ${NC}$TOR_PASSWORD"
echo -e "${BLUE}# Application URL: ${NC}http://localhost:8000"
echo -e "${BLUE}# Service status: ${NC}systemctl status chatgpt-web"
echo -e "${BLUE}# View logs: ${NC}journalctl -u chatgpt-web -f"
echo -e "${BLUE}# Test with: ${NC}curl -X POST -H 'Content-Type: application/json' -d '{\"user_id\":\"test\",\"message\":\"Hello\"}' http://localhost:8000/chat"