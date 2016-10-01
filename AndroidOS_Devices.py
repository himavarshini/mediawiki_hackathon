
# coding: utf-8

# In[6]:

import pywikibot
import pywikibot.pagegenerators
enwiki = pywikibot.Site(code="en", fam="wikipedia")
androidOS_users = pywikibot.pagegenerators.CategorizedPageGenerator(pywikibot.Category(enwiki, 'Category:Android (operating system) devices'))
                
from pprint import pprint
pprint(list(androidOS_users))

