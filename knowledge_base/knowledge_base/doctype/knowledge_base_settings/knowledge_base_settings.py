# Copyright (c) 2013, Frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from knowledge_base.utils import clear_cache

class KnowledgeBaseSettings(Document):
	def on_update(self):
		clear_cache()
