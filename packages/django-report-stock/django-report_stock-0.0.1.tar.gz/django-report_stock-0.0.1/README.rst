django-report_stock
==========

django-report_stock is a Django app to use for stockanalyser. For each question,
visitors can choose between a fixed number of answers.

Quick start
------------

1. Add "report_stock" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'fav_stock',
        'report_stock',
    ]

2. Run below command to create the fav_stock models.::

    python manage.py makemigrations fav_stock
    python manage.py migrate
    python manage.py createsuperuser

3. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a fav_stock (you'll need the Admin app enabled).

4. Add the namespace in urlpattern like this::

    urlpatterns = [
    ...
      path('fav_stock/', include('fav_stock.urls', namespace='fav_stock')),
      path('report_stock', include('report_stock.urls', namespace='report_stock')),
    ]

5. Usage in the template::

    {% load report_stock_custom_tags %}
    ...
    {% get_report code="005490" %}

6. If you want to see appropriate html render, please use bootstrap 5.
