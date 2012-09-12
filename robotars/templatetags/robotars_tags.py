# http://robohash.org/

from django import template
from md5 import md5


register = template.Library()


@register.inclusion_tag("robotars/robotar.html")
def robotar(user, size=None, gravatar_fallback=False, hashed=False):
    url = "http://robohash.org/"
    if gravatar_fallback:
        if hashed:
            url += "%s?gravatar=hashed&" % md5(user.email).hexdigest()
        else:
            url += "%s?gravatar=yes&" % user.email
    else:
        url += "%s?" % user
    if size is not None:
        url += 'size=%s' % size
    return {"robotar_url": url, "robotar_user": user}
