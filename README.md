# Event Management API

The Event Management API provides a comprehensive solution for managing events, RSVPs, and comments. It supports user authentication, event management by admins, and includes both public and admin-specific endpoints.

## Table of Contents

1. [Usage](#usage)
2. [API Endpoints](#api-endpoints)
   - [User Authentication](#1-user-authentication)
   - [Events Management](#2-events-management)
   - [RSVP Management](#3-rsvp-management)
   - [Comments Management](#4-comments-management)
   - [Admin Endpoints](#admin-endpoints)
3. [Authorization](#authorization)
4. [Running the API](#running-the-api)
5. [Notes](#notes)
6. [License](#license)
7. [Contribution](#contribution)
8. [Author](#author)

## Usage

This API allows users to create accounts, log in, RSVP for events, and comment on events. Admins have additional privileges to create, update, delete, and manage events.

## API Endpoints

### 1. **User Authentication**

#### **Sign Up**

- **Endpoint:** `POST /api/signup/`
- **Description:** Creates a new user account.
- **Request:**
  ```json
  {
    "username": "test",
    "password": "test1234",
    "email": "test@gmail.com"
  }
  ```
- **Response:** Returns a token and user details upon successful registration.

#### **Login**

- **Endpoint:** `POST /api/login/`
- **Description:** Logs in an existing user and provides an authentication token.
- **Request:**
  ```json
  {
    "username": "test",
    "password": "test1234"
  }
  ```
- **Response:** Returns an authentication token and user details if credentials are valid.

### 2. **Events Management**

#### **Get All Events**

- **Endpoint:** `GET /api/events/`
- **Description:** Retrieves a list of all events.
- **Headers:**
  - `Authorization: Token <your_token>`

### 3. **RSVP Management**

#### **Create RSVP**

- **Endpoint:** `POST /api/rsvp/`
- **Description:** Creates a new RSVP for an event.
- **Headers:**
  - `Authorization: Token <your_token>`
- **Request:**
  ```json
  {
    "event": 3,
    "response": "True"
  }
  ```

#### **Get All RSVPs**

- **Endpoint:** `GET /api/rsvp/`
- **Description:** Retrieves all RSVPs of the authenticated user.
- **Headers:**
  - `Authorization: Token <your_token>`

#### **Get RSVP by ID**

- **Endpoint:** `GET /api/rsvp/2/`
- **Description:** Retrieves the details of a specific RSVP by ID.
- **Headers:**
  - `Authorization: Token <your_token>`

#### **Update RSVP**

- **Endpoint:** `PUT /api/rsvp/2/`
- **Description:** Updates an existing RSVP.
- **Headers:**
  - `Authorization: Token <your_token>`
- **Request:**
  ```json
  {
    "response": "False"
  }
  ```

#### **Delete RSVP**

- **Endpoint:** `DELETE /api/rsvp/2/`
- **Description:** Deletes a specific RSVP by ID.
- **Headers:**
  - `Authorization: Token <your_token>`

### 4. **Comments Management**

#### **Create a Comment**

- **Endpoint:** `POST /api/comments/`
- **Description:** Adds a new comment to an event.
- **Headers:**
  - `Authorization: Token <your_token>`
- **Request:**
  ```json
  {
    "event": 2,
    "comment": "This is a comment"
  }
  ```

#### **Get Comment by ID**

- **Endpoint:** `GET /api/comments/2/`
- **Description:** Retrieves a specific comment by ID.
- **Headers:**
  - `Authorization: Token <your_token>`

#### **Update a Comment**

- **Endpoint:** `PUT /api/comment/3/`
- **Description:** Updates an existing comment.
- **Headers:**
  - `Authorization: Token <your_token>`
- **Request:**
  ```json
  {
    "comment": "New comment on the event"
  }
  ```

#### **Delete a Comment**

- **Endpoint:** `DELETE /api/comment/1/`
- **Description:** Deletes a specific comment by ID.
- **Headers:**
  - `Authorization: Token <your_token>`

## Admin Endpoints

These endpoints are restricted to admin users and require a bearer token for authentication.

#### **Register an Admin**

- **Endpoint:** `POST /register`
- **Description:** Registers a new admin.
- **Request:**
  ```json
  {
    "username": "admin1",
    "password": "securepassword",
    "name": "Admin User",
    "email": "admin@example.com"
  }
  ```
- **Response:** Returns admin details upon successful registration.

#### **Create Event**

- **Endpoint:** `POST /events`
- **Description:** Creates a new event.
- **Headers:**
  - `Authorization: Bearer <admin_token>`
- **Request:**
  ```json
  {
    "title": "Event Title",
    "description": "Event Description",
    "date": "2024-09-01T10:00:00",
    "location": "Event Location"
  }
  ```
- **Response:** Returns the created event details.

#### **Get All Events**

- **Endpoint:** `GET /events`
- **Description:** Retrieves a list of all events.
- **Headers:**
  - `Authorization: Bearer <admin_token>`

#### **Update Event**

- **Endpoint:** `PUT /events/<event_id>`
- **Description:** Updates an existing event.
- **Headers:**
  - `Authorization: Bearer <admin_token>`
- **Request:**
  ```json
  {
    "title": "Updated Event Title",
    "description": "Updated Event Description",
    "date": "2024-09-02T12:00:00",
    "location": "Updated Location"
  }
  ```
- **Response:** Returns the updated event details.

#### **Delete Event**

- **Endpoint:** `DELETE /events/<event_id>`
- **Description:** Deletes an event by ID.
- **Headers:**
  - `Authorization: Bearer <admin_token>`
- **Response:** Confirms event deletion.

## Authorization

- All user-specific and admin endpoints require an authorization token.
- General users receive their token upon login.
- Admin users must provide a Bearer token for protected endpoints.

## Running the API

1. **Clone the Repository:**
   ```bash
   git clone <your-repo-url>
   cd <your-repo-directory>
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Migrations:**
   ```bash
   python manage.py migrate
   ```

4. **Start the Server:**
   ```bash
   python manage.py runserver
   ```

**Start the Server for Admin:**
   ```bash
   cd Admin
   python run.py
   ```

5. **Test the API using Postman or any other API testing tool.**

## Notes

- Make sure to use the correct token for authorization when testing the API.
- The token can be obtained after a successful login or admin registration.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contribution

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

Please ensure your code follows the project's coding style and includes appropriate tests.

## Author

- [waltertaya](https://www.github.com/waltertaya)
