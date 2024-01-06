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
        self.html_template = """
        <html>
            <body>
                <p>Daily summary for [date]</p>
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
                <img src="cid:radiance-logo-no-bg">
            </body>
        </html>
        """

        self.image_path = "./../frontend/public/radiance-logo-no-bg.png"

        self.user_data = {}

    def send_email(self):
        em = EmailMessage()
        em["From"] = self.email_sender
        em["To"] = self.email_receiver
        em["Subject"] = self.subject

        # render template
        template = Template(self.html_template)
        html_content = template.render(user_data=self.user_data)
        em.add_alternative(html_content, subtype="html")

        # Attach an image
        with open(self.image_path, 'rb') as img:
            image_data = img.read()
            image_type = imghdr.what(img.name)
            image_name = img.name

        cid = "radiance-logo-no-bg"
        em.add_attachment(image_data, maintype="image", subtype=image_type, filename=image_name, cid=cid)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
            smtp.login(self.email_sender, self.email_password)
            smtp.sendmail(self.email_sender, self.email_receiver, em.as_string())
