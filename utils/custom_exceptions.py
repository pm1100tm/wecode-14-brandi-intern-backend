"""사용자 제작 예외 처리

앱 관련 사용자 제작 예외처리는 모두 이곳에 Exception 클래스를 상속받아 작성한다.
작성한 사용제 제작 예외 처리는 error_handler.py 에서 사용된다.

기본적인 사용 예시:
  class IamException(Exception):
        def __init__(self, error_message):
        self.status_code = 400
        self.message = 'your message goes here'
        self.error_message = error_message
        super().__init__(self.status_code, self.message, self.error_message)

"""

# don't touch
class CustomUserError(Exception):
    def __init__(self, status_code, message, error_message):
        self.status_code = status_code
        self.message = message
        self.error_message = error_message


#-----------------------------------------------------------------------------------------------------------------------


class InvalidUserId(CustomUserError):
    def __init__(self, error_message):
        status_code = 400
        message = 'id_must_be_integer'
        error_message = error_message
        super().__init__(status_code, message, error_message)


class UserAlreadyExist(CustomUserError):
    def __init__(self, error_message):
        status_code = 403
        message = "user_already_exist"
        error_message = error_message
        super().__init__(status_code, message, error_message)


class UserUpdateDenied(CustomUserError):
    def __init__(self, error_message):
        status_code = 400
        message = 'user_update_denied'
        error_message = error_message
        super().__init__(status_code, message, error_message)


class UserCreateDenied(CustomUserError):
    def __init__(self, error_message):
        status_code = 500
        message = 'user_create_denied'
        error_message = error_message
        super().__init__(status_code, message, error_message)


class UserNotExist(CustomUserError):
    def __init__(self, error_message):
        status_code = 404
        message = 'user_not_exist'
        error_message = error_message
        super().__init__(status_code, message, error_message)


class InvalidUser(CustomUserError):
    def __init__(self, error_message):
        status_code = 403
        message = 'invalid_user'
        error_message = error_message
        super().__init__(status_code, message, error_message)


class InvalidToken(CustomUserError):
    def __init__(self, error_message):
        status_code = 403
        message = 'invalid_token'
        error_message = error_message
        super().__init__(status_code, message, error_message)


class TokenCreateDenied(CustomUserError):
    def __init__(self, error_message):
        status_code = 500
        message = 'token_create_denied'
        error_message = error_message
        super().__init__(status_code, message, error_message)


class UnauthorizedUser(CustomUserError):
    def __init__(self, error_message):
        status_code = 401
        message = error_message
        error_message = error_message
        super().__init__(status_code, message, error_message)


class DatabaseCloseFail(CustomUserError):
    def __init__(self, error_message):
        status_code = 500
        message = "database_close_fail"
        error_message = error_message
        super().__init__(status_code, message, error_message)


class DatabaseError(CustomUserError):
    def __init__(self, error_message):
        status_code = 500
        message = "database_error"
        error_message = error_message
        super().__init__(status_code, message, error_message)


class DestinationNotExist(CustomUserError):
    """ 배송지 조회 불가

    Author: 김기용

    History:
        2020-12-28(김기용): 초기생성
    """
    def __init__(self, error_message):
        status_code = 401
        message = 'destination_does_not_exist'
        error_message = error_message
        super().__init__(status_code, message, error_message)
       

class DestinationCreateDenied(CustomUserError):
    """ 배송지 생성 거절

    Author: 김기용

    History:
        2020-12-28(김기용): 초기생성
    """
    def __init__(self, error_message):
        status_code = 400
        message = 'destination_creatation_denied'
        error_message = error_message
        super().__init__(status_code, message, error_message)


class NotUser(CustomUserError):
    """ 유저가 아님

    Author: 김기용

    History:
        2020-12-28(김기용): 초기생성
    """
    def __init__(self, error_message):
        status_code = 400
        message = 'not_a_user'
        error_message = error_message
        super().__init__(status_code, message, error_message)


class AccountNotExist(CustomUserError):
    """ 계정정보없음

    Author: 김기용

    History:
        2020-12-28(김기용): 초기생성
    """
    def __init__(self, error_message):
        status_code = 401
        message = 'account_does_not_exist'
        error_message = error_message
        super().__init__(status_code, message, error_message)


class CartItemNotExist(CustomUserError):
    """ 장바구니 상품 조회 실패 

    Author: 고수희

    History:
        2020-12-28(고수희): 초기생성
    """
    def __init__(self, error_message):
        status_code = 400
        message = 'cart items not exist'
        error_message = error_message
        super().__init__(status_code, message, error_message)


class CartItemCreateFail(CustomUserError):
    """ 장바구니 상품 추가 실패

    Author: 고수희

    History:
        2020-12-28(고수희): 초기생성
    """
    def __init__(self, error_message):
        status_code = 400
        message = 'cart item create'
        error_message = error_message
        super().__init__(status_code, message, error_message)


class DataLimitExceeded(CustomUserError):
    """ 데이터 제한 초과

    Author: 김기용

    History:
        2020-12-28(김기용): 초기생성
    """
    def __init__(self, error_message):
        status_code = 400
        message = 'data_limit_reached'
        error_message = error_message
        super().__init__(status_code, message, error_message)


class CustomerPermissionDenied(CustomUserError):
    """ 일반 유저 권한이 아님

    Author: 고수희

    History:
        2020-12-28(고수희): 초기생성
    """
    def __init__(self, error_message):
        status_code = 400
        message = 'customer permissions denied'
        error_message = error_message
        super().__init__(status_code, message, error_message)


class ProductNotExist(CustomUserError):
    """ 상품이 존재하지 않음

    Author: 고수희

    History:
        2020-12-30(고수희): 초기생성
    """
    def __init__(self, error_message):
        status_code = 400
        message = 'product does not exist'
        error_message = error_message
        super().__init__(status_code, message, error_message)


class DeleteDenied(CustomUserError):
    """ 논리 삭제 거부

    Author: 김기용

    History:
        2020-12-30(김기용): 초기생성
    """
    def __init__(self, error_message):
        status_code = 400
        message = 'invalid_delete_command_access'
        error_message = error_message
        super().__init__(status_code, message, error_message)


class DateMissingOne(CustomUserError):
    def __init__(self, error_message):
        status_code = 400
        message = 'date inputs should be start_date and end_date'
        error_message = error_message
        super().__init__(status_code, message, error_message)


class UpdateDenied(CustomUserError):
    """ 수정 거부

    Author: 김기용

    History:
        2020-12-30(김기용): 초기생성
    """
    def __init__(self, error_message):
        status_code = 400
        message = 'unable_to_update'
        error_message = error_message
        super().__init__(status_code, message, error_message)


class EventSearchTwoInput(CustomUserError):
    def __init__(self, error_message):
        status_code = 400
        message = 'event search inputs must be only one'
        error_message = error_message
        super().__init__(status_code, message, error_message)


class EventDoesNotExist(CustomUserError):
    def __init__(self, error_message):
        status_code = 404
        message = 'event not exist'
        error_message = error_message
        super().__init__(status_code, message, error_message)
