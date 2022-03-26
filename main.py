import utils.informations as informations
import utils.searchs as searchs
from os import system

searchQuery = input("enter a search query : ")

productLink = searchs.torob(searchQuery)
productInfo = informations.torob(productLink)

system('clear')

print(f"""

Link for this product is : {productLink}\n\n\n\n\n\n

{productInfo['name']}

{"- " * 40}

Minimum price of {searchQuery} is : {productInfo['prices']['minimum']}
Maximum price of {searchQuery} is : {productInfo['prices']['maximum']}

""")