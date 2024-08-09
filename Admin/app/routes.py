from flask_httpauth import HTTPTokenAuth
from werkzeug.security import generate_password_hash, check_password_hash

from flask import request, jsonify
from . import db, send_notification
from .models import Admin, Event

import datetime


def register_routes(app):

    auth = HTTPTokenAuth(scheme='Bearer')

    @auth.verify_token
    def verify_token(token):
        user = Admin.query.filter_by(token=token).first()
        if user:
            return user.token
        return None

    @app.route('/register', methods=['POST'])
    def register():
        data = request.get_json()
        user = Admin.query.filter_by(username=data['username']).first()
        if user:
            return jsonify({'Error': 'User already exists'}), 400
        new_admin = Admin(
            username=data['username'],
            password=generate_password_hash(data['password']),
            name=data['name'],
            email=data['email']
        )
        db.session.add(new_admin)
        db.session.commit()
        return jsonify(new_admin.to_dict()), 201
    
    @app.route('/events', methods=['POST'])
    @auth.login_required
    def create_event():
        data = request.get_json()
        if not data or not all(k in data for k in ('title', 'description', 'date', 'location')):
            return jsonify({'Error': 'Missing required fields'}), 400

        new_event = Event(
            title=data['title'],
            description=data['description'],
            date=datetime.datetime.fromisoformat(data['date']),
            location=data['location']
        )
        db.session.add(new_event)
        db.session.commit()
        send_notification(new_event, 'created')
        return jsonify(new_event.to_dict()), 201

    @app.route('/events/<int:event_id>', methods=['PUT'])
    @auth.login_required
    def update_event(event_id):
        data = request.get_json()
        event = Event.query.get_or_404(event_id)

        if 'title' in data:
            event.title = data['title']
        if 'description' in data:
            event.description = data['description']
        if 'date' in data:
            event.date = datetime.datetime.fromisoformat(data['date'])
        if 'location' in data:
            event.location = data['location']

        db.session.commit()
        send_notification(event, 'updated')
        return jsonify(event.to_dict()), 200

    @app.route('/events/<int:event_id>', methods=['DELETE'])
    @auth.login_required
    def delete_event(event_id):
        event = Event.query.get_or_404(event_id)
        db.session.delete(event)
        db.session.commit()
        send_notification(event, 'deleted')
        return jsonify({'message': 'Event deleted successfully'}), 200

    return app
