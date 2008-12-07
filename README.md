django-autolinks
================

A small app, which stores information about websites to which you
links in your preious posts. This application is able to process
your new post, and append an information about such links to the
end of the text.

This piece of code was inspired by [Will Larson's post][lethain] about
blogging and DRY priciple.

Installation
------------

* As usual, use `easy_install django-autolinks` or download sources
  and place django_autolinks somewhere in the pythonpath.
* Next, add `django_autolinks ` to the INSTALLED_APPS.
* Run `./manage.py syncdb`, to create table which will hold information
  about urls.
* Add few lines in your models.py, to process links. It should look like
  this:

    def save(self):
        self.body = process_links(self.body)
        super(TextPost, self).save()

  This simple example was taken right from my another project — [django-dzenlog-text].

Contribution
------------

Feel free to clone [this project at github][django-autolinks] and send me patches or any
suggestions.

[lethain]: http://lethain.com/entry/2008/jan/09/dont-repeat-yourself-bloggers-dynamic-blog-context/
[django-autolinks]: http://github.com/svetlyak40wt/django-autolinks
[django-dzenlog-text]: http://github.com/svetlyak40wt/django-dzenlog-text

