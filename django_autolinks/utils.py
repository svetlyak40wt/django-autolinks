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
    for link in links:
        try:
            obj = Link.objects.get(slug=link['slug'])
            link['url'] = obj.url
        except Link.DoesNotExist:
            pass
    return links

def separate_links(links):
    '''Returns tuple with two lists.
       First list contains all links with URLs
       and second list contains links without URSs.'''

    return (
            [link for link in links if link['url'] is not None],
            [link for link in links if link['url'] is None]
           )

def process_links(text):
    links_with_urls, links_without_urls = separate_links(
                                            extract_links(text))
    save_links(links_with_urls)
    load_links(links_without_urls)

    return text + ''.join('\n[%(slug)s]: %(url)s' % link for link in links_without_urls)

