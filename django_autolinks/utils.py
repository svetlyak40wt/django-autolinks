import re

from models import Link

MD_SLUG1 = r'.*\[[^]]+\]\[([^]]+)\].*'
MD_SLUG2 = r'.*\[([^]]+)\]\[\].*'
MD_LINK  = r'.*\[([^]]+)\]: ([^ \n]+).*'

def extract_links(text):
    slugs  = set(re.findall(MD_SLUG1, text))
    slugs.update(re.findall(MD_SLUG2, text))
    links  = [dict(zip(('slug', 'url'), m))
                for m in re.findall(MD_LINK, text)]
    for link in links:
        try:
            slugs.remove(link['slug'])
        except KeyError:
            pass
    links += [dict(slug = slug, url = None)
                for slug in slugs if slug]
    return links

def save_links(links):
    for link in links:
        if link['url'] is not None:
            obj, created = Link.objects.get_or_create(slug = link['slug'])
            obj.url = link['url']
            obj.save()

def load_links(links):
    return links

