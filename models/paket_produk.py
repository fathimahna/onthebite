from odoo import api, fields, models


class PaketProduk(models.Model):
    _name = 'otb.paketproduk'
    _description = 'New Description'

    name = fields.Char(string='Nama Paket')

    pilihanproduk_ids = fields.One2many(comodel_name='otb.pilihan', 
                                        inverse_name='paketproduk_id', 
                                        string='Pilihan Produk')

    pesanan_id = fields.One2many(comodel_name='otb.pesananproduk', 
                                 inverse_name='paketproduk_id', 
                                 string='Pesanan')
    
    produk_id = fields.Many2one(comodel_name='otb.produk', string='Produk')
    qty = fields.Integer(string='Quantity')
    
    harga_satuan = fields.Float(compute='_compute_harga_satuan', string='harga_satuan')
    
    @api.depends('produk_id')
    def _compute_harga_satuan(self):
        for record in self:
            record.harga_satuan = record.produk_id.harga_satuan
    
    harga = fields.Float(
        compute='_compute_harga', string='Total')
    
    @api.depends('produk_id')
    def _compute_harga(self):
        for record in self:
            record.harga = record.produk_id.harga_satuan * record.qty

class PilihanProduk(models.Model):
    _name = 'otb.pilihan'
    _description = 'New Description'

    paketproduk_id = fields.Many2one(comodel_name='otb.paketproduk', string='Paket Produk')
    produk_id = fields.Many2one(comodel_name='otb.produk', string='Produk')
    
    qty = fields.Integer(string='Quantity')
    harga_satuan = fields.Float(
        compute='_compute_harga_satuan', string='Harga Satuan')
    
    @api.depends('produk_id')
    def _compute_harga_satuan(self):
        for record in self:
            record.harga_satuan = record.produk_id.harga_satuan
    
    jumlah = fields.Float(
        compute='_compute_jumlah', string='Jumlah')
    
    @api.depends('harga_satuan','qty')
    def _compute_jumlah(self):
        for record in self:
            record.jumlah = record.harga_satuan * record.qty
