#coding=utf-8
from frostcms.libs.validators import *
import datetime
from logging import getLogger

log = getLogger(__name__)

_ = lambda s: s


class UniquePhoneNumber(PhoneNumber):
    
    messages = dict(
                    exist = _(u'手机号已被其他用户注册')
                    )
    
    def _validate_python(self, value, state):
        user = state.request.db.user.find_one({'phone': value})
        if user:
            if not state.request.user or state.request.user.id != user['_id']:
                msg = self.message('exist', state, object=value)
                raise fe.Invalid(msg, value, state)
            
    validate_python = _validate_python

class UniqueEmail(fe.FancyValidator):
    
    messages = dict(
                    exist = _(u'邮箱已被其他用户注册')
                    )
    
    def _convert_to_python(self, value, state):
        validator = fe.validators.Email()
        value = validator.to_python(value, state)
        return value
    
    
    
    def _validate_python(self, value, state):
        user = state.request.db.user.find_one({'email': value})
        if user:
            if not state.request.user or state.request.user.id != user['_id']:
                msg = self.message('exist', state, object=value)
                raise fe.Invalid(msg, value, state)
            
    _to_python = _convert_to_python
    validate_python = _validate_python
                

def RealName(*kw, **kwargs):
    return fe.validators.UnicodeString(min=2, max=10)


def Password(*kw, **kwargs):
    return fe.validators.String(min=6, max=14)

def PhoneCode(*kw, **kwargs):
    return fe.validators.String(min=4, max=6)

    
    
