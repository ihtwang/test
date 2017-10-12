from selenium import webdriver
from lettuce import before, world
import lettuce_webdriver.webdriver
@before.all
def setup_browser():
    world.browser = webdriver.Firefox()
