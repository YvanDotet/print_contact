{
        'name':'Printing of contacts',
        'description':'Provide contacts pdfs reports',
        'summary': "Print contact, print partner, print client, pdf contact, pdf partner, pdf client, ...",
        'author':'Yvan Dotet',
        'depends':['base','contacts'],
        'application':False,        
        'version':'19.0.0.1',
        'license':'AGPL-3',
        'support': 'yvandotet@yahoo.fr',
        'website':'https://github.com/YvanDotet/print_contact',
        
        'data':[
            'report/print_page.xml',
            'report/print_listing.xml',
            'report/print_checkin.xml',
            ],
         
        'images': ['images/thumbnail.png'],
}

