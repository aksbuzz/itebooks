"""

A python wrapper for the it-books web API. 

Copyright @ 2017 

Akshay

"""

import helpers


class Ebook(object):
    """
    Ebook class to create a new ebppk instance.
    """
    # Base URL

    end_point = 'http://it-ebooks-api.info/v1/'

    def __init__(self):

        pass

    def search(self, query_string, page_number=1):

        assert len(query_string) <= 50

        url = self.end_point + \
            '/search/{}/page/{}'.format(query_string, page_number)

        response = helpers.get_json(url)

        self.error = response.get("Error", None)
        self.time = response.get("Time", None)
        self.total = response.get("Total", None)
        self.page = response.get("Page", None)
        self.books = response.get("Books", None)


    def book_detail(self, id_):

        url = self.end_point + '/book/{}'.format(id_)

        response = helpers.get_json(url)

        self.error = response.get("Error", None)
        self.time = response.get("Time", None)
        self.id_ = response.get("ID", None)
        self.title = response.get("Title", None)
        self.subtitle = response.get("SubTitle", None)
        self.description = response.get("Description", None)
        self.author = response.get("Author", None)
        self.isbn = response.get("ISBN", None)
        self.page = response.get("Page", None)
        self.year = response.get("Year", None)
        self.publisher = response.get("Publisher", None)
        self.image = response.get("Image", None)
        self.download = response.get("Download", None)

if __name__ == '__main__':
    
    ebook = Ebook()

    ebook.search("python")

    print(ebook.total)
    
    print(ebook.books)