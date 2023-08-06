"""Declares exception types."""
import uuid

from .schema import CanonicalExceptionSchema


class CanonicalException(Exception):
    """The base class for all exceptions."""
    __module__ = 'unimatrix.ext.model'

    #: The schema class used to convert the canonical exception to a
    #: dictionary.
    schema_class = CanonicalExceptionSchema

    #: The HTTP default HTTP status code.
    http_status_code: int = None

    #: The default code for the exception.
    code: str = 'UNCAUGHT_EXCEPTION'

    #: The default message.
    message: str = None

    #: The default detail.
    detail: str = None

    #: The default hint
    hint: str = None

    #: The default log message. String formatting is applied.
    log_message: str = "Caught fatal {code} (id: {id})"

    #: The cooldown period enforced on the caller.
    backoff: dict = None

    @property
    def http_headers(self) -> dict:
        """The HTTP headers when returning this exception to a client."""
        return self.get_http_headers()

    def __init__(self, id=None, code=None, message=None, detail=None, hint=None,
        http_status_code=None, **params):
        """Initialize a new :class:`CanonicalException`."""
        self.id = id or uuid.uuid4()
        self.code = code or self.code
        self.message = message or self.message
        self.detail = detail or self.detail
        self.hint = hint or self.hint
        self.http_status_code = http_status_code or self.http_status_code
        self.schema = self.schema_class()
        self.params = params

    def as_dict(self):
        """Return a dictionary containing the exception properties."""
        return self.schema.dump(self)

    def get_http_headers(self) -> dict:
        """Return a dictionary containing the HTTP headers to add to
        a client response.
        """
        return {
            'X-Error-Code': self.code,
            'X-Canonical-Exception': type(self).__name__
        }


    def log(self, func, message=None):
        """Use `logger` to log the exception as `level`."""
        return func((message or self.log_message).format(**self.as_dict()))

    def set_backoff(self,
        ttl: int,
        expires: int,
        attempts: int
    ) -> None:
        """Set a backoff (cooldown) period that indicating how
        long the caller wait before retrying the request that
        caused the :class:`CanonicalException`.
        """
        self.backoff = {
            'ttl': ttl,
            'expires': expires,
            'attempts': attempts
        }

    def __str__(self) -> str:
        return repr(self)

    def __repr__(self) -> str:
        return f'<{type(self).__name__}: {self.code} (id: {self.id})>'
