Date-offset
==============
.. image:: https://badge.fury.io/py/date-offset.svg
    :target: http://badge.fury.io/py/date-offset


.. image:: https://codecov.io/gh/django-advance-utils/date-offset/branch/main/graph/badge.svg?token=QPGW5TIGX3
    :target: https://codecov.io/gh/django-advance-utils/date-offset
    
This allow you to offset time with a string.

Example

.. code-block::

    d = DateOffset()
    tomorrow = d.get_offset("1d")
    yesterday = d.get_offset("-1d")



Keyword

* # start of week (Monday)
* \* end of week
* % first day of the month
* d offset by days (1d)
* w offset by weeks (1w)
* m offset by months (1m)
* ~ not weekend
* t time (10t = 10hr. 10:15t = 10hr 15mins. 10:15:45t = 10hr 15mins 45secs)
    
Nested string can be used

.. code-block::

    d = DateOffset()
    second_day_of_current_month = d.get_offset("%1d")
