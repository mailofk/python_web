from requests import get
from bs4 import BeautifulSoup
from extractors.wwr import extract_wwr_jobs
from extractors.indeed import extract_indeed_jobs
from extractors.file import save_to_file

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

browser = webdriver.Chrome(options = options)

keyword = input("찾을 직업 : ")

indeed = extract_indeed_jobs(keyword)
wwr = extract_wwr_jobs(keyword)
jobs = indeed+wwr

save_to_file(keyword,jobs)