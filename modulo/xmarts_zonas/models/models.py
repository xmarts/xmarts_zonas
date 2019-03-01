## -*- coding: utf-8 -*-

from openerp import models, fields, api, _, tools
from openerp.exceptions import UserError, RedirectWarning, ValidationError
import xlrd
import shutil



class respartnerzonas(models.Model):
	_name = 'zonas.partner'

	name = fields.Char(string='Zona de Residencia', help='Coloca la zona de residencia para especificar la zona de localizacion', requiered=True)



class InheritZona(models.Model):

	_inherit = 'res.partner'

	zone = fields.Many2one('zonas.partner',string='Zona de Entrega', help='Coloca la zona de residencia para especificar la zona de localizacion')

	_sql_constraints = [('rfc_uniq','unique(vat)','EL RFC debe de ser unico, ya existe uno registrado.')]

		




# class ReportClassName(models.AbstractModel):
# 	_name = 'report.account.invoice.report_invoice_document_interkey'

# 	@api.model
# 	def render_html(self, docids, data=None):
# 		print "data....", data
# 		docargs = {
# 			'doc_ids': self.ids,
# 			'doc_model': self.model,
# 			'data': data,
# 		}
# 		return self.env['report'].render('account.invoice.report_invoice_document_interkey', docargs)
