app_name = "upgrade_shipping_rule"
app_title = "Upgrade Shipping Rule"
app_publisher = "Zaviago"
app_description = "Add new options in shipping rule"
app_email = "muzammal.rasool1079@gmail.com"
app_license = "mit"
from upgrade_shipping_rule import CustomShippingRule
# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/upgrade_shipping_rule/css/upgrade_shipping_rule.css"
# app_include_js = "/assets/upgrade_shipping_rule/js/upgrade_shipping_rule.js"

# include js, css files in header of web template
# web_include_css = "/assets/upgrade_shipping_rule/css/upgrade_shipping_rule.css"
# web_include_js = "/assets/upgrade_shipping_rule/js/upgrade_shipping_rule.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "upgrade_shipping_rule/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "upgrade_shipping_rule/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "upgrade_shipping_rule.utils.jinja_methods",
# 	"filters": "upgrade_shipping_rule.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "upgrade_shipping_rule.install.before_install"
# after_install = "upgrade_shipping_rule.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "upgrade_shipping_rule.uninstall.before_uninstall"
# after_uninstall = "upgrade_shipping_rule.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "upgrade_shipping_rule.utils.before_app_install"
# after_app_install = "upgrade_shipping_rule.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "upgrade_shipping_rule.utils.before_app_uninstall"
# after_app_uninstall = "upgrade_shipping_rule.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "upgrade_shipping_rule.notifications.get_notification_config"

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

# DocType Class
# ---------------
# Override standard doctype classes

override_doctype_class = {
	"Shipping Rule": "upgrade_shipping_rule.CustomShippingRule.CustomShippingRule"
}

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"upgrade_shipping_rule.tasks.all"
# 	],
# 	"daily": [
# 		"upgrade_shipping_rule.tasks.daily"
# 	],
# 	"hourly": [
# 		"upgrade_shipping_rule.tasks.hourly"
# 	],
# 	"weekly": [
# 		"upgrade_shipping_rule.tasks.weekly"
# 	],
# 	"monthly": [
# 		"upgrade_shipping_rule.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "upgrade_shipping_rule.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"erpnext.erpnext.controllers.accounts_controller.apply_shipping_rule": "upgrade_shipping_rule.shipping_rule_settings.overRiddenapplyShippingRule"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "upgrade_shipping_rule.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["upgrade_shipping_rule.utils.before_request"]
# after_request = ["upgrade_shipping_rule.utils.after_request"]

# Job Events
# ----------
# before_job = ["upgrade_shipping_rule.utils.before_job"]
# after_job = ["upgrade_shipping_rule.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"upgrade_shipping_rule.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

