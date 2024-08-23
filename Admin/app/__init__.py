from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_mail import Mail, Message
import secrets

db = SQLAlchemy()
mail = Mail()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

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
    subject = f"Event {action.capitalize()}: {event.title}"

    body = f"""
    <html>
    <body style="font-family: Arial, sans-serif; color: #333; line-height: 1.6;">
        <div style="max-width: 600px; margin: 0 auto; padding: 20px; border: 1px solid #ddd; border-radius: 10px;">
            <h2 style="text-align: center;">🎉 Event Update: {event.title} 🎉</h2>
            <p>Hey there!</p>
            <p>Just wanted to give you a quick heads-up that the event <strong>'{event.title}'</strong> has been <strong>{action}</strong>! 😃</p>
            <p>Here's the lowdown:</p>
            <ul>
                <li><strong>Description:</strong> {event.description}</li>
                <li><strong>Date:</strong> {event.date}</li>
                <li><strong>Location:</strong> {event.location}</li>
            </ul>
            <p>Don't miss out on all the fun! Make sure to RSVP by clicking <a href="http://127.0.0.1:8000/api/v1/rsvp/{event.id}" style="color: #1a73e8;">here</a> 🚀.</p>
            <p>Can't wait to see you there! If you have any questions or need anything, just hit me up.</p>
            <p>Cheers,</p>
            <p>Your Event Team 🌟</p>
        </div>
    </body>
    </html>
    """

    recipients = ['brett@gmail.com']

    msg = Message(subject=subject,
                  html=body,
                  recipients=recipients,
                  sender='tayaevents@gmail.com')
    mail.send(msg)

def gen_token():
    token_len = 32
    token = secrets.token_hex(token_len)
    return token
