app_name = "knowledge_base"
app_title = "Knowledge Base"
app_publisher = "Frappe"
app_description = "Knowledge Base / Help Portal"
app_icon = "icon-question-sign"
app_color = "#4cd964"
app_email = "info@frappe.io"
app_url = "https://frappe.io/apps/knowledge_base"
app_version = "0.0.1"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/knowledge_base/css/knowledge_base.css"
# app_include_js = "/assets/knowledge_base/js/knowledge_base.js"

# include js, css files in header of web template
web_include_css = "/assets/knowledge_base/css/knowledge_base.css"
# web_include_js = "/assets/knowledge_base/js/knowledge_base.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
website_generators = ["Help Article", "Help Category"]

website_clear_cache = "knowledge_base.utils.clear_website_cache"

# Installation
# ------------

# before_install = "knowledge_base.install.before_install"
# after_install = "knowledge_base.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "knowledge_base.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"knowledge_base.tasks.all"
# 	],
# 	"daily": [
# 		"knowledge_base.tasks.daily"
# 	],
# 	"hourly": [
# 		"knowledge_base.tasks.hourly"
# 	],
# 	"weekly": [
# 		"knowledge_base.tasks.weekly"
# 	]
# 	"monthly": [
# 		"knowledge_base.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "knowledge_base.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "knowledge_base.event.get_events"
# }

