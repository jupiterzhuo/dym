from openerp import models, fields, api 

class dym_report_registerpraso_ai(models.Model):
    _inherit = 'dealer.spk'
    
    def _report_xls_registerpraso_fields(self, cr, uid, context=None):
        return [
            'no',\
            'branch_status',\
            'area',\
            'branch_code',\
            'branch_name',\
            'invoice_number',\
            'invoice_date',\
            'last_update_time',\
            'invoice_status',\
            'no_registrasi',\
            'spk_name',\
            'name',\
            'date_order',\
            'state',\
            'state_ksu',\
            'state_picking',\
            'oos_number',\
            'is_cod',\
            'sls_pay',\
            'vcust_id',\
            'finco_code',\
            'finco_branch',\
            'no_po',\
            'tgl_po',\
            'tenor',\
            'jp_po',\
            'cust_code',\
            'cust_name',\
            'cabang_partner',\
            'alamat_cust_name',\
            'kota_cust_name',\
            'no_hp_cust_beli',\
            'cust_stnk_code',\
            'cust_stnk_name',\
            'alamat_cust_stnk_name',\
            'kota_cust_stnk_name',\
            'jns_kota_cust_stnk_name',\
            'kec_cust_stnk_name',\
            'kel_cust_stnk_name',\
            'no_hp_cust_stnk',\
            'cust_corp',\
            'nik_sales_name',\
            'sales_name',\
            'job_name',\
            'nik_sales_koor_name',\
            'sales_koor_name',\
            'spv_nik',\
            'spv_name',\
            'partner_komisi_id',\
            'partner_komisi_name',\
            'hutang_komisi_id',\
            'amount_hutang_komisi',\
            'pph_komisi',\
            'lot_name',\
            'lot_chassis',\
            'product_name',\
            'product_desc',\
            'pav_code',\
            'categ_name',\
            'categ2_name',\
            'prod_series',\
            'tahun_rakit',\
            'ps_ahm',\
            'ps_md',\
            'ps_finco',\
            'ps_dealer',\
            'ps_other',\
            'ps_total',\
            'price_unit',\
            'sales',\
            'disc_total',\
            'discount_po',\
            'discount_extern_ps',\
            'discount_intern_ps',\
            'disc_quo_incl_tax_no',\
            'price_bbn',\
            'piutang_total',\
            'dsb_name',\
            'dsbl_diskon_ahm',\
            'dsbl_diskon_md',\
            'dsbl_diskon_dealer',\
            'dsbl_diskon_finco',\
            'dsbl_diskon_others',\
            'dsbl_total_diskon',\
            'beban_cabang',\
            'price_subtotal',\
            'PPN',\
            'total',\
            'force_cogs',\
            'gp_dpp_minus_hpp',\
            'gp_unit',\
            'price_bbn_beli',\
            'gp_bbn',\
            'gp_total',\
            'dpp_insentif_finco',\
            'tambahan_bbn',\
            'product_qty',\
            'qty_pic',\
            'qty_retur',\
            'net_sales',\
            'proposal_id',\
            'proposal_address',\
            'npwp_cust',\
            'pkp',\
            'tax_type',\
            'faktur_pajak',\
            'or_name',\
            'ar_days',\
            'tgl_lunas',\
            'md_code',\
        ]
    