# The main aim of this code it to practice how to get data for all african countries with their
# Various respective administrative Area names and Area Status from https://citypopulation.de/Africa.html

from bs4 import BeautifulSoup
import requests
import csv

r = requests.get('https://citypopulation.de/Africa.html')
data = r.text
list_of_links = BeautifulSoup(data, 'html.parser')

# Prepare CSV writer.

WriteResultsFile = csv.writer(open('CountriesTowns.csv', 'w'))
WriteResultsFile.writerow(['Country', 'Area Status', 'Area Name'])

# Checking if the links are accessible.

try:
    html = r.read()
finally:
    r.close()

    # Looping through the list to get each and every link

    for link in list_of_links.find_all('a'):
        country_links = link.get('href')

        # Getting the tail link so that we can loop the lists obtained above in order to see if it has a php link

    for countries in country_links:
        page_data = requests.get('https://citypopulation.de/'+ countries.text)
        sifter = BeautifulSoup(page_data, 'html.parser')
        for rightpages in sifter.find_all('href'):
            prelinked_pages = requests.get('https://citypopulation.de/'+ rightpages.text)


            # Once the PHP link has been obtained we start getting data

            if prelinked_pages({0: 3} == 'php/'):
                php_links = requests.get('https://citypopulation.de/'+ prelinked_pages.text)

                page_content = BeautifulSoup(php_links, 'html.parser')

                # Harvesting data

                country_name = page_content.find('h1')
                area_status = page_content.find('td', attrs={'itemprop="name': 'name'})

                area_name = page_content.find('td', attrs={'class': 'rstatus'})


                # Writing data into a CSV file

                with open('CountriesTowns.csv', 'a') as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow([country_name, area_status, area_name])

                    writer.writerow.nextcolumn([country_name, area_status, area_name])


                    # Getting data from the regular html files

    page_content = BeautifulSoup(prelinked_pages, 'html.parser')
    country_name = page_content.find('h1')
    area_status = page_content.find('td',
                                    attrs={'itemprop="name': 'name'})
    area_name = page_content.find('td', attrs={'class': 'rstatus'})

    # Writing data into a CSV file

    with open('CountriesTowns.csv', 'a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([country_name, area_status, area_name])
        writer.writerow.nextcolumn([country_name, area_status,area_name])





