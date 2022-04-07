from odoo import api, fields, models


class Produk(models.Model):
    _name = 'otb.produk'
    _description = 'New Description'

    supplierproduk_id = fields.Many2one(comodel_name='res.partner', 
                                        string='Supplier',
                                        domain=[('is_customernya','=',True)],
                                        store=True)

    pilihanproduk_ids = fields.One2many(comodel_name='otb.pilihan', 
                                        inverse_name='produk_id', string='Produk')
                                    
    paket_ids = fields.One2many(comodel_name='otb.paketproduk', inverse_name='produk_id', string='Paket Produk')
    

    name = fields.Char(string='Nama Produk', required=True)
    stok = fields.Integer(string='Quantity')
    
    harga_satuan = fields.Float(string='Harga Satuan')



    
    
