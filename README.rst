itebooks : A python wrapper around http://it-ebooks-api.info/ API
===================================================================

**What is it?**
****************

itebooks is a Python wrapper for the it-ebooks API.

It allows quick and easy comsumption of it-ebooks API from your Python application.

itebooks reqires Python 3.

	
**Install**
***********

You can install itebooks using:

.. code ::

	$ pip3 install itebooks

Build from source

.. code ::
	
	$ git clone https://github.com/aksbuzz/itebooks.git

	$ cd itebooks

	$ make


**Usage**
*********

*API Key*
^^^^^^^^^
For access to the eBook API you would need a API Key.

You can get the API Key from here http://api.eBook.in/

*Using the module*
^^^^^^^^^^^^^^^^^^



.. code :: python
    
    >>> eBook = itebooks.Ebook()

    >>> '''
    	Search the books
    	'''

    >>> search_ = eBook.search("php mysql")

    >>> print(search_.error)
    >>> print(search_.time)
    >>> print(search_.total)
    >>> print(search_.page)

    >>> print(search_.books)

    >>> '''
  	This will return a list of dictionary with following details:

  		ID, 
  		Title, 
  		SubTitle (optional), 
  		Description, 
  		Image
   	'''
 Get book detail
    

    >>> book_ = eBook.book_detail(869476162)

    >>> print(book_.download)

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