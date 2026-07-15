from django.utils import timezone
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


# Generation of reference number
def generate_reference(initial, obj):
    """Generation of reference number

    Args:
        initial (str): prefix of word
        obj (object): model object

    Returns:
        str: reference number
    """

    now = timezone.now()

    prefix = (
        f"{initial}-"
        f"{now:%Y%m}"
    )

    count = obj.objects.count() + 1

    return (

        f"{prefix}"

        f"-{count:04d}"
    )






def sendmail(**kwargs)-> bool: 
    """email sender

    Returns:
        _type_: Boolean
    """
    username = kwargs.get('username')
    usermail = kwargs.get('usermail')
    mailsubject = kwargs.get('mailsubject')
    template_html = kwargs['html_file']
    template_txt = kwargs['txt_file']
    protocol = kwargs.get('protocol')
    host = kwargs.get('host')
    path = kwargs.get('path')
    reference = kwargs.get('reference')
    message = kwargs.get('message')
    info = {
        'username' : username,
        'protocol' : protocol,
        'host' : host,
        'reference' : reference,
        'message' : message,
    }

    template_email = render_to_string(template_html, info)
    text_content = render_to_string(template_txt, info)

    email = EmailMultiAlternatives(
            mailsubject,
            text_content, 
            settings.EMAIL_HOST_USER, 
            [usermail],
            [settings.EMAIL_CC],
        )
    email.attach_alternative(template_email, "text/html")
    email.fail_silently = False
    try:
        email.send()
        return {'email_sent' : True}
    except Exception as e:
        print(e)
        return {'email_sent' : False}