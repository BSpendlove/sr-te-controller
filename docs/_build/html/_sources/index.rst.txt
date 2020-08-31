.. SR-TE Controller documentation master file, created by
   sphinx-quickstart on Mon Aug 31 10:07:02 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

SR-TE Controller (Python) Documentation
=======================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

SR-TE Controller is an attempt to build a very dumb controller that will push a label stack for a specific prefix into the current network and maintain current SR-TE paths via a database without the use of PCEP. (Mainly because I don't know how PCEP works yet, but there is a Go library that works quite well which I might try to implement when I get better at programming)...

Think of this project being various flask apps that run as different containers to provide the communication between a BGP-LS API (ExaBGP) and a frontend which draws out the Link-State topology and allows the user to click fancy buttons to visualize an SR-TE path for a given prefix.

This documentation as of September 2020 will be used just to maintain what outputs you can expect when the application interacts with the ExaBGP JSON data and stores it into a database. This data can then be exposed so you technically have a full Link State database (BGP-LS) at your disposal if you don't want to use the front-end part of this project.


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
