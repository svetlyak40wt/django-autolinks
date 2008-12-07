from django.test import TestCase
from django_autolinks.utils import *
from django_autolinks.models import Link

class Autolinks(TestCase):
    def setUp(self):
        self.first_text = '''
               [Minor example][minor] of autolinks.
               This is a [my second post][second post].

               [minor]: http://example.com
               [second post]: http://second.ru
               '''

        self.second_text = '''
               Lorem [ipsum][ipsum wiki] blah [minor][], blah foo bar.
               This is a [second][second post] blah.

               [ipsum wiki]: http://wiki.com
               '''
        Link.objects.all().delete()

    def testExtract(self):
        self.assertEqual([
            dict(slug='ipsum wiki', url='http://wiki.com'),
            dict(slug='second post', url=None),
            dict(slug='minor', url=None),
            ], extract_links(self.second_text))

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

    def testLoad(self):
        links1 = [dict(slug='my site', url='http://aartemenko.com'),]
        links2 = [dict(slug='my site', url=None),]
        save_links(links1)

        self.assertEqual(None, links2[0]['url'])
        load_links(links2)
        self.assertEqual('http://aartemenko.com', links2[0]['url'])

    def testSeparation(self):
        all = [ dict(slug='ipsum wiki', url='http://wiki.com'),
                dict(slug='second post', url=None),
                dict(slug='minor', url=None), ]
        without_urls = [ dict(slug='second post', url=None),
                         dict(slug='minor', url=None), ]
        with_urls = [ dict(slug='ipsum wiki', url='http://wiki.com'), ]

        self.assertEqual(
            (with_urls, without_urls),
            separate_links(all))

    def testMagick(self):
        result = self.second_text + ''.join((
                    '\n[second post]: http://second.ru',
                    '\n[minor]: http://example.com',))

        self.assertEqual(
            self.first_text,
            process_links(self.first_text))

        self.assertEqual(
            result,
            process_links(self.second_text))

