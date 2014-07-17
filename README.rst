========
robotars
========

.. image:: https://img.shields.io/travis/eldarion/robotars.svg
    :target: https://travis-ci.org/eldarion/robotars

.. image:: https://img.shields.io/coveralls/eldarion/robotars.svg
    :target: https://coveralls.io/r/eldarion/robotars

.. image:: https://img.shields.io/pypi/dm/robotars.svg
    :target:  https://pypi.python.org/pypi/robotars/

.. image:: https://img.shields.io/pypi/v/robotars.svg
    :target:  https://pypi.python.org/pypi/robotars/

.. image:: https://img.shields.io/badge/license-BSD-blue.svg
    :target:  https://pypi.python.org/pypi/robotars/


Generate robot avatars with optional support for being a gravatar
fallback.

Usage:

::

  {% load robotars_tags %}
  {% robotar "bob@example.org" %}
  {# with gravatar fallback and size #}
  {% robotar "bob@example.org" "63x63" 1 1 %}

You can optionally pass the following arguments:

* size: The size of the robohash to be generated. eg "63x63"
* gravatar_fallback: whether robohash should be the fallback for the
  gravatar service
* hashed: whether your user's email address should be obscured from
  robohash.
