{
    'name': 'ViettelPost Connection Core',
    'version': '15.0.1.0',
    'summary': 'Provide connection core for add-ons ViettelPost Connector.',
    'description': """
        The ViettelPost Connection Core module is a crucial component that enables the proper functioning of a system that requires connectivity with the ViettelPost service. This module serves as a bridge between the system and the ViettelPost service, allowing the exchange of data and information.
    """,
    'category': 'Services/Connector',
    'support': 'odoo.tangerine@gmail.com',
    'author': 'Tangerine',
    'license': 'OPL-1',
    'depends': ['base', 'mail', 'viettelpost_connector'],
    'data': [
        'security/ir.model.access.csv',
        'data/api_connect_config_data.xml',
        'data/api_endpoints_config_data.xml',
        'data/ir_cron_data.xml',
        'views/api_connect_config_views.xml',
        'views/api_connect_history_views.xml',
        'views/api_endpoint_config_views.xml',
        'views/ir_cron_views.xml',
        'views/menus.xml'
    ],
    'external_dependencies': {
        'python': ['selenium']
    },
    'currency': 'USD',
    'price': 21,
    'images': ['static/description/thumbnail.png'],
    'application': True
}