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

def load_config():
    config_path = os.path.join(os.path.dirname(__file__), 'config.json')
    with open(config_path) as config_file:
        return json.load(config_file)

async def main():
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