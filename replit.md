# BanhammerMarie Telegram Bot

A modular Telegram group management bot built in Python 3 using the python-telegram-bot library.

## Features
- Admin tools (ban, kick, mute, warn, etc.)
- Anti-flood protection
- Blacklisting
- Custom filters and notes
- Welcome/goodbye messages
- Global bans
- AFK status tracking
- And more (21 modules total)

## Setup
The bot requires these secrets to be set:
- `TOKEN` — Telegram bot token (from @BotFather)
- `OWNER_ID` — Your Telegram user ID (numeric)

Environment variables (already configured):
- `ENV=True` — Use environment variables for config
- `NO_LOAD=translation rss sed` — Modules to skip loading

## Running
The bot runs via the "Start application" workflow:
```
python3 -m tg_bot
```

It uses long polling (no webhook needed) and connects to the Replit PostgreSQL database automatically.

## Technical Notes
- Python 3.12 on Replit
- python-telegram-bot 13.15 (patched for Python 3.12 compatibility)
- SQLAlchemy 2.x (with compatibility fixes for table creation ordering)
- PostgreSQL (Replit managed DB) with BigInteger user IDs for Telegram 64-bit IDs
- Modules load dynamically from `tg_bot/modules/`

## User Preferences
