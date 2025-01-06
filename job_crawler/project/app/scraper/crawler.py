from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import random
from ..models import JobPosting, Profile

class LinkedInScraper:
    def __init__(self):
        self.setup_driver()

    def setup_driver(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
        
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )

    def scrape_jobs(self, keywords, location, num_jobs=20):
        jobs = []
        search_url = f"https://www.linkedin.com/jobs/search/?keywords={keywords}&location={location}"
        self.driver.get(search_url)
        
        time.sleep(random.uniform(2, 5))
        
        job_cards = self.driver.find_elements(By.CLASS_NAME, "job-card-container")
        
        for card in job_cards[:num_jobs]:
            try:
                title = card.find_element(By.CLASS_NAME, "job-title").text
                company = card.find_element(By.CLASS_NAME, "company-name").text
                location = card.find_element(By.CLASS_NAME, "job-location").text
                
                job = JobPosting(
                    title=title,
                    company=company,
                    location=location,
                    url=card.get_attribute("href")
                )
                jobs.append(job)
            except Exception as e:
                print(f"Error scraping job: {e}")
                
        return jobs

    def scrape_profiles(self, job_title, location, num_profiles=5):
        profiles = []
        return profiles

    def __del__(self):
        if hasattr(self, 'driver'):
            self.driver.quit()
