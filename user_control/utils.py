import random, secrets
from django.core.mail import send_mail
from django.urls import reverse
from django.conf import settings
from twilio.rest import Client


def generate_verification_code():
    # Generate a random 6-digit verification code
    return str(random.randint(100000, 999999))


def send_password_reset_email(email, token):
    reset_link = reverse('password-reset-confirm', args=[token])
    reset_url = f'{settings.FRONTEND_BASE_URL}{reset_link}'
    subject = 'Password Reset Request'
    message = f'Click the following link to reset your password: {reset_url}'
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email])


def generate_unique_token(length=32):
    """
    Generate a unique and secure token.

    Parameters:
    - length (int): Length of the token (default is 32).

    Returns:
    - str: Generated token.
    """
    return secrets.token_urlsafe(length)


def send_verification_code(phone_number, verification_code):
    # Set up Twilio client
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

    # Replace with your Twilio phone number
    twilio_phone_number = settings.TWILIO_PHONE_NUMBER

    # Send SMS with verification code
    message = client.messages.create(
        body=f'Your verification code is: {verification_code}',
        from_=twilio_phone_number,
        to=phone_number
    )


def send_verification_email(email, verification_code):
    # Send verification email
    subject = 'Verify your email address'
    message = f'Your verification code is: {verification_code}'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list)

    return verification_code
