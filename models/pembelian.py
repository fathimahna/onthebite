from odoo import api, fields, models


class Pembelian(models.Model):
    _name = 'otb.pembelian'
    _description = 'New Description'

    pesananproduk_ids = fields.One2many(comodel_name='otb.pesananproduk', 
                                        inverse_name='pesanan_id', 
                                        string='Pesanan Produk')
    
    id_order = fields.Char(string='Kode Order', size=10, required=True)
    
    name = fields.Char(string='Pemesan')
    
    tgl_pesanan = fields.Date(
        string='Tanggal Pesanan',
        default=fields.Date.today()
    )
    
    total = fields.Float(string='Total')


class PesananProduk(models.Model):
    _name = 'otb.pesananproduk'
    _description = 'New Description'

    pesanan_id = fields.Many2one(comodel_name='otb.pembelian', string='Pesanan')
    produk_id = fields.Many2one(comodel_name='otb.produk', string='Produk', required=True)

    name = fields.Char(string='Name')
    qty = fields.Integer(string='Quantity')

    harga_satuan = fields.Float(
        compute='_compute_harga_satuan', string='Harga Satuan')

    harga = fields.Float(
        compute='_compute_harga', string='Harga')
    
    @api.depends('produk_id')
    def _compute_harga_satuan(self):
        for record in self:
            record.harga_satuan = record.produk_id.harga_jual
    
    
    @api.depends('qty','harga_satuan')
    def _compute_harga(self):
        for record in self:
            record.harga = record.qty * record.harga_satuan
    

    
    
    

    

    
