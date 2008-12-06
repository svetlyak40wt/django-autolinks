from setuptools import setup, find_packages

setup(
    name = 'django-autolinks',
    version = __import__('django_autolinks').__version__,
    description = 'App for storing links and automatic '
                  'link extraction from markdown texts.',
    keywords = 'django apps blogging',
    license = 'New BSD License',
    author = 'Alexander Artemenko',
    author_email = 'svetlyak.40wt@gmail.com',
    url = 'http://github.com/svetlyak40wt/django-autolinks/',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Plugins',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    packages = find_packages(),
    include_package_data = True,
)

