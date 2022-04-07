from email.policy import default
from odoo import api, fields, models


class Keuangan(models.Model):
    _name = 'otb.keuangan'
    _description = 'New Description'
    _order = 'id asc'

    name = fields.Char(string='Pemesan')
    
    tgl_transaksi = fields.Date(string='Tanggal Transaksi', 
                                default=fields.Date.today())

    debit = fields.Float(string='Debit')
    kredit = fields.Float(string='Kredit')
    saldo = fields.Float(
        compute='_compute_saldo', string='Saldo')
    
    @api.depends('debit', 'kredit')
    def _compute_saldo(self):
        for record in self:
            prev = self.search_read([('id', '<', record.id)], limit=1, order='tgl_transaksi desc')
            prev_saldo = prev[0]['saldo'] if prev else 0
            record.saldo = prev_saldo + record.kredit - record.debit
    

    
    
    
    
    
