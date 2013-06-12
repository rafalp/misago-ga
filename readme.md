# Misago Google Analytics

Small and simple plugin that adds [Google Analytics](https://www.google.com/analytics) tracking script to your [Misago](http://misago-project.org) forum.

Installation
------------

Put `misagoga` directory under your python path, then add following entries to your installation settings:

### INSTALLED_APPS
```python
'misagoga'
```

### TEMPLATE_MIDDLEWARES
```python
'misagoga.templatemiddleware.GoogleAnalyticsMiddleware'
```

After that, add path to misagoga templates to your `TEMPLATE_DIRS`.

Finally, set add following code to your config:

```python
# Google Analytics ID
GOOGLE_ANALYTICS_ID = 'YOUR GOOGLE ANALYTICS ID'
```

Don't forget to replace "YOUR GOOGLE ANALYTICS ID" with your Analytics service ID, you'll find it your GA control panel.

Can't find INSTALLED_APPS or TEMPLATE_MIDDLEWARES?
--------------------------------------------------

This would mean you haven't installed any extensions to your Misago. To expose those settings, add following codes at the end of your settings.py:

```python
INSTALLED_APPS += (
    'misagoga',
)

TEMPLATE_MIDDLEWARES += (
    'misagoga.templatemiddleware.GoogleAnalyticsMiddleware',
)
```

Same pattern goes for `TEMPLATE_DIRS` except it should already be defined in your settings.py

Authors
-------

**Rafał Pitoń**

+ http://rpiton.com
+ http://github.com/ralfp
+ https://twitter.com/RafalPiton


Copyright and license
---------------------
 
> This program comes with ABSOLUTELY NO WARRANTY.  
> This is free software and you are welcome to redistribute it under the conditions described in the license.
>
> For the complete license, refer to [LICENSE.md](LICENSE.md)
