# Simple Web Scraper with Python

A simple web scraper which extract necessary descriptions from the E-Commerce site. The result of my work converted to CSV file, for continuing working with scraped data.

## Main goal

Write a script, which gives need information from the site of our provider.  

## Tools
1. Python
2. BeautifulSoap4
3. Pandas
4. Requests
5. UrlLib
6. FakeUserAgent 

## Description

Firsty, I find the navbar block and gives all categories links

![Group 1](https://github.com/FuckingJester/Web_Scraper/assets/104007930/1208c880-e0af-4d35-a81e-696c3341172f)

Then I go throw every category and gives all products links from each page.

![Group 3](https://github.com/FuckingJester/Web_Scraper/assets/104007930/d25bcf9a-224f-4ce3-927f-227b9a7e1ce8)

The last step is visit evey product page and gives necessary information about the product.

![Group 4](https://github.com/FuckingJester/Web_Scraper/assets/104007930/07b0d93b-004e-4d9f-8ca4-61a4a9c2fe1e)

## Result

In the end file, I get the CSV file with two column _MODEL_ and _DESCRIPTION_


