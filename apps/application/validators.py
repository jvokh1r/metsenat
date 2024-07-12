from django.core.exceptions import ValidationError


def validate_phone_number(phone_number: str) -> None:
    if not len(phone_number) != 17 or not phone_number.startswith('+998') or not phone_number[1:].isdigit():
        raise ValidationError('Phone number is not valid!')