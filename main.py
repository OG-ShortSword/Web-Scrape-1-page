import requests
from bs4 import BeautifulSoup
import sys


def find_jobs():
    html_text = requests.get('https://www.reed.co.uk/jobs/jobs-in-bristol').text  # Importing the library Requests assigning a value "html_text" "reqeust.get" is accessing the library and using the function "get"(to retrieve) then we use ".text" to tell the program how to interpret the information coming.
    soup = BeautifulSoup(html_text, 'lxml')  # Importing the library Beautifulsoup and assigning a value of 'soup' to call upon beautifulsoup throughout the program. passing 'html_text' to process the data from the job website
    full_info = soup.find_all('div', class_='col-sm-12 col-md-9 details')  # Telling Beautifulsoup where to look for the information required and assigning a variable 'full_info' for it to be called upon later in the program
    for index, info in enumerate(full_info):
        location = info.find('li', class_='job-metadata__item job-metadata__item--location').text.replace(' ', '')
        job = info.find('h3', class_='job-result-heading__title').text.replace(' ', '')
        company_name = info.find("a", class_='gtmJobListingPostedBy').text.replace(' ', '')
        salary_amount = info.find('li', class_='job-metadata__item job-metadata__item--salary').text.replace(' ', '')

        with open(f'posts/{index}.txt', 'w') as f:
            f.write(f"Company Name: {company_name.strip()}")
            f.write(f"Job Title: {job.strip()}")
            f.write(f"Salary: {salary_amount}")
            f.write(f"Location: {location.strip()}")
        print(f'File saved as: {index}')


if __name__ == '__main__':  # use main like it is in C++ to call the functions into a loop
    while True:
        find_jobs()
        print('Jobs found!! Terminating program.')
        sys.exit()
