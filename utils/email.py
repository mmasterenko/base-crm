from django.conf import settings
from django.template import loader
from django.core.mail import send_mail
from constance import config

from project.celery import send_email


MAILS = {
    'found_many': (
        'Несколько одинаковых оригиналов !',
        loader.get_template('emails/system/found_many.txt')
    ),
    'found_nothing': (
        'Не нашлось оригинала !',
        loader.get_template('emails/system/found_nothing.txt')
    ),

    'register_new_user': (
        'Поздравляем! Вы зарегистрировались в OnlineCarService.',
        loader.get_template('emails/register_new_user.txt')
    ),

    'approve_link': (
        'Ссылка для подтверждения email',
        loader.get_template('emails/approve_link.txt')
    ),

    'restore_password': (
        'Восстановление пароля на OnlineCarService',
        loader.get_template('emails/restore_password.txt')
    ),

    'account_approved': (
        'Ваш аккаунт был подтвержден',
        loader.get_template('emails/account_approved.txt')
    ),

    'account_disapproved': (
        'Ваш аккаунт был заблокирован',
        loader.get_template('emails/account_disapproved.txt')
    ),

    'no_rangeset_found': (
        'Не нашлось рейнжсета',
        loader.get_template('emails/system/no_rangeset_found.txt')
    ),

    'no_valid_rangeset_found': (
        'Не нашлось валидного рейнжсета',
        loader.get_template('emails/system/no_valid_rangeset_found.txt')
    ),

    'many_valid_rangeset_found': (
        'Нашлось несколько валидных рейнжсетов',
        loader.get_template('emails/system/many_valid_rangeset_found.txt')
    ),
}


class EmailFactory:

    def __init__(self, mail_id, context=None):

        self.context = context

        if isinstance(mail_id, (list, tuple)):
            self.subject_template = mail_id[0]
            self.message_template = mail_id[1]
        else:
            self.subject_template = MAILS[mail_id][0]
            self.message_template = MAILS[mail_id][1]

    def get_subject(self, **kwargs):
        prefix = settings.EMAIL_SUBJECT_PREFIX
        subject = self.subject_template.format(**kwargs)
        return '{prefix} {subject}'.format(prefix=prefix, subject=subject)

    def get_message(self, context=None):
        return self.message_template.render(context)

    @property
    def subject(self):
        return self.get_subject()

    @property
    def message(self):
        return self.get_message(context=self.context)


def send_email_message(subject, message, *recipients):
    """
    Yandex doesn't allow set different `From` and `smtp_from`
    In this case SMTP Yandex server returns an error:

    '5.7.1 Sender address rejected: not owned by auth user.'
    """
    from_email = 'OnlineCarService <{from_email}>'.format(from_email=config.SMTP_USERNAME)

    if settings.USE_CELERY:
        return send_email.delay(subject, message, from_email, recipients)
    else:
        return send_mail(subject=subject,
                         message=message,
                         from_email=from_email,
                         recipient_list=recipients)


def send_email_managers(subject, message):
    from_email = 'OnlineCarService <{from_email}>'.format(from_email=config.SMTP_USERNAME)

    recipients = [a[1] for a in settings.MANAGERS]

    if settings.USE_CELERY:
        return send_email.delay(subject, message, from_email, recipients)
    else:
        return send_mail(subject=subject,
                         message=message,
                         from_email=from_email,
                         recipient_list=recipients)
