# http://robohash.org/

from django import template
from hashlib import md5


register = template.Library()


@register.inclusion_tag("robotars/robotar.html")
def robotar(user, size=None, gravatar_fallback=False, hashed=False):
    url = "//robohash.org/"
    if gravatar_fallback:
        email = user.email.lower()
        if hashed:
            url += "%s?gravatar=hashed&" % md5(email).hexdigest()
        else:
            url += "%s?gravatar=yes&" % email
    else:
        url += "%s?" % user
    if size is not None:
        if size.isdigit():
            size = "%sx%s" % (size, size)
        url += 'size=%s' % size
    return {"robotar_url": url, "robotar_user": user}
