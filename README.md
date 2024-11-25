# Infobip Email Sender with File Attachment

This script demonstrates how to send emails with attachments using the [Infobip Email API](https://www.infobip.com/docs/api#channels/email) and Python's `requests` library.

## Features

- Send emails with custom HTML content.
- Attach a file (e.g., a PDF receipt) to the email.
- Specify the sender's name and email address.
- Utilize Infobip's API for robust email delivery.

## Prerequisites

1. **Infobip Account:** Ensure you have an active Infobip account with access to the Email API.
2. **API Key:** Obtain your Infobip API key from the [Infobip Dashboard](https://portal.infobip.com/).
3. **Python Environment:** The script is written in Python and requires the following modules:
   - `requests`
   - `mimetypes`
   - `email.utils`

   You can install the `requests` library using pip:
   ```bash
   pip install requests
   ```

4. **Email Setup:**
   - Replace `YOUR_API_KEY`, `YOUR_EMAIL_ADDRESS`, and `YOUR_EMAIL_FROM` in the script with your actual Infobip API key, sender email address, and sender name.

5. **File to Attach:** Ensure the file you wish to attach (`receipt.pdf` in this case) is located in the `files/` directory.

## Usage

1. **Clone or Download the Script**
   Clone the repository or copy the script into your project directory.

2. **Modify Configuration**
   Update the following variables in the script:
   ```python
   API_KEY = "YOUR_API_KEY"
   EMAILS_FROM_EMAIL = "YOUR_EMAIL_ADDRESS"
   EMAILS_FROM_NAME = "YOUR_EMAIL_FROM"
   ```

3. **Run the Script**
   Execute the script:
   ```bash
   python email_sender.py
   ```

4. **Check the Response**
   The script prints the API response to the console. Verify that the email was sent successfully.

## Code Overview

- **Form Data:**
  The `data` dictionary contains fields such as `from`, `to`, `subject`, and `html` for email content.

- **File Attachment:**
  The `files` dictionary includes the file to be attached. MIME type is determined automatically using the `mimetypes` module.

- **Request:**
  A POST request is sent to the Infobip Email API with the form data, headers, and attachment.

## Example HTML Email Content

The script sends the following email body as an example:
```html
<html>
  <body>
    <h1 style="color: #754ffe;">Dear Recipient,</h1>
    <p>This is a <b>test message</b> from <i>Infobip</i>.</p>
    <p>Have a <span style="color: green;">great day!</span></p>
  </body>
</html>
```

## Notes

- **Security:** Never hard-code sensitive information such as API keys in your scripts. Use environment variables or a configuration file for secure storage.
- **Error Handling:** Implement error handling for production use to capture and log API failures.
- **Attachments:** Ensure the file path and MIME type are correct for the attachment.

## License

This script is released under the MIT License. See the [LICENSE](LICENSE) file for details.

## Support

For issues or feature requests, please open an issue in this repository. For Infobip-related support, refer to the [Infobip Help Center](https://www.infobip.com/support).