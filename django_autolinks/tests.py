from django.test import TestCase
from django_autolinks.utils import extract_links, save_links
from django_autolinks.models import Link

class Autolinks(TestCase):
    def testExtract(self):
        text = '''
               Lorem [ipsum][ipsum wiki] blah [minor][], blah foo bar.
               This is a [second][second post] blah.
               [minor]: http://example.com
               '''
        self.assertEqual([
            dict(slug='minor', url='http://example.com'),
            dict(slug='second post', url=None),
            dict(slug='ipsum wiki', url=None),
            ], extract_links(text))

    def testSave(self):
        links = [
            dict(slug='my site', url='http://aartemenko.com'),
            dict(slug='second post', url=None),
            dict(slug='ipsum wiki', url=None),
            ]
        save_links(links)
        self.assert_(Link.objects.get(slug='my site'))
        self.assertRaises(Link.DoesNotExist, Link.objects.get, slug='second post')

    def testUpdate(self):
        links1 = [dict(slug='my site', url='http://aartemenko.com'),]
        links2 = [dict(slug='my site', url='http://svetlyak.ru'),]
        save_links(links1)
        save_links(links2)
        link = Link.objects.get(slug='my site')
        self.assert_(link)
        self.assertEqual('http://svetlyak.ru', link.url)
