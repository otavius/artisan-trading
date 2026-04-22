from bs4 import BeautifulSoup

with open("./mock_files/example.html", "r") as file:
    data = file.read()

soup = BeautifulSoup(data, "html.parser")

#print(soup.prettify())

book_entries = soup.find_all("div", class_="book-entry")

for b in book_entries:
    print(b)
    print()

book_entry = soup.find("div", class_="book-entry")
print(book_entry)