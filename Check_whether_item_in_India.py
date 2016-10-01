
# coding: utf-8

# In[45]:

import pywikibot
wikidata = pywikibot.Site('wikidata', 'wikidata')
itempage = pywikibot.ItemPage(wikidata, "Q62")
itemdata = itempage.get()
itemdata.keys()
itemdata['claims']
itempage.claims['P17']
p17_claim_target = itempage.claims['P17'][0].getTarget()
p17_claim_target.get()
p17_claim_target.labels['en'] == 'India'

