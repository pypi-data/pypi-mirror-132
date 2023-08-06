django-market_graphs
==========

django-market_graphs is a Django app to use for stockanalyser. For each question,
visitors can choose between a fixed number of answers.

Quick start
------------

1. Add "market_graphs" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'market_graphs',
    ]

2. Add the namespace in urlpattern like this::

    urlpatterns = [
    ...
      path('market_graphs/', include('market_graphs.urls', namespace='market_graphs')),
    ]

5. Usage in the template::

    {% load market_graphs_custom_tags %}
    ...
    {% get_market_graphs %}

6. If you want to see appropriate html render, please use bootstrap 5.
