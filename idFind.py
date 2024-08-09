import asyncio
import logging
import json
import os
from telethon import TelegramClient


logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    handlers=[
        logging.FileHandler("IDfind.log"),
        logging.StreamHandler()
    ]
)

def create_config_file():
    config = {}
    print("Get your API ID and API Hash from my.telegram.org.")

    config['api_id'] = input("API ID: ")
    config['api_hash'] = input("API Hash: ")
    config['phone'] = input("Phone Number: ")

    with open('config.json', 'w') as config_file:
        json.dump(config, config_file, indent=4)

    print("config.json created successfully.")

def load_config():
    config_path = os.path.join(os.path.dirname(__file__), 'config.json')
    with open(config_path) as config_file:
        return json.load(config_file)

async def main():
    if not os.path.exists('config.json'):
        create_config_file()

    config = load_config()

    api_id = config['api_id']
    api_hash = config['api_hash']
    phone = config['phone']

    client = TelegramClient('session_name', api_id, api_hash)

    await client.start(phone)

    logging.info("connected To telegram.")

    async for dialog in client.iter_dialogs():
        if dialog.is_group or dialog.is_channel:
            logging.info(f"Name: {dialog.name}, ID: {dialog.id}")

if __name__ == "__main__":
    asyncio.run(main())
