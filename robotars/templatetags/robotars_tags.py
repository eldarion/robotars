# http://robohash.org/

from django import template
from md5 import md5


register = template.Library()


@register.inclusion_tag("robotars/robotar.html")
def robotar(user, size=None, gravatar_fallback=False, hashed=False):
    _user = user
    if hashed:
        _user = md5(user).hexdigest()
    url = "http://robohash.org/%s?" % _user
    if size is not None:
        url += 'size=%s' % size
    if gravatar_fallback:
        sep = "?"
        if "?size=" in url:
            sep = "&"
        url += "%sgravatar=%s" % (sep, "hashed" if hashed else "yes")
    return {"robotar_url": url, "robotar_user": user}
