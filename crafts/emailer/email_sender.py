import os
import smtplib
import ssl
import imghdr
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from jinja2 import Template

class EmailSender:
    def __init__(self):
        self.email_sender = os.getenv("EMAIL_SENDER")
        self.email_password = os.getenv("EMAIL_PASSWORD")
        self.email_receiver = os.getenv("EMAIL_RECEIVER")
        self.subject = "Test Email"
        self.body = """
        <html>
            <body>
                <p>Daily summary for [date]<p>
                <table>
                    <tr>
                        <th>User</th>
                        <th>Sign In</th>
                        <th>Sign Out</th>
                        <th>Total Time</th>
                    </tr>
                    <tr>
                        {% for user, data in user_data.items() %}
                        <td>{{ user }}</td>
                        <td>{{ data[0] }} h</td>
                        <td>{{ data[1] }} h</td>
                        <td>{{ data[2] }} h</td>
                        {% endfor %}
                    </tr>
                </table>
            </body>
        </html>
        """

        self.image_path = "./../../frontend/public/radiance-logo-no-bg.png"

        self.user_data = {
            "user": ["9 AM", "5 PM", 8]
        }

    def send_email(self):
        em = EmailMessage()
        em["From"] = self.email_sender
        em["To"] = self.email_receiver
        em["Subject"] = self.subject
        em.set_content(self.body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
            smtp.login(self.email_sender, self.email_password)
            smtp.sendmail(self.email_sender, self.email_receiver, em.as_string())
