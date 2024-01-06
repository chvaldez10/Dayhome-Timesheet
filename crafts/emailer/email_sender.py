import os
import smtplib
import ssl
import imghdr
from email.message import EmailMessage
from jinja2 import FileSystemLoader, Environment
class EmailSender:
    def __init__(self):
        self.email_sender = os.getenv("EMAIL_SENDER")
        self.email_password = os.getenv("EMAIL_PASSWORD")
        self.email_receiver = os.getenv("EMAIL_RECEIVER")
        self.subject = "Test Email"

        # html template
        self.template_loader = FileSystemLoader(searchpath="./../frontend/public/")
        self.template_env = Environment(loader=self.template_loader)
        self.template_file = "email_template.html"

        # image
        self.image_path = "./../frontend/public/radiance-logo-no-bg.png"

        # user data
        self.user_data = {}

    def send_email(self):
        em = EmailMessage()
        em["From"] = self.email_sender
        em["To"] = self.email_receiver
        em["Subject"] = self.subject

        # render template
        template = self.template_env.get_or_select_template(self.template_file)
        html_content = template.render(user_data=self.user_data)
        em.add_alternative(html_content, subtype="html")

        # attach image
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
