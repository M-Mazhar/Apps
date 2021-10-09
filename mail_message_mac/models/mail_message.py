# -*- coding: utf-8 -*-
import pdb

from odoo import models, fields, api
from getmac import get_mac_address as gma


class MailMessage(models.Model):
	_inherit = 'mail.message'

	mac_address = fields.Char(copy=False)

	@api.model
	def create(self, vals):
		vals['mac_address'] = gma()
		res = super(MailMessage, self).create(vals)
		return res

	def _get_message_format_fields(self):
		fields_to_show = super(MailMessage, self)._get_message_format_fields()
		if self.env.user.has_group('base.user_admin'):
			fields_to_show.append('mac_address')
		return fields_to_show
