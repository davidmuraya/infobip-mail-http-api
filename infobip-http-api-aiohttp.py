import asyncio
import mimetypes
from email.utils import formataddr

import aiohttp

API_KEY = "YOUR_API_KEY"
INFOBIP_API_URL = "https://api.infobip.com/email/3/send"
EMAILS_FROM_EMAIL = "YOUR_EMAIL_ADDRESS"
EMAILS_FROM_NAME = "YOUR_EMAIL_FROM"


async def send_email_with_attachment():
    # File to attach
    file_path = "files/receipt.pdf"

    # Get the MIME type of the fileS
    mime_type, _ = mimetypes.guess_type(file_path)

    # Connection to Infobip API
    url = INFOBIP_API_URL

    # Form data to send (including text fields)
    data = {
        "from": formataddr((EMAILS_FROM_NAME, EMAILS_FROM_EMAIL)),
        "subject": "This is your receipt",
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

    data["to"] = ["recipient@example.com"]

    # Headers
    headers = {
        "Authorization": f"App {API_KEY}",
        "Accept": "application/json",
    }

    # Open the file and send the request
    async with aiohttp.ClientSession() as session:
        with open(file_path, "rb") as file:
            # Attach the file
            files = {"attachment": (file_path.split("/")[-1], file, mime_type)}

            # Make the request
            form_data = aiohttp.FormData()
            form_data.add_field(
                "attachment", file, filename="receipt.pdf", content_type=mime_type
            )
            for key, value in data.items():
                if isinstance(value, list):
                    # Ensure list values (e.g., "to") are properly handled
                    for item in value:
                        form_data.add_field(key, item)
                else:
                    form_data.add_field(key, value)

            async with session.post(url, data=form_data, headers=headers) as response:
                # Read the response
                response_text = await response.text()
                print(response_text)


# Run the coroutine
asyncio.run(send_email_with_attachment())
