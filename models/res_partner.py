from email.policy import default
from odoo import api, fields, models


class Supplier(models.Model):
    _inherit = ['res.partner']

    is_pegawainya = fields.Boolean(string='Pegawai', default=False)
    is_customernya = fields.Boolean(string='Customer', default=False)
    
    
    
    
