
#Requirments Libraries

from bs4 import BeautifulSoup
import requests
import urllib
from fake_useragent import UserAgent
import pandas as pd


# Operational Data
data = []
data1 = []


main_url = 'https://rabona.com.ua/uk/'
sub_url = 'https://rabona.com.ua/'


#Fake User Agent to Bypass The Security System
ua = UserAgent()
headers = {'User-Agent' : str(ua.chrome)}


# Function For Parse Url's with BS4
def get_soup(url):
    res = requests.get(url, headers=headers, proxies=urllib.request.getproxies())
    return BeautifulSoup(res.text, "html.parser")


#Get All description
def get_descriptions(url, df):

    # Found Main Page
    main__page = get_soup(url)

    # Found The Navbar Block
    navbar = main__page.find('ul',class_='cat-nav-list')

    # Extract all div with appropriate links
    links_block = navbar.findAll('div',class_="cat-nav-item")

    # For Loop to go throw every one in list
    for link in links_block:

        # End Category Link
        category_link = f"https://rabona.com.ua{link.find('a')['href']}"

        # Go to first Category Page
        category_page = get_soup(category_link)

        # Find the pagination block with pages count
        pagination = category_page.find('ul', class_='pagination')
        number_of_pages = pagination.findAll('a')

        # Find the max page in pagination block
        max_page = max([int(link.get_text(strip=True)) for link in number_of_pages if link.get_text(strip=True).isdigit()])

        # For loop to walk every page in each category
        for curr_page in range(1, max_page + 1):

            sep_category_link = f'{category_link}?page={curr_page}'
            sep_category_page = get_soup(sep_category_link)

            # Parse all cards
            card_products = sep_category_page.findAll('div' ,class_='col-sm-3 col-xs-6')

            for product in card_products:

                # Go throw every product link
                product_link = f"https://rabona.com.ua{product.find('div',class_='three_lines_name').find('a')['href']}"
                product_page = get_soup(product_link)

                #Detect product name
                name = product_page.find('div',class_="product-submain").find('h1').text

                #Extract article from name
                article = name.split('(')[-1].replace(')','')

                # Extract description
                description = product_page.find('div',class_='description')
                print(article)
                df.append([article,description])


def convert_to_csv(data, url):

    # Use Pandas to export scraped data into csv file
    df = pd.DataFrame(data, columns=['_MODEL_','_DESCRIPTION_'])
    df.to_csv(url,index=False,columns=['_MODEL_','_DESCRIPTION_'],sep=';')

def remove_incorrect(csv_file_path, output_csv_file_path):

    # Function to extract style attributes from tags in strings

    # Read CSV File
    df = pd.read_csv(csv_file_path,sep=';')

    def clean_html(html):
        if pd.isna(html):  # Check if the value is NaN
            return html # Return the value unchanged
        else:
            soup = BeautifulSoup(html, 'html.parser')

            # Delete all inline-styles
            for tag in soup.find_all():
                if tag.has_attr('style'):
                    del tag['style']

            # Clean <p> with no text
            for p_tag in soup.find_all('p'):
                if not p_tag.text.strip():
                    p_tag.extract()

            return str(soup)

    # Apply function and clean some text
    df['_DESCRIPTION_'] = df['_DESCRIPTION_'].apply(clean_html)

    # Write data to csv
    df.to_csv(output_csv_file_path, index=False,sep=';')

if __name__ == '__main__':

    # Run Functions to scraping data
    get_descriptions(main_url, data)
    convert_to_csv(data, 'C:\\Users\\alexa\\Desktop\Fooball Mall\\TOBRANDS\\RABONA_DESCRIPTION.csv')


    # Clean some incorrect data
    remove_incorrect('C:\\Users\\alexa\\Desktop\\Fooball Mall\\TOBRANDS\\RABONA_DESCRIPTION.csv', 'C:\\Users\\alexa\\Desktop\\Fooball Mall\\TOBRANDS\\DESC_UKR.csv')
