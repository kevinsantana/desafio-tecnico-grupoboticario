from cashback_api.excecoes import CashbackApiException


class TokenExpiradoException(CashbackApiException):
    def __init__(
        self,
        status: int,
        error: str,
        message: str,
        error_details: list = [],
    ):
        self.status = status
        self.error = error
        self.message = message
        self.error_details = error_details
        super().__init__(status, error, message, error_details)


class TokenInvalidoException(CashbackApiException):
    def __init__(
        self,
        status: int,
        error: str,
        message: str,
        error_details: list = [],
    ):
        self.status = status
        self.error = error
        self.message = message
        self.error_details = error_details
        super().__init__(status, error, message, error_details)


class TokenNaoInformadoException(CashbackApiException):
    def __init__(
        self,
        status: int,
        error: str,
        message: str,
        error_details: list = [],
    ):
        self.status = status
        self.error = error
        self.message = message
        self.error_details = error_details
        super().__init__(status, error, message, error_details)
