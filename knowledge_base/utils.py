# Copyright (c) 2013, Frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def get_level_class(level):
	return {
		"Beginner": "success",
		"Intermediate": "info",
		"Expert": "warning"
	}[level]

def get_category_sidebar():
	def _get():
		return frappe.db.sql("""select concat(category_name, " (", help_articles, ")") as title, concat("kb/", page_name) as name
			from `tabHelp Category`
			where ifnull(published,0)=1 and help_articles > 0
			order by help_articles desc""", as_dict=True)

	return frappe.cache().get_value("knowledge_base:category_sidebar", _get)

def clear_cache():
	frappe.cache().delete_value("knowledge_base:category_sidebar")
	frappe.cache().delete_value("knowledge_base:faq")

	from frappe.website.render import clear_cache
	clear_cache()
