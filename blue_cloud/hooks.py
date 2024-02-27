app_name = "blue_cloud"
app_title = "Blue Cloud"
app_publisher = "Blue Cloud"
app_description = "Official App"
app_email = "shubham.p@bluecloudsoftech.com"
app_license = "mit"
# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/blue_cloud/css/blue_cloud.css"
# app_include_js = "/assets/blue_cloud/js/blue_cloud.js"

# include js, css files in header of web template
# web_include_css = "/assets/blue_cloud/css/blue_cloud.css"
# web_include_js = "/assets/blue_cloud/js/blue_cloud.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "blue_cloud/public/scss/website"

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
# app_include_icons = "blue_cloud/public/icons.svg"

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
# 	"methods": "blue_cloud.utils.jinja_methods",
# 	"filters": "blue_cloud.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "blue_cloud.install.before_install"
# after_install = "blue_cloud.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "blue_cloud.uninstall.before_uninstall"
# after_uninstall = "blue_cloud.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "blue_cloud.utils.before_app_install"
# after_app_install = "blue_cloud.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "blue_cloud.utils.before_app_uninstall"
# after_app_uninstall = "blue_cloud.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "blue_cloud.notifications.get_notification_config"

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
# override_doctype_class = {
# 	# "ToDo": "custom_app.overrides.CustomToDo",
# 	"Timesheet": "blue_cloud.blue_cloud.doctype.timesheet.timesheet.Timesheet",
# }
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
# 		"blue_cloud.tasks.all"
# 	],
# 	"daily": [
# 		"blue_cloud.tasks.daily"
# 	],
# 	"hourly": [
# 		"blue_cloud.tasks.hourly"
# 	],
# 	"weekly": [
# 		"blue_cloud.tasks.weekly"
# 	],
# 	"monthly": [
# 		"blue_cloud.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "blue_cloud.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "blue_cloud.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "blue_cloud.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["blue_cloud.utils.before_request"]
# after_request = ["blue_cloud.utils.after_request"]

# Job Events
# ----------
# before_job = ["blue_cloud.utils.before_job"]
# after_job = ["blue_cloud.utils.after_job"]

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
# 	"blue_cloud.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }







doc_events = {
    "Book Issue": {
        "on_update": [
            "blue_cloud.blue_cloud.doctype.book_issue.book_issue.on_update",
        ],
        "on_cancel": [
            "blue_cloud.blue_cloud.doctype.book_issue.book_issue.on_cancel",
        ]
    },
    "Book Return": {
        "on_update": [
            "blue_cloud.blue_cloud.doctype.book_return.book_return.on_update",
            # "blue_cloud.blue_cloud.doctype.book_return.book_return.validate_book_status",
        ],
        "on_submit": [
            "blue_cloud.blue_cloud.doctype.book_return.book_return.create_penalty_on_submit",
        ],
        "on_cancel": [
            # "blue_cloud.blue_cloud.doctype.book_return.book_return.on_cancel",
        ]
    }
}
