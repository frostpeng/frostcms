#coding=utf-8

import formencode as fe
import re
from bson import ObjectId
from logging import getLogger

log = getLogger(__name__)

_ = lambda s: s


class PhoneNumber(fe.FancyValidator):
    
    def _convert_to_python(self, value, state):
        validator = fe.validators.Regex(r'^0{0,1}(13\d|15\d|18[0123456789])\d{8}$')
        value = validator.to_python(value, state)
        return value
    
    _to_python = _convert_to_python
    
