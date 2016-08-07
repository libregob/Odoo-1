{
    'name': "Sythil SAAS Server",
    'version': "1.0",
    'author': "Sythil",
    'category': "Tools",
    'summary':'Share your Odoo instace with others',
    'license':'LGPL-3',
    'data': [
        'views/sythil_saas_server_templates.xml',
        'views/saas_database_views.xml',
        'views/saas_template_database_views.xml',
        'security/ir.model.access.csv',        
    ],
    'demo': [],
    'images':[
        'static/description/3.jpg',
        'static/description/2.jpg',
        'static/description/1.jpg',
        'static/description/4.jpg',
    ],
    'depends': ['website'],
    'installable': True,
}