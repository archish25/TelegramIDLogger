# TelegramIDLogger


## Overview

This project requires a `config.json` file to function properly. This file contains essential configuration details, including your Telegram API credentials.

## Setup Instructions

### 1. Run the Program to Generate and Configure `config.json`

When you run the program for the first time, the `config.json` file will be automatically created. The program will prompt you to enter your API credentials and phone number during this initial run.

### 2. Obtain API Credentials

You will need an API ID and API Hash from Telegram. Follow these instructions to obtain them:

1. Visit [my.telegram.org](https://my.telegram.org).
2. Log in with your Telegram account.
3. Create a new application to get your `api_id` and `api_hash`.

### 3. Enter Your Details

When prompted by the program, provide the following details:

- **API ID**
- **API Hash**
- **Phone Number**


The program will automatically save these details to the `config.json` file.

### 4. Update the `config.json` File

Once the `config.json` file has been generated, open it and include the following fields:

```json
{
    "api_id": "",
    "api_hash": "",
    "phone": ""
}
