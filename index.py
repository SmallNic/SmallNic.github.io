import django
from django.conf import settings
from django.template import Template, Context
from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up Django to use standalone templating engine
# @see https://stackoverflow.com/questions/43834226/django-error-no-djangotemplates-backend-is-configured
# @see https://stackoverflow.com/questions/22162027/how-do-i-generate-a-static-html-file-from-a-django-template
TEMPLATES = [{'BACKEND':  'django.template.backends.django.DjangoTemplates'}]
settings.configure(TEMPLATES=TEMPLATES)
django.setup()

html_template = """
<!doctype html>
<html>
  <head>
    <title>Random Daily Image</title>
  </head>
  <link rel="stylesheet" href="style.css">
  <body>
    <img alt="Today's image" src="{{img_src}}"/>
  </body>
</html>
"""

# Use Selenium to scrape Pexels for first image
driver = webdriver.Chrome()
url = 'https://www.pexels.com/'
driver.get(url)
image = driver.find_element(By.CLASS_NAME, 'MediaCard_image__yVXRE')
img_src = image.get_attribute('src')
driver.quit() 

# Populate Django template with scraped image
template = Template(html_template)
context = Context({"img_src": img_src})
populated_template = template.render(context)

# Overwrite index.html file with populated template
file = open("index.html", "w")
file.write(populated_template)
file.close()