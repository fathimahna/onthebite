from odoo import api, fields, models


class Supplier(models.Model):
    _name = 'otb.supplier'
    _description = 'New Description'

    name = fields.Char(string='Name Supplier')
    produk_ids = fields.One2many(comodel_name='otb.produk', inverse_name='supplierproduk_id', string='Nama Produk')
    aset_ids = fields.One2many(comodel_name='otb.aset', inverse_name='supplieraset_id', string='Nama Aset')
    
    platform = fields.Char(string='Platform')
    alamat = fields.Char(string='Alamat')
    tlp = fields.Char(string='No Tlp')
    
    
    
