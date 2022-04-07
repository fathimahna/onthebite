from odoo import api, fields, models


class Aset(models.Model):
    _name = 'otb.aset'
    _description = 'New Description'

    name = fields.Char(string='Nama Barang')
    stok = fields.Integer(string='Quantity')
    harga_satuan = fields.Float(string='Harga Satuan')
    type = fields.Selection(string='Jenis', selection=[('tidak habis pakai', 'Tidak Habis Pakai'), ('habis pakai', 'Habis Pakai'),])
    kondisi = fields.Selection(string='Kondisi', selection=[('baru', 'Baru'), ('bekas', 'Bekas'),])
    supplieraset_id = fields.Many2one(comodel_name='res.partner', 
                                      string='Supplier', 
                                      domain=[('is_customernya','=',True)],
                                      store=True)
    
    
    
    
    
    
    
    
