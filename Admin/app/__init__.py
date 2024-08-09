from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_mail import Mail, Message
import secrets
import mailslurp_client
from mailslurp_client import ApiClient, Configuration, InboxControllerApi

db = SQLAlchemy()
mail = Mail()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # provided by mailtrap for testing
    app.config['MAIL_SERVER']=''
    app.config['MAIL_PORT'] = 2525
    app.config['MAIL_USERNAME'] = ''
    app.config['MAIL_PASSWORD'] = ''
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False

    app.config['MAIL_DEFAULT_SENDER'] = 'tayaevents@gmail.com'

    db.init_app(app)
    mail.init_app(app)

    with app.app_context():
        from . import routes, models
        db.create_all()

    return app

def create_mail_service(app):
    return Mail(app)

def send_notification(event, action):
    # using mailslurp for testing
    configuration = Configuration()
    configuration.api_key['x-api-key'] = ''

    with ApiClient(configuration) as api_client:
        inbox_controller = InboxControllerApi(api_client)
        inbox = inbox_controller.create_inbox()
        test_email = inbox.email_address

    subject = f"Event {action.capitalize()}: {event.title}"
    body = f"The event '{event.title}' has been {action}.\n\n" \
           f"Description: {event.description}\n" \
           f"Date: {event.date}\n" \
           f"Location: {event.location}"

    recipients = ['taya@gmail.com']

    msg = Message(subject=subject,
                  body=body,
                  recipients=recipients,
                  sender='tayaevents@gmail.com')
    mail.send(msg)

    print(f"Notification sent to test email: {test_email}")

def gen_token():
    token_len = 32
    token = secrets.token_hex(token_len)
    return token
