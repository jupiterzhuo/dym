import time
from datetime import datetime
from openerp.osv import fields, osv
from openerp.tools.translate import _
import openerp.addons.decimal_precision as dp
from openerp.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT, DATETIME_FORMATS_MAP

class udstk_partner(osv.osv):
    _inherit = "res.partner"
    
    def is_udstk_ok(self,cr,uid,ids,val,context=None):
        return all([
            val.street_tab,
            val.rt_tab,
            val.rw_tab,
            val.state_tab_id,
            val.city_tab_id,
            val.kecamatan_tab_id,
            val.zip_tab_id,
            val.kelurahan_tab,
        ])
        
    def write(self,cr,uid,ids,vals,context=None):
        if not ids:
            return {}
        for val in self.browse(cr,uid,ids):
            lot = self.pool.get('stock.production.lot')
            lot_search = lot.search(cr,uid,[
                ('customer_stnk','=',val.id),
                ('lot_status_cddb','!=','ok'),
                ('state_stnk','=',False),'|',
                ('state','=','paid'),'|',
                ('state','=','sold'),'|',
                ('state','=','paid_offtr'),
                ('state','=','sold_offtr')
            ])
            if lot_search :
                lot_browse = lot.browse(cr,uid,lot_search)
                is_udstk_ok = self.is_udstk_ok(cr, uid, ids, val, context)
                if is_udstk_ok :
                    for x in lot_browse :
                        if x.lot_status_cddb == 'cddb' :
                            lot_browse.write({'lot_status_cddb':'ok'})
                        if x.lot_status_cddb == 'ok' :
                            lot_browse.write({'lot_status_cddb':'ok'})
                        if x.lot_status_cddb == 'not' :
                            lot_browse.write({'lot_status_cddb':'udstk'})   
        return super(udstk_partner, self).write(cr, uid, ids, vals, context=context) 
        return {'type':'ir.actions.act_close_wizard_and_reload_view'}