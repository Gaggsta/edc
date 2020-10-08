import requests
import schedule
import time
from bs4 import BeautifulSoup
import logging

logging.basicConfig(
    format='%(asctime)s - %(message)s')


def getter():
    req = requests.get("https://status.ecwid.com/")
    if req.status_code == 200:
        soup = BeautifulSoup(req.text, 'html.parser')
        indicators = soup.find_all(
            'div', class_='component-container border-color')
        for indicator in indicators:
            spans = indicator.find_all("span")
            spans = [span.text.strip() for span in spans]
            logging.warning(f"{spans[0]} is {spans[1]}")
            if spans[1] != 'Operational':
                logging.error(f"ATTENTION - {spans[0]}:{spans[1]}")


schedule.every(10).minutes.do(getter)

while True:
    schedule.run_pending()
    time.sleep(1)
