from bs4 import BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')
# The title tag of the page
print(soup.title)
# The title of the page as string
print(soup.title.string)
