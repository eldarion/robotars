# http://robohash.org/

from django import template


register = template.Library()


@register.inclusion_tag("robotars/robotar.html")
def robotar(user, size=None):
    url = "http://robohash.org/%s" % user
    if size is not None:
        url += "?size=%s" % size
    return {"robotar_url": url, "robotar_user": user}