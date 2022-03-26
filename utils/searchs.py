def torob(query):
    page = requests.get(f"https://torob.com/search/?query={query}")
    soup = BeautifulSoup(page.content, "html.parser")

    firstProduct = soup.find_all("a", {"class" : "jsx-2834913897"})[0]
    return "https://torob.com" + firstProduct['href']