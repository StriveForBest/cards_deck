cards_deck
==========

Small python app that has a standard playing cards class with implementation of perfect faro shuffle method.


Requirements
------------

Python > 2.6

Usage
-----

You can use it two different ways. The deck.py file is executable, so if you have python installed you can just run::

    python deck.py

Or you can import it as a module from your app or within python interpreter::

    from deck import Deck

    d = Deck()
    d.shuffle()

    d.print_cards()
