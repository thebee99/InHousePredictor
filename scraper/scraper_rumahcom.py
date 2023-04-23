#BeautifulSoup for managing HTML elements
from bs4 import BeautifulSoup
#Cloudscraper to scrape websites and get HTML content
import cloudscraper
#Pandas for data manipulation
import pandas as pd
#Decimal to convert strings to decimal numbers
from decimal import Decimal
#M = billion, JT = million
d = {
        'b': 3,
        'B': 3,
        't': 6,
        'T': 6,
        'm': 9,
        'M': 9,
}
# Time to check how long the program takes to run
import time
start_time = time.time()

# Function to convert string to number (specifically decimal number)
def text_to_num(text):
        #change all commas to dots
        text = text.replace(',', '.')
        if text[-1] in d:
            # Remove the space between the number and the magnitude
            text = text.replace(' ', '')
            # If the last character is a T, remove the second last character (J)
            if text[-1] == 'T' or text[-1] == 't':
                text = text[:-2] + text[-1]
            # If the last character is a B, remove the second last character (R)
            elif text[-1] == 'B' or text[-1] == 'b':
                text = text[:-2] + text[-1]
            num, magnitude = text[:-1], text[-1]
            return Decimal(num) * 10 ** d[magnitude]
        else:
            return Decimal(text)

# Base URL to scrape
base_url = "https://www.rumah.com/properti-dijual"

#URL for Central Jakarta (Jakarta Pusat)
CENTRALJAKadd_url = 'freetext=Jakarta+Pusat&listing_type=sale&property_type=B&property_type_code[]=BUNG&market=residential&district_code=IDJK02&search=true'
#URL for West Jakarta (Jakarta Barat)
WESTJAKadd_url = 'freetext=Jakarta+Barat&listing_type=sale&property_type=B&property_type_code[]=BUNG&market=residential&district_code=IDJK01&search=true'
#URL for South Jakarta (Jakarta Selatan)
SOUTHJAKadd_url = 'freetext=Jakarta+Selatan&listing_type=sale&property_type=B&property_type_code[]=BUNG&market=residential&search=true'
#URL for East Jakarta (Jakarta Timur)
EASTJAKadd_url = 'freetext=Jakarta+Timur&listing_type=sale&property_type=B&property_type_code[]=BUNG&market=residential&district_code=IDJK04&search=true'
#URL for North Jakarta (Jakarta Utara)
NORTHJAKadd_url = 'freetext=Jakarta+Utara&listing_type=sale&property_type=B&property_type_code[]=BUNG&market=residential&district_code=IDJK05&search=true'
#list of all the additional URLs
add_urls = [CENTRALJAKadd_url, WESTJAKadd_url, SOUTHJAKadd_url, EASTJAKadd_url, NORTHJAKadd_url]
#dictionary to link additional URLs to Jakarta districts
add_url_dict = {CENTRALJAKadd_url: 'CENTRAL', WESTJAKadd_url: 'WEST', SOUTHJAKadd_url: 'SOUTH', EASTJAKadd_url: 'EAST', NORTHJAKadd_url: 'NORTH'}

# List to store the property listings and their links
property_listing_links = []
#target url to identify property listing in HTML elements
property_link_start = 'https://www.rumah.com/listing-properti/'

# Counter to keep track of the page number
page_number = 1

# Make lists to store the data we want to extract``
propertyID = []
propertyName = []
price = []
streetAddress = []
bed = []
bath = []
listing_area = []
certificate = []
propertyLink = []
JAKDIV = []

# Loop until we reach a page with no property listings
for add_url in add_urls:
    while page_number < 100:
        # URL for the current page
        url = base_url + "/{}?".format(page_number) + add_url
        print(url)

        scraper = cloudscraper.create_scraper(delay=10, browser="chrome") 
        content = scraper.get(url).text 
        # Check if the request was successful
        # Check how many occurences of substrings (target link) in string
        soup = BeautifulSoup(content, "html.parser")
        
        # Get the inner content (target content) of the HTML element with class="col-xs-12 col-sm-12 listing-description" or
        # "col-xs-12 col-sm-7 listing-description"
        inner_content1 = soup.select("div.col-xs-12.col-sm-12.listing-description")
        inner_content2 = soup.select("div.col-xs-12.col-sm-7.listing-description")
        #Concatenate the inner content of both HTML elements
        inner_content = inner_content1 + inner_content2
        for content in inner_content:
            # If the property listing didn't put a price, skip it
            if content.select("span.price") == []:
                continue
            # Also, if the page price is a range, skip it
            if "-" in content.select("span.price")[0].text:
                print(content.select("span.price")[0].text)
                continue
            # Add the property ID which is the numbers in the end of the link before the hyphen
            page_property_link = content.select("a.nav-link")
            # The page property link is the href
            page_property_link = page_property_link[0].get('href')
            page_propertyID = page_property_link.split('-')[-1]
            # Add 'rmh.com' to the property ID to make it unique
            page_propertyID = 'rmh.com' + page_propertyID
            propertyID.append(page_propertyID)
            print(page_propertyID)
            # If the property listing is a studio, then the HTML element with class="studio" will be present
            # In this case, the number of bedrooms is 1 and the number of bathrooms is 1
            if content.select("span.studio") != []:
                bed.append("1")
                bath.append("1")
            # Else, the number of bedrooms and bathrooms are in the HTML element with class="bed" and class="bath"
            else:
                # Get all the HTML content with span class="bed"
                page_bed = content.select("span.bed")
                if page_bed != []:
                    bed.append(page_bed[0].text)
                else:
                    bed.append("0")
                # Get all the HTML content with span class="bath"
                page_bath = content.select("span.bath")
                if page_bath != []:
                    bath.append(page_bath[0].text)
                else:
                    bath.append("0")
            # Get all the HTML content with span class="price"
            page_price = content.select("span.price")
            page_price = page_price[0].text
            # Convert number (with magnitude) to corresponding number without magnitude
            page_price = int(text_to_num(page_price))
            price.append(page_price)
            # Get all the HTML content with span itemprop="streetAddress"
            page_streetAddress = content.select("span[itemprop='streetAddress']")
            # The address to be appended is only the item before the second last comma
            # For example, if the address is "Menteng, Jakarta Pusat, DKI Jakarta", then the address to be appended is "Menteng"
            page_streetAddress = page_streetAddress[0].text.split(',')
            page_streetAddress = page_streetAddress[:-2][-1].strip()
            streetAddress.append(page_streetAddress)
            # Get all the HTML content with li class="listing-floorarea pull-left"
            page_listing_area = content.select("li.listing-floorarea.pull-left")
            listing_area.append(page_listing_area[0].text)
            # Get all the HTML content with ul class="listing-property-type" and the second li element
            if content.select("ul.listing-property-type li:nth-of-type(2)") == []:
                certificate.append("None")
            else:
                page_certificate = content.select("ul.listing-property-type li:nth-of-type(2)")
                # If the page certificate is the third element
                if page_certificate[0].text == "Rumah":
                    #Then the certificate is the third element
                    page_certificate = content.select("ul.listing-property-type li:nth-of-type(3)")
                # If the property listing didn't put a certificate, put "None"
                certificate.append(page_certificate[0].text)               
            # Get all the href for the HTML element with class="nav-link" (already got before)
            propertyLink.append(page_property_link)
            # Add the division of Jakarta to the list (as many times as the number of property listings in the page)
            JAKDIV.append(add_url_dict[add_url])
            
        
        # If the length of lists are not equal, then there is a problem -> break the loop
        if len(price) != len(streetAddress) or len(price) != len(bed) or len(price) != len(bath) or len(price) != len(listing_area) or len(price) != len(certificate) or len(price) != len(JAKDIV) or len(price) != len(propertyLink):
            print("Length of lists are not equal")
            print(len(price), len(propertyID), len(streetAddress))
            break
            
        page_number += 1
    page_number = 1


print(len(propertyID), len(price), len(streetAddress), len(bed), len(bath), len(listing_area), len(certificate), len(JAKDIV), len(propertyLink))

# Write the data to a csv file
df = pd.DataFrame({'ID': propertyID, 'Price': price, 'Street Address': streetAddress, 'Bed': bed, 'Bath': bath, 'Listing Area': listing_area, 'Certificate': certificate, 'Jakarta Division': JAKDIV, 'Property Link': propertyLink})
#If there are rows with the same ID, drop them
df.drop_duplicates(subset='ID', keep='first', inplace=True)
#!CHANGE THE FILE NAME HERE
df.to_csv('Rumah.comdataset_v2.csv', index=False, encoding='utf-8')

# Print how long the program took to run in minutes and seconds
print("Time taken to run the program: ", (time.time() - start_time)/60, " minutes and ", (time.time() - start_time)%60, " seconds")




