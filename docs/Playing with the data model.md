# Playing with the data model
## see tutorial step 3

In the tutorial get some tips how to use the data model

It is easier to play around within a Python file

The next lines should be part of the Python test file

``` {.python}
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()
print('Python %s on %s' % (sys.version, sys.platform))
print('Django %s' % django.get_version())
print("Django Environment variable DJANGO_SETTINGS_MODULE is set to: '%s'" % (os.getenv("DJANGO_SETTINGS_MODULE")))

from polls.models import Question ...
```