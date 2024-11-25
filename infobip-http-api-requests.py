import mimetypes
from email.utils import formataddr

import requests

API_KEY = "YOUR_API_KEY"
INFOBIP_API_URL = "https://api.infobip.com/email/3/send"
EMAILS_FROM_EMAIL = "YOUR_EMAIL_ADDRESS"
EMAILS_FROM_NAME = "YOUR_EMAIL_FROM"

# File to attach
file_path = "files/receipt.pdf"

# Get the MIME type of the file
mime_type, _ = mimetypes.guess_type(file_path)

# Connection to Infobip API
url = INFOBIP_API_URL

# Form data to send (including text fields)
data = {
    "from": formataddr((EMAILS_FROM_NAME, EMAILS_FROM_EMAIL)),
    "subject": "This is your receipt",
    "to": ["recipient@example.com"],
    "bulkId": "test1234",
    "html": """
        <html>
          <body>
            <h1 style="color: #754ffe;">Dear Recipient,</h1>
            <p>This is a <b>test message</b> from <i>Infobip</i>.</p>
            <p>Have a <span style="color: green;">great day!</span></p>
          </body>
        </html>
    """,
}

# Headers
headers = {
    "Authorization": f"App {API_KEY}",
    "Accept": "application/json",
}

# Using context manager for file handling
with open(file_path, "rb") as file:
    # Attach the file (MIME type is automatically guessed)
    files = {"attachment": ("receipt.pdf", file, mimetypes.guess_type(file_path)[0])}

    # Send the request
    response = requests.post(url, data=data, headers=headers, files=files)

# Read the response
print(response.text)
