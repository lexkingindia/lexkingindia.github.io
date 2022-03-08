"""
Lexking Official Product Adder
License: MIT
Author: Aasheesh Agarwal
Website: lexkingofficial.github.io

* Uses Python


Keywords to edit:

Product Template:
[name]: Toilet Cleaner 500 ML
[fullname]: Lexking Disinfectant Toilet Cleaner 500 ML
[description]: Description....
[amount]: ₹89
[amazon_buy]: y OR n
[amazon_buy_url]: The amazon buy url (optional)

Browser Template:
[more-product]: The code to be replaced by the new product
[fullname]: Lexking Disinfectant Toilet Cleaner 500 ML
[slug]: toilet500ml
[name]: Toilet Cleaner 500 ML
[product-small-type-size]: Toilet Cleaner 500 ML
[image]: The image url
[filter]: The type of product, will filter in browser.


Browser Template HTML Code: <div class="col-lg-4 col-md-6 portfolio-item filter-cleaner"><div class="portfolio-wrap"><img alt="[fullname]" class="img-fluid" src="[image]"><div class="portfolio-links"><a href="[slug]" title="More Details"><span class="material-icons-outlined open_in_new">open_in_new<br><br><br><br></span></a></div><div class="portfolio-info col-lg-12"><h4>[name]</h4><p>[product-type-full]<br><b>[product-small-type-size]</b></p></div></div>

[name] [fullname] [description] [amount] [amazon_buy]
[more-product] [fullname] [slug] [name] [product-small-type-size] [image]
"""

files = [[None,None],None]
product_template = "products\\template.html"
product_directory = "products"

def read(file):
	files[0][0] = open(file,"r")
	files[0][1] = files[0][0].read()
	files[0][0].close()
	return files[0][1]

def write(file,value):
	files[1] = open(file,"w")
	files[1].write(value)
	files[1].close()

def isTrue(value):
	if value == 1 or value == "1" or value.lower() == "y" or value.lower() == "yes" or value:
		return True
	else:
		return False

def isFalse(value):
	if value == 1 or value == "1" or value.lower() == "y" or value.lower() == "yes" or value:
		return False
	else:
		return True

name = input("Product Name Like Toilet Cleaner 500 ML: ")
fullname = input("Full name with lexking disinfectant, size, flavour: ")
description = input("Full description: ")
amount = input("Amount containing rupees sign: ")
amazon_buy = input("If is on amazon, type y else n: ")
amazon_buy_url = input("If on amazon, type url else skip: ")
if isTrue(amazon_buy):
	amazon_buy = True
else:
	amazon_buy = False
image = input("URL of the image: ")
slug = input("Slug that would be file name: ")
feature = input("Show in the Homepage? Y/N: ")
if isTrue(feature):
	feature = True
else:
	feature = False
filter_class = input("Type f for floor cleaner, g for glass cleaner, t for toilet cleaner and o for others (this will show in the products browser): ").lower()
if filter_class == "f":
	filter_class = "filter-cleaner"
elif filter_class == "t":
	filter_class = "filter-toilet"
elif filter_class == "g":
	filter_class = "filter-glass"
elif filter_class == "o":
	filter_class = "filter-others"

if isTrue(amazon_buy):
	amazon_buy_template = '<a href="[url]" target="_blank"><button class="buya">Buy on Amazon</button></a>'
else:
	amazon_buy_template = '<button class="buya" disabled>Buy on Amazon [ Not Available ]</button>'

product_source = read(product_template)
product_source = product_source.replace("[name]",name)
product_source = product_source.replace("[fullname]",name)
product_source = product_source.replace("[description]",description)
product_source = product_source.replace("[amount]",amount)
product_source = product_source.replace("[amazon_buy]",amazon_buy_template)
product_source = product_source.replace("[image]",image)
write("products\\{slug}.html".format(slug=slug),product_source)
print("Successfully Built Full Page. Now adding to browser...")

product_flavour = input("Flavour like Lexking Disinfectant Toilet Cleaner: ")

browser_source = read("products\\browse.html")
browser_template_source = '<!-- [more-product] -->\n<div class="col-lg-4 col-md-6 portfolio-item filter-cleaner"><div class="portfolio-wrap"><img alt="[fullname]" class="img-fluid" src="[image]"><div class="portfolio-links"><a href="[slug]" title="More Details"><span class="material-icons-outlined open_in_new">open_in_new<br><br><br><br></span></a></div><div class="portfolio-info col-lg-12"><h4>[name]</h4><p>[product-type-full]<br><b>[product-small-type-size]</b></p></div></div>'
browser_template_source = browser_template_source.replace("[fullname]",fullname)
browser_template_source = browser_template_source.replace("[image]",image)
browser_template_source = browser_template_source.replace("[slug]",slug)
browser_template_source = browser_template_source.replace("filter-cleaner",filter_class)
browser_template_source = browser_template_source.replace("[name]",name)
browser_template_source = browser_template_source.replace("[product-type-full",product_flavour)
browser_template_source = browser_template_source.replace("[product-small-type-size]",name)

browser_source = browser_source.replace("<!-- [more-product] -->",browser_template_source)

write("products\\browse.html",browser_source)
print("Successfully added to browser. Now adding to homepage if its...")
if feature:
	home_template = browser_template_source.replace("<!-- [more-product] -->","<!-- [featured-product] -->")
	home_source = read("index.html").replace("<!-- [featured-product] -->",home_template)
	write("index.html",home_source)
	print("Successfully added to homepage.")
else:
	print("Skipping adding to homepage as you declined.")
print("Product Add completed successfully.")