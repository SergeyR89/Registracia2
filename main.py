from time import sleep
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options


def log_in():
    urls = input('URL link: ')
    ua = UserAgent()
    agent = ua.chrome
    optins = Options()
    optins.set_preference('dom.webdriver.enabled', False)
    optins.set_preference('media.volume_scale', '0.0')
    optins.set_preference('dom.ipc.processCount', 3)
    optins.set_preference('toolkit.cosmeticAnimations.enabled', False)
    optins.set_preference('general.useragent.override', agent)
    optins.set_preference('browser.sessionstore.max_tabs_undo', 2)
    optins.set_preference('browser.sessionhistory.max_entries', 10)
    optins.set_preference('browser.sessionhistory.max_total_viewers', 4)
    optins.set_preference('geo.enabled', False)
    optins.set_preference('network.prefetch-next', False)
    optins.set_preference('media.cache_size', 128000)

    serves = Service(executable_path='Draiver/geckodriver.exe')
    driver = webdriver.Firefox(service=serves, options=optins)
    driver.delete_all_cookies()

    driver.get(url=urls)
# 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


def main():
    log_in()


if __name__ == '__main__':
    main()