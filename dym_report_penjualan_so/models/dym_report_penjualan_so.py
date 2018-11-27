from openerp import models, fields, api

class dym_report_penjualan_so_sm(models.Model):
    _inherit = 'sale.order'
    
    def _report_xls_penjualan_so_fields(self, cr, uid, context=None):
        return [
            'no',\
            'branch_status',\
            'branch_code',\
            'branch_name',\
            'name',\
            'state',\
            'date_order',\
            'invoice_name',\
            'invoice_status',\
            'invoice_date',\
            'oos_number',\
            'oos_tgl',\
            'dno_number',\
            'dno_tgl',\
            'cust_name',\
            'tipe_konsumen',\
            'tipe_transaksi',\
            'product_name',\
            'categ_name',\
            'category',\
            'product_qty',\
            'price_unit',\
            'discount_show',\
            'discount',\
            'discount_program',\
            'discount_cash',\
            'discount_lain',\
            'price_subtotal',\
            'dpp',\
            'ppn',\
            'force_cogs',\
            'retur',\
            'tgl_bayar',\
            'bayar',\
            'ar_bayar',\
            'ar',\
            'faktur_pajak',\
            'sales_name',\
            'program_subsidi',\
        ]
    