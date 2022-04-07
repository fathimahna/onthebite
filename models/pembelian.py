from email.policy import default
from odoo import api, fields, models


class Pembelian(models.Model):
    _name = 'otb.pembelian'
    _description = 'New Description'

    pesananproduk_ids = fields.One2many(comodel_name='otb.pesananproduk', 
                                        inverse_name='pesanan_id', 
                                        string='Pesanan Produk')
    
    id_pembelian = fields.Char(string='Kode Order')
    
    name = fields.Char(string='Pemesan')
    
    tgl_pesanan = fields.Date(
        string='Tanggal Pesanan',
        default=fields.Date.today()
    )
    
    total = fields.Float(
        compute='_compute_total', string='Total', store=True)
    
    @api.depends('pesananproduk_ids')
    def _compute_total(self):
        for record in self:
            record.total = sum(self.env['otb.pesananproduk'].search([('pesanan_id', '=', record.id)]).mapped('harga'))

    sudah_bayar = fields.Boolean(string='Paid', default=False)

    @api.model
    def create(self, values):
        result = super(Pembelian, self).create(values)
        if result.tgl_pesanan:
            self.env['otb.pembelian'].search([('id','=',result.id_pembelian)]).write({'sudah_bayar':True})
            self.env['otb.keuangan'].create({'kredit':result.total, 'name':result.name})
        return result      
    

class PesananProduk(models.Model):
    _name = 'otb.pesananproduk'
    _description = 'New Description'

    pesanan_id = fields.Many2one(comodel_name='otb.pembelian', string='Pesanan')
    paketproduk_id = fields.Many2one(comodel_name='otb.paketproduk', string='Paket')

    qty = fields.Integer(string='Quantity')

    harga_satuan = fields.Float(
        compute='_compute_harga_satuan', string='Harga Satuan')

    harga = fields.Float(
        compute='_compute_harga', string='Harga')
    
    @api.depends('paketproduk_id')
    def _compute_harga_satuan(self):
        for record in self:
            record.harga_satuan = record.paketproduk_id.harga
    
    
    @api.depends('qty','harga_satuan')
    def _compute_harga(self):
        for record in self:
            record.harga = record.qty * record.harga_satuan
    