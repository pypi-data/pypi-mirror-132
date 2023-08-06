=====
Banner
=====

Banner is a Django app to add and manage banners for a site.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "banner" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'banner',
    ]

2. Add the following context processors to your OPTIONS::

    'OPTIONS': {
        'context_processors': [
            ...
            'banner.processors.banner_endpoint',
            'banner.processors.banner_sidebar_right',
            'banner.processors.banner_sidebar_left',
            'banner.processors.banner_content',
            'banner.processors.banner_bottom',
            'banner.processors.banner_top'
        ]
    }

3. Include the banner URL conf in your project urls.py like this::

    path('banner/', include('banner.urls')),

4. Run ``python manage.py migrate`` to create the banner models.

5. Start the development server and visit http://localhost:/admin/
   to create a banner (you'll need the Admin app enabled).
