from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_booking_confirmation_email(user_email, listing_title):
    subject = 'Booking Confirmation'
    message = f'Thank you for booking: {listing_title}. We’ve received your booking.'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user_email]
    send_mail(subject, message, from_email, recipient_list)
