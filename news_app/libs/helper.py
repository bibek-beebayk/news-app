import re
from django.template.defaultfilters import striptags
from django.utils import timezone


def today():
    return timezone.localdate()


def smart_truncate(content, length=158, suffix=' …'):
    if len(content) <= length:
        return content
    else:
        return ' '.join(content[:length + 1].split(' ')[0:-1]) + suffix


def get_excerpt(st):
    st = st.replace('&nbsp;', ' ')
    st = striptags(st)
    # Remove tabs
    st = st.replace('\t', '')
    # Combine white spaces
    st = re.sub(r'(\s)\1{1,}', r'\1', st.replace('\r\n', '\n'))
    return smart_truncate(st.strip())