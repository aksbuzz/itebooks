import pyebooks


if __name__ == '__main__':

    '''
    creata a new eBook object.
    '''
    
    eBook = pyebooks.Ebook()

    '''
    Search the books
    '''

    search_ = eBook.search("php mysql")

    print(search_.error)
    print(search_.time)
    print(search_.total)
    print(search_.page)
    print(search_.books)

    '''
    Get book detail
    '''

    book_ = eBook.book_detail(869476162)

    print(book_.download)