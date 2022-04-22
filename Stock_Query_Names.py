from bs4 import BeautifulSoup
import requests
import time

stock_query = input("Insert the name of the stock you would like to search: ")

class Stock(object):
    def __init__(self,user_input):
        self.user_input =  'https://site.financialmodelingprep.com/search?q='+ user_input


    def display_stock_info(self):

        """
        The below uses the 'requests.get()' method from the request library it
        will 'get()' the url and will assign the '.text' of the html to the
        variable, 'html_text'
        """
        html_text = requests.get(self.user_input).text

        """
        The 'soup' variable contains the 'html_text' after 'BeautifulSoup()' has formatted it so that
        the 'bs4' library can use their methods like "find_all()" to find all of a certain element in
        the 'html_text'
        """

        soup = BeautifulSoup(html_text, "html.parser")

        """
        'find_all()' the <tr> elements in the html and recognize them as rows
        """
        table_rows = soup.find_all("tr")

        """
         look at each row
        """

        for each_row in table_rows:
            """
            'find_all()' the <td> elements in the one <tr> element.
            """
            cells = each_row.find_all("td")
            """
            if the '<tr>' we are looking at does not have (6) points of
            data (Word, Symbol, Name, Price, Change, ChangePercent),
            then the "for" loop will pass on to find the next <tr> element
            """
            if not cells:
                continue
            """
            All cells in the row are assigned a variable (Word, Symbol, Name, Price, Change, ChangePercent)
            """
            Word, Symbol, Name, Price, Change, ChangePercent = cells
            """
            the 'Name' variable consists of the entire <td> element. This will strip
            everything but the text part of the html sting that was stored in 'Name'.
            """
            Name = Name.text.strip()
            print(Name)




a_stock = Stock(stock_query)
a_display = a_stock.display_stock_info()
