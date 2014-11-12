# Copyright (c) 2013, Web Notes and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.website.utils import delete_page_cache

class KnowledgeBaseSettings(Document):
	def on_update(self):
		delete_page_cache("kb")
