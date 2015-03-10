# Copyright (c) 2013, Frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.website.website_generator import WebsiteGenerator
from knowledge_base.utils import get_level_class, get_category_sidebar, clear_cache

class HelpCategory(WebsiteGenerator):
	website = frappe._dict(
		condition_field = "published",
		template = "templates/generators/help_category.html",
		page_title_field = "category_name"
	)

	def before_insert(self):
		self.published=1

	def autoname(self):
		self.name = self.category_name

	def get_context(self, context):
		context.articles = frappe.get_all("Help Article", fields = ["title", "parent_website_route",
			"page_name", "creation", "level", "likes", "author"], filters={"published":1, "category":self.name})
		context.get_level_class = get_level_class
		context.parents = [{"title":"Knowledge Base", "name":"/kb"}]
		context.children = get_category_sidebar()

	def on_update(self):
		clear_cache()
		super(HelpCategory, self).on_update()
