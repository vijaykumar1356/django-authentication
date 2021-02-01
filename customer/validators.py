import re
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

def username_length(value):
    if len(value)<4:
        raise ValidationError(_("Username is too short!"))
    return value

def username_is_alphanum(value):
    if not re.match(r'^([a-z]+[0-9]+)$', value):
        raise ValidationError(_("Username should be a mix of characters & numbers"))
    return value

def username_lowercase(value):
    if not value.islower():
        raise ValidationError(_("Username should be in lowercase!"))

def validate_password(value):
    if not re.match(r'^([a-zA-Z]+[0-9]+)$', value):
        raise ValidationError(_("Password should be a combination of alphabets & numbers!"))
    return value

