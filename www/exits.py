# exits.py 
"""Creates a dictionary of page exit names to manage the links used in Templates"""

def get_exits():
    the_exits = { "home": "/",
        "about": "/about",
        "contact": "/contact",
        "links": "/links",
        "prices": "/prices",
        "product": "/product",
        "displayInfo": "/displayInfo",
        "parkingInfo": "/parkingInfo",
        "emailSales": "sales@lindcraftracks.biz",
        "emailAddress": "sales@lindcraftracks.biz",
        }
    return the_exits