# Infobip Email Sender with File Attachment

This repository contains two Python scripts that demonstrate how to send emails with attachments using the [Infobip Email API](https://www.infobip.com/docs/api#channels/email). The scripts utilize two different libraries:

1. **`requests`** (for synchronous HTTP requests)
2. **`aiohttp`** (for asynchronous HTTP requests)

## Features

- Send emails with custom HTML content.
- Attach a file (e.g., a PDF receipt) to the email.
- Specify the sender's name and email address.
- Choose between synchronous (`requests`) and asynchronous (`aiohttp`) implementations.

---

## Scripts Overview

### 1. **`email_sender_requests.py`**
This script uses the `requests` library to send an email with an attachment.

#### Key Characteristics:
- **Synchronous Implementation:** Each API call blocks the program until it completes.
- Simple to set up and execute.
- Suitable for straightforward tasks without concurrency.

---

### 2. **`email_sender_aiohttp.py`**
This script uses the `aiohttp` library for an asynchronous approach to sending emails with attachments.

#### Key Characteristics:
- **Asynchronous Implementation:** Supports non-blocking I/O operations, making it efficient for tasks requiring high concurrency.
- Requires Python's `asyncio` to manage event loops and tasks.

---

## Prerequisites

1. **Infobip Account:** Ensure you have an active Infobip account with access to the Email API.
2. **API Key:** Obtain your Infobip API key from the [Infobip Dashboard](https://portal.infobip.com/).
3. **Python Environment:** Install the required libraries:
   - `requests` (for the synchronous script)
   - `aiohttp` (for the asynchronous script)

   Use pip to install them:
   ```bash
   pip install requests aiohttp
   ```

4. **Email Setup:**
   - Replace `YOUR_API_KEY`, `YOUR_EMAIL_ADDRESS`, and `YOUR_EMAIL_FROM` in both scripts with your actual Infobip API key, sender email address, and sender name.

5. **File to Attach:** Ensure the file you wish to attach (`receipt.pdf` in this case) is located in the `files/` directory.

---

## Usage

### **1. Run the Synchronous Script (`infobip-http-api-requests.py`)**

1. Modify the script to add your Infobip API details:
   ```python
   API_KEY = "YOUR_API_KEY"
   EMAILS_FROM_EMAIL = "YOUR_EMAIL_ADDRESS"
   EMAILS_FROM_NAME = "YOUR_EMAIL_FROM"
   ```

2. Execute the script:
   ```bash
   python email_sender_requests.py
   ```

3. Check the console for the API response.

---

### **2. Run the Asynchronous Script (`infobip-http-api-aiohttp.py`)**

1. Modify the script to add your Infobip API details:
   ```python
   API_KEY = "YOUR_API_KEY"
   EMAILS_FROM_EMAIL = "YOUR_EMAIL_ADDRESS"
   EMAILS_FROM_NAME = "YOUR_EMAIL_FROM"
   ```

2. Execute the script:
   ```bash
   python email_sender_aiohttp.py
   ```

3. Check the console for the API response.

---

## Example HTML Email Content

The scripts send the following email body as an example:
```html
<html>
  <body>
    <h1 style="color: #754ffe;">Dear Recipient,</h1>
    <p>This is a <b>test message</b> from <i>Infobip</i>.</p>
    <p>Have a <span style="color: green;">great day!</span></p>
  </body>
</html>
```

---

## Notes

- **Security:** Never hard-code sensitive information such as API keys in your scripts. Use environment variables or a configuration file for secure storage.
- **Error Handling:** Implement error handling for production use to capture and log API failures.
- **Attachments:** Ensure the file path and MIME type are correct for the attachment.

---

## License

This repository is released under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Support

For issues or feature requests, please open an issue in this repository. For Infobip-related support, refer to the [Infobip Help Center](https://www.infobip.com/support).