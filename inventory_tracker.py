#!usr/bin/env python3
#Jacob Foppes  Blog Post 6 Inventory Tracker 
'''This is an inventory and order processing applkication for a warehouse of an online retialer
this program accepts an order frm an online website, generates a pick for the warehouse team, and adjust stock levels accourindly'''

''''1. inventory controll system this should be stored in  a fucntion/loop and run contantly i nthe BKG to continually update invenroty '''

onHand = {'itemName':'(QTY)', 'redBox':80, 'GreenBox':60, 'xbox':100}
targetStock = {'itemName':'(QTY)', 'redBox':80, 'GreenBox':100, 'xbox':120}
onOrder = {'itemName':'(QTY)', 'redBox':0, 'GreenBox':40, 'xbox':20}

for key in onHand:
    if key["itme"] < targetStock["item"]:
        pass # order the diffence between the 2 values 
    
    
'''2. Incomming orders '''

#let assume the web order comes in a a txt file
order = open("order.txt")
for i in order:
    pass # takes lines and sets them as variesbale 
last = ""
first = ""
orderid = ""
email = ""
phoneum = ""
addy = ""
items = []
# subdevide order line by line into parts that are later combined into dictionary  dictionary with embeded tupl,e and subdictionary of items in order
'''{'orderID':12345654321,
               'customerInfo':[smith, John, jsmith@me.com, 4208675309,(address)],
               items:{'itemName':'(QTY)', 'redBox':4, 'GreenBox':6, 'xbox':1}}'''
sample_ord = {'orderID':orderid,
               'customerInfo':[last, first, email, phoneum,(addy)],
               items:{'itemName':'(QTY)', 'redBox':4, 'GreenBox':6, 'xbox':1}}

'''3. ORder processing '''
# this section will be where the order i sprocessed and subtracted from the onhand count 

# the order is then archied once confirmation is recieed that it has ben packed 
    
    
    
    
