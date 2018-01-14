from django.conf import settings
from django.utils.log import AdminEmailHandler
from django.core.mail.message import EmailMultiAlternatives
from constance import config


def mail_admins(subject, message, fail_silently=False, connection=None,
                html_message=None):
    """Sends a message to the admins, as defined by the ADMINS setting."""
    if not settings.ADMINS:
        return
    mail = EmailMultiAlternatives(
        '%s%s' % (settings.EMAIL_SUBJECT_PREFIX, subject),
        message,
        config.SMTP_USERNAME,
        [a[1] for a in settings.ADMINS],
        connection=connection,
    )
    if html_message:
        mail.attach_alternative(html_message, 'text/html')
    mail.send(fail_silently=fail_silently)


class CustomAdminEmailHandler(AdminEmailHandler):

    def send_mail(self, subject, message, *args, **kwargs):
        mail_admins(subject, message, *args, connection=self.connection(), **kwargs)
