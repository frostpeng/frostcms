#coding=utf-8
from pyramid.authentication import AuthTktCookieHelper
from pyramid.security import Everyone, Authenticated
from zope.interface import implementer

from pyramid.interfaces import IAuthenticationPolicy

from .token import Token
from logging import getLogger
log = getLogger(__name__)

@implementer(IAuthenticationPolicy)
class AuthenticationPolicy(object):
    """ A :app:`Pyramid` :term:`authentication policy` which
    obtains data from a Pyramid "auth ticket" cookie.

    Constructor Arguments

    ``secret``

       The secret (a string) used for auth_tkt cookie signing.
       Required.

    ``cookie_name``

       Default: ``auth_tkt``.  The cookie name used
       (string).  Optional.

    ``secure``

       Default: ``False``.  Only send the cookie back over a secure
       conn.  Optional.

    ``include_ip``

       Default: ``False``.  Make the requesting IP address part of
       the authentication data in the cookie.  Optional.

    ``timeout``

       Default: ``None``.  Maximum number of seconds which a newly
       issued ticket will be considered valid.  After this amount of
       time, the ticket will expire (effectively logging the user
       out).  If this value is ``None``, the ticket never expires.
       Optional.

    ``reissue_time``

       Default: ``None``.  If this parameter is set, it represents the number
       of seconds that must pass before an authentication token cookie is
       automatically reissued as the result of a request which requires
       authentication.  The duration is measured as the number of seconds
       since the last auth_tkt cookie was issued and 'now'.  If this value is
       ``0``, a new ticket cookie will be reissued on every request which
       requires authentication.

       A good rule of thumb: if you want auto-expired cookies based on
       inactivity: set the ``timeout`` value to 1200 (20 mins) and set the
       ``reissue_time`` value to perhaps a tenth of the ``timeout`` value
       (120 or 2 mins).  It's nonsensical to set the ``timeout`` value lower
       than the ``reissue_time`` value, as the ticket will never be reissued
       if so.  However, such a configuration is not explicitly prevented.

       Optional.

    ``max_age``

       Default: ``None``.  The max age of the auth_tkt cookie, in
       seconds.  This differs from ``timeout`` inasmuch as ``timeout``
       represents the lifetime of the ticket contained in the cookie,
       while this value represents the lifetime of the cookie itself.
       When this value is set, the cookie's ``Max-Age`` and
       ``Expires`` settings will be set, allowing the auth_tkt cookie
       to last between browser sessions.  It is typically nonsensical
       to set this to a value that is lower than ``timeout`` or
       ``reissue_time``, although it is not explicitly prevented.
       Optional.

    ``path``
 
       Default: ``/``. The path for which the auth_tkt cookie is valid.
       May be desirable if the application only serves part of a domain.
       Optional.
 
    ``http_only``
 
       Default: ``False``. Hide cookie from JavaScript by setting the
       HttpOnly flag. Not honored by all browsers.
       Optional.

    ``wild_domain``

       Default: ``True``. An auth_tkt cookie will be generated for the
       wildcard domain.
       Optional.

    Objects of this class implement the interface described by
    :class:`pyramid.interfaces.IAuthenticationPolicy`.
    """
    def __init__(self, 
                 secret,
                 cookie_name='auth_tkt',
                 callback = None,
                 secure=False,
                 include_ip=False,
                 timeout=None,
                 reissue_time=None,
                 max_age=None,
                 path="/",
                 http_only=False,
                 wild_domain=True):
        self.cookie = AuthTktCookieHelper(
            secret,
            cookie_name=cookie_name,
            secure=secure,
            include_ip=include_ip,
            timeout=timeout,
            reissue_time=reissue_time,
            max_age=max_age,
            http_only=http_only,
            path=path,
            wild_domain=wild_domain,
            )
        self.secret = secret
        self.callback = callback
        
    def unauthenticated_userid(self, request):
        token = request.params.get('access_token')
        
        if token:
            t = Token()
            
            obj = t.decode(token)
            if obj:
                return obj['userid']
        result = self.cookie.identify(request)
        if result:
            return result['userid']

    def remember(self, request, principal, **kw):
        """ Accepts the following kw args: ``max_age=<int-seconds>,
        ``tokens=<sequence-of-ascii-strings>``"""
        return self.cookie.remember(request, principal, **kw)

    def forget(self, request):
        return self.cookie.forget(request)
    
    def authenticated_userid(self, request):
        if request.user:
            return request.user.id
        
    def effective_principals(self, request):
        principals = [Everyone]
        user = request.user
        if user:
            principals += [Authenticated, '%s' % user.id]
            if self.callback:
                principals.extend(('%s' % g for g in self.callback(user.id, request)))
        return principals