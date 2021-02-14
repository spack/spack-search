from urllib.parse import urlparse, parse_qs

from django.conf import settings
from django import template

register = template.Library()


@register.filter
def highlight(value):
    return value.replace("dlopen", "<span class='highlight'>dlopen</span>")


@register.simple_tag
def yield_lines(sourcefile, term=settings.SEARCH_TERM):
    return sourcefile.lines(term)

@register.simple_tag
def update_query_key(url, key, value):
    """ Set or update url query key value """

    parsed_url = urlparse(url)
    parsed_url.query = parse_qs(parsed_url.query).update(
        {
            key: [
                value,
            ]
        }
    )

    print(parsed_url)
