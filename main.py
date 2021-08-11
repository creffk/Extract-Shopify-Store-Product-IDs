import requests, json, re, openpyxl
from bs4 import BeautifulSoup

#load excel file
file = openpyxl.load_workbook("product-urls.xlsx")
urls = file.active

#sheet starting row ID
count = 1

#loop urls in col A in sheet
for row in urls.iter_rows(min_row=2, min_col=1, max_row=356, max_col=1):
    for cell in row:
        cellvalue = cell.value

        #pull out product ID and page titles
        r = requests.get(cellvalue)
        soup = BeautifulSoup(r.content, 'html.parser')

        # finding the tag and css class that contains the required data
        product_data = soup.select('span.shopify-product-reviews-badge')

        #find URL page title
        title = soup.select('title')

        #write row number, url, page title and product ID into txt file
        with open('output-file.txt', 'a+') as f:
            if product_data:
                f.write(str(count))
                f.write("\n")
                f.write(cell.value)
                f.write("\n")
                f.write(str(title[0]))
                f.write("\n")
                f.write('product id' + ' ' + product_data[0]['data-id'])
                f.write("\n")
                f.write( '-' )
                f.write("\n")
    #increment row ID
    count = count + 1



#https://stackoverflow.com/questions/53272999/extract-json-content-in-script-using-beautifulsoup
#https://stackoverflow.com/questions/32474842/attributeerror-resultset-object-has-no-attribute-find-all-beautifulsoup
#https://stackoverflow.com/questions/53884639/python-script-need-to-save-output-to-text-file
#https://openpyxl.readthedocs.io/en/stable/