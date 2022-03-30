from odoo import api, fields, models


class Produk(models.Model):
    _name = 'otb.produk'
    _description = 'New Description'

    supplierproduk_id = fields.Many2one(comodel_name='otb.supplier', 
                                        string='Supplier',
                                        required=True)
    pesananproduk_ids = fields.One2many(
        string='Produk',
        comodel_name='otb.pesananproduk',
        inverse_name='produk_id'
    )

    name = fields.Char(string='Nama Produk', required=True)
    stok = fields.Integer(string='Quantity')
    harga_beli = fields.Float(string='Harga Beli')
    harga_jual = fields.Float(string='Harga Jual')
    
    
    
    
    
