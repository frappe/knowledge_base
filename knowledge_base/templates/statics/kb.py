import frappe
from knowledge_base.utils import get_level_class, get_category_sidebar

def get_context(context):
	context.faq = get_faq()
	context.children = get_category_sidebar()
	context.get_level_class = get_level_class

def get_faq():
	def _get():
		settings = frappe.get_doc("Knowledge Base Settings", "Knowledge Base Settings")
		faq = []
		for a in settings.home_page_help_articles:
			faq.append(frappe.get_doc("Help Article", a.help_article).as_dict())

		return faq

	return frappe.cache().get_value("knowledge_base:faq", _get)
