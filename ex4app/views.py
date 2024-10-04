from django.core.mail import send_mail
from django.http import HttpResponse

def send_email(request):
    subject = 'Test Email from Django'
    message = 'Hello! This is a test email sent from a Django application.'
    recipient_list = ['arthyit@kamarajengg.edu.in']  # Replace with a real email
    
    send_mail(
        subject,
        message,
        '22uit082@kamarajengg.edu.in',  # From email (replace with your email)
        recipient_list,
        fail_silently=False,  # Set to True if you want to suppress errors
    )
    
    return HttpResponse("Email has been sent successfully!")
