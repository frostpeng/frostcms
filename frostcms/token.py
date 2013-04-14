#coding=utf-8
import md5, time

from logging import getLogger

log = getLogger(__name__)

class Token(object):
    
    def __init__(self,secret='haoshanghustß'):
        self.secret = secret
    
    def decode(self, token):
        params = str(token).split('.')
        userid = params[0]
        expire_in = int(params[1])
        sign = params[2]
        if expire_in > time.time():
            if sign == self._to_sign(userid, expire_in):
                return dict(userid=userid, expire_in = expire_in)
        return None
    
    def encode(self, userid, expire_in):
        userid = str(userid)
        return "%s.%d.%s" % (userid, expire_in, self._to_sign(userid, expire_in))
    
    def _to_sign(self, userid, expire_in):
        unsigned_data = 'userid=%s&expire_in=%d&secret=%s' % (userid, expire_in, self.secret)
        m = md5.new()
        m.update(unsigned_data)
        return m.hexdigest()