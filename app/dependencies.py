from fastapi import Request

def get_current_user(request: Request):
    """
    Login olmuş kullanıcının email'ini cookie'den alır
    """
    return request.cookies.get("user")