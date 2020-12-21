from bs4 import BeautifulSoup
import requests
import time

source_url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python'


def find_jobs(url):
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for job in jobs:
        company = job.find('h3', class_='joblist-comp-name').text.replace(' ', '').strip()
        skills = job.find('span', class_='srp-skills').text.replace(' ', '').strip()
        published = job.find('span', class_='sim-posted').text.strip()
        link = job.header.h2.a['href']

        # print(skills)
        print(f'''Company: {company}\nSkills: {skills}\nPublished: {published}\nLink: {link}\n''')


if __name__ == '__main__':
    while True:
        find_jobs(source_url)
        print(f"Waiting 10 min")
        time.sleep(600)
