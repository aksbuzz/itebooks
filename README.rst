pyebooks : A python wrapper around http://it-ebooks-api.info/ API
===================================================================

**What is it?**
****************

pyebooks is a Python wrapper for the it-ebooks API.

It allows quick and easy comsumption of it-ebooks API from your Python application.

pyebooks reqires Python 3.


**Install**
***********

You can install pyebooks using:

.. code ::

	$ pip3 install pyebooks

Build from source

.. code ::
	
	$ git clone https://github.com/aksbuzz/pyebooks.git

	$ cd pyebooks

	$ make


**Usage**
*********

*API Key*
^^^^^^^^^
For access to the eBook API you would need a API Key.

You can get the API Key from here http://api.eBook.in/

*Using the module*
^^^^^^^^^^^^^^^^^^

Creating an instance object of class

.. code :: python
	
	>>> from pyebooks import Ebook
	>>> eBook = Ebook(api_key)

Getting details of given PNR number

.. code :: python
	
	>>> eBook.pnr(your_pnr_number)


In any case the object returns
	
	"status" and "result"


**Examples**
************

You can find example usage in the examples folder.

**Contribution**
****************

Contributions are welcome!.

**Documentation**
*****************

Documentation at http://it-ebooks-api.info/

**Todo**
********

- Add Python 2 support
- Add detailed documentation