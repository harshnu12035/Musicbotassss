# VC Mic Booster Userbot

Real-time voice boost for Telegram VC (150-200dB)

## Setup
1. Get SESSION from: `https://my.telegram.org`
2. Edit `config.py` or `.env`
3. `docker-compose up -d`

## Commands
- `.boost 123456789` - Boost specific user
- `.unboost 123456789` - Stop boost
- `.status` - Check status

- ## VPS DEVELOPMENT GUIDE
- # 1. Clone & Setup
git clone YOUR_GITHUB_REPO_URL
cd vc-mic-booster

# 2. Edit config
nano config.py  # Add SESSION, API_ID, API_HASH

# 3. Docker Install
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh
systemctl start docker

# 4. Deploy
docker-compose up -d

# 5. Check
docker ps
docker logs vc-mic-booster
