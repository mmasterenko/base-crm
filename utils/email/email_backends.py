import threading

from django.conf import settings
from django.core.mail.backends.smtp import EmailBackend
from constance import config


class CustomEmailBackend(EmailBackend):

    def __init__(self, host=None, port=None, username=None, password=None,
                 use_tls=None, fail_silently=False, use_ssl=None, timeout=None,
                 ssl_keyfile=None, ssl_certfile=None,
                 **kwargs):
        super(EmailBackend, self).__init__(fail_silently=fail_silently)
        self.host = host or config.SMTP_HOST
        self.port = port or config.SMTP_PORT
        self.username = config.SMTP_USERNAME if username is None else username
        self.password = config.SMTP_PASSWORD if password is None else password
        self.use_tls = config.USE_TLS if use_tls is None else use_tls

        self.use_ssl = settings.EMAIL_USE_SSL if use_ssl is None else use_ssl
        self.timeout = settings.EMAIL_TIMEOUT if timeout is None else timeout
        self.ssl_keyfile = settings.EMAIL_SSL_KEYFILE if ssl_keyfile is None else ssl_keyfile
        self.ssl_certfile = settings.EMAIL_SSL_CERTFILE if ssl_certfile is None else ssl_certfile
        if self.use_ssl and self.use_tls:
            raise ValueError(
                "EMAIL_USE_TLS/EMAIL_USE_SSL are mutually exclusive, so only set "
                "one of those settings to True.")
        self.connection = None
        self._lock = threading.RLock()
