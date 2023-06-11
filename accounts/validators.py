from re import match
from django.core.exceptions import ValidationError


#----------------------------- User ---------------------------------------
def limit_file_size(value):
    if value.size > 2097152:
        raise ValidationError("حجم عکس بیشتر از 2 مگابایت نمیتواند باشد.")
    if value.height / value.width != 1:
        raise ValidationError("ابعداد عکس باید 1x1 (مربعی) باشد.")
    

def phone_validation(value):
    if not bool(match(pattern=r"^09\d{9}$", string=value)):
        return False
    return True
