import random

#open and read files with first and last names
with open("./web-scraping/firstnames.txt", "r") as f, open("./web-scraping/lastnames.txt", "r") as g:
    fn = [i for i in f]
    ln = [i.capitalize() for i in g]
    
# print random selections of first and last names
first_name = random.choice(fn)
last_name = random.choice(ln)
print(str(first_name) + str(last_name))









