import os
import smtplib
import ssl
import imghdr
from email.message import EmailMessage
from jinja2 import FileSystemLoader, Environment
from readers.json_reader import load_json

CONFIG_SPEC_FILENAME = "./json/smtp_config_spec.json"

class EmailConfig:
    """Load and hold configuration for email service provider."""
    def __init__(self, provider_name: str):
        self.provider_name = provider_name
        all_config = load_json(CONFIG_SPEC_FILENAME)
        self.config = all_config[provider_name]

class EmailSender:
    """Manage the creation and sending of emails using SMTP protocol."""

    def __init__(self, year_month_day: str, email_provider_name: str, email_template_filename:str) -> None:
        self.year_month_day = year_month_day
        # Load configuration for email provider
        self.config = EmailConfig(email_provider_name).config

        # Load environmental variables
        self.email_sender = os.getenv("EMAIL_SENDER")
        self.email_password = os.getenv("EMAIL_PASSWORD")
        self.email_receiver = os.getenv("EMAIL_RECEIVER")

        # Set up Jinja2 for HTML templating
        self.template_loader = FileSystemLoader(searchpath="./../frontend/public/")
        self.template_env = Environment(loader=self.template_loader)
        self.template_file = email_template_filename

        # Image path configuration
        self.image_path = "./../frontend/public/radiance-logo-no-bg.png"

        # Data to be used within the user email
        self.user_data = {}

    def send_email(self, subject: str):
        """Send an email with the given subject."""
        em = self._prepare_email_message(subject)

        # Use SSL context for secure email sending
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(self.config["smtp_server"], self.config["smtp_port"], context=context) as smtp:
            smtp.login(self.email_sender, self.email_password)
            smtp.sendmail(self.email_sender, self.email_receiver, em.as_string())

    def _prepare_email_message(self, subject: str) -> EmailMessage:
        """Prepare the email message with HTML content and image attachment."""
        em = EmailMessage()
        em["From"] = self.email_sender
        em["To"] = self.email_receiver
        em["Subject"] = subject

        # Render HTML template and set email body
        template = self.template_env.get_or_select_template(self.template_file)
        html_content = template.render(user_data=self.user_data, year_month_day=self.year_month_day)
        em.add_alternative(html_content, subtype="html")

        # Attach image (if applicable)
        with open(self.image_path, 'rb') as img:
            image_data = img.read()
            image_type = imghdr.what(img.name)
            image_name = os.path.basename(img.name)

        em.add_attachment(image_data, maintype="image", subtype=image_type, filename=image_name)

        return em