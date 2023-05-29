# Password Checker

This is a simple password checker application that checks if a given password has been compromised in any known data breaches. It uses the Have I Been Pwned API to retrieve password hash information and determine if a password has been exposed.

## Features

- The application takes a user-input password and sends a hashed version of it to the Have I Been Pwned API.
- The API responds with a list of password hashes that match the first five characters of the hashed password.
- The application compares the remaining characters of the hashed password with the received password hashes to check for a match.
- If a match is found, the application indicates that the password has been compromised and suggests changing it.
- If no match is found, the application assures the user that the password has not been found in any known data breaches.

## Installation

To use this application, follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies by running the command `pip install -r requirements.txt`.
3. Run the application by executing the command `python app.py`.
4. Access the application through a web browser at `http://localhost:5000`.

## Usage

1. Enter a password in the provided input field.
2. Click the "Check Password" button.
3. The application will display the result indicating whether the password has been compromised or not.
4. If the password has been compromised, it is recommended to change it to maintain security.

## Note

- The application uses the SHA-1 hashing algorithm to securely transmit the password information.
- The Have I Been Pwned API is a trusted source that securely handles password hash information without sending the actual password.
- The application does not store any user passwords or transmit them to third-party services.
- This is a basic implementation and can be expanded or integrated into other applications as needed.

**Disclaimer: Please exercise caution and use this application responsibly. Avoid entering passwords that you currently use or that are sensitive in nature. Always prioritize your online security by using strong and unique passwords for each service.**
