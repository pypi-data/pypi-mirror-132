.. -*- mode: rst -*-

|BuildTest|_ |PyPi|_ |License|_ |Downloads|_ |PythonVersion|_

.. |BuildTest| image:: https://travis-ci.com/daniel-yj-yang/Linked_List_lib.svg?branch=main
.. _BuildTest: https://app.travis-ci.com/github/daniel-yj-yang/Linked_List_lib

.. |PythonVersion| image:: https://img.shields.io/badge/python-3.8%20%7C%203.9-blue
.. _PythonVersion: https://img.shields.io/badge/python-3.8%20%7C%203.9-blue

.. |PyPi| image:: https://img.shields.io/pypi/v/Linked_List_lib
.. _PyPi: https://pypi.python.org/pypi/Linked_List_lib

.. |Downloads| image:: https://pepy.tech/badge/Linked_List_lib
.. _Downloads: https://pepy.tech/project/Linked_List_lib

.. |License| image:: https://img.shields.io/pypi/l/Linked_List_lib
.. _License: https://pypi.python.org/pypi/Linked_List_lib


============================================================
Library for Studying and Applying Linked List Data Structure
============================================================

Installation
------------

.. code-block::

   pip install Linked_List_lib

Sample Usage
------------

.. code-block::

   from Linked_List_lib import sll_node # singly linked list node

   curr = head = sll_node(1)
   curr.next = sll_node(2)
   curr = curr.next
   curr.next = sll_node(3)
   curr = curr.next
   curr.next = sll_node(4)
   curr = curr.next
   curr.next = sll_node(5)

   print(head)
   print(head.middle)
   head = head.reversed
   print(head)
   head = head.reversed
   print(head)
