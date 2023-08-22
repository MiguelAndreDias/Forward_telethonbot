# Forward_telethonbot
Simple telegram bot that forwards messages from certain users from one group to another group/channel.



# Telegram Forward Bot

A Python bot using the Telethon library to forward messages from certain users and automatically pin messages to a channel whenever someone from a given list posts a crypto smart contract.


## Introduction

The Telegram Forward Bot is designed to forward messages from specific users and automatically pin messages to a designated channel when certain users post a crypto smart contract. It uses the Telethon library to interact with the Telegram API and perform these actions.

## Requirements

- Python 3.x
- Telethon library
- `python-dotenv` library

## Installation

1.Install the required Python packages using pip:

```
pip install -r requirements.txt

```


2.Create a .env file in the project directory and add your Telegram API ID and API hash:
```
API_ID=your_api_id
API_HASH=your_api_hash
```

3.Customize the lista_users list with the usernames of users whose messages you want to forward. Update the groups list with the channel/group IDs where you want to forward and pin messages.

