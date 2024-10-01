app_name = "gift"
app_title = "CRM System for Gift Management"
app_publisher = "SERVIO Technologies"
app_description = "Customized CRM System for Gift Management"
app_email = "carl@servio.ph"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "gift",
# 		"logo": "/assets/gift/logo.png",
# 		"title": "CRM System for Gift Management",
# 		"route": "/gift",
# 		"has_permission": "gift.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/gift/css/gift.css"
# app_include_js = "/assets/gift/js/gift.js"


# include js, css files in header of web template
# web_include_css = "/assets/gift/css/gift.css"
# web_include_js = "/assets/gift/js/gift.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "gift/public/scss/website"

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
# app_include_icons = "gift/public/icons.svg"

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
# 	"methods": "gift.utils.jinja_methods",
# 	"filters": "gift.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "gift.install.before_install"
# after_install = "gift.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "gift.uninstall.before_uninstall"
# after_uninstall = "gift.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "gift.utils.before_app_install"
# after_app_install = "gift.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "gift.utils.before_app_uninstall"
# after_app_uninstall = "gift.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "gift.notifications.get_notification_config"

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

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

## gift/hooks.py

# gift/hooks.py

doctype_js = {
    "Items": "public/js/items.js"
}

doc_events = {
    "Items": {
        "validate": "gift.api.validate_item_quantity",  # Optional: For server-side validations
        "after_insert": "gift.api.update_item_summary",
        "on_update": "gift.api.update_item_summary",
        "on_cancel": "gift.api.cancel_stock_balance",
    }
}



# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"gift.tasks.all"
# 	],
# 	"daily": [
# 		"gift.tasks.daily"
# 	],
# 	"hourly": [
# 		"gift.tasks.hourly"
# 	],
# 	"weekly": [
# 		"gift.tasks.weekly"
# 	],
# 	"monthly": [
# 		"gift.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "gift.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "gift.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "gift.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["gift.utils.before_request"]
# after_request = ["gift.utils.after_request"]

# Job Events
# ----------
# before_job = ["gift.utils.before_job"]
# after_job = ["gift.utils.after_job"]

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
# 	"gift.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

