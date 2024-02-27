# Copyright (c) 2024, Blue Cloud and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class BookIssue(Document):
	pass







import frappe

# def on_submit(doc, method):
#     # Check if the document has been submitted
#     if doc.docstatus == 1:
#         # Update the status of the book to "Not Available"
#         frappe.db.set_value("Book", doc.book_name, "status", "Not Available")



import frappe

# def on_update(doc, method):
#     # # Check if the document has been submitted
#     if doc.docstatus == 0 or doc.docstatus == 1:
#         # # Fetch the current status of the book
#         current_status = frappe.get_value("Book", doc.book_name, "status")
        
#         # # Check if the current status is "Available"
#         if current_status == "Available":
#             # Update the status of the book to "Not Available"
#             frappe.db.set_value("Book", doc.book_name, "status", "Not Available")
#             frappe.msgprint("Book status updated to 'Not Available'.")
#         else:
#             frappe.throw("Book status is not Available for now. You cannot issue this book")
		
		

import frappe

def on_update(doc, method):
    # Check if the document has been submitted
    if doc.docstatus == 0:
        # Fetch the current status of the book
        current_status = frappe.get_value("Book", doc.book_name, "status")
        
        # Check if the current status is "Available"
        if current_status == "Available":
            # Update the status of the book to "Not Available"
            # frappe.db.set_value("Book", doc.book_name, "status", "Not Available")
            # frappe.db.set_value("Book", doc.book_name, "last_issue_document", doc.name)
            frappe.msgprint(f"Submit this document '{doc.name}' to issue the book.")
        else:
            frappe.throw("Book status is not Available for now. You cannot issue this book")


    if doc.docstatus == 1:
        # Fetch the current status of the book
        current_status = frappe.get_value("Book", doc.book_name, "status")
        
        # Check if the current status is "Available"
        if current_status == "Available":
            # Update the status of the book to "Not Available"
            frappe.db.set_value("Book", doc.book_name, "status", "Not Available")
            frappe.db.set_value("Book", doc.book_name, "last_issue_document", doc.name)
            frappe.msgprint("Book status updated to 'Not Available'.")
            frappe.db.set_value("Book", doc.book_name, "current_user", doc.student_id)
            # frappe.db.set_value("Book", doc.book_name, "expected_available_on", doc.return_date)
            frappe.db.set_value("Book", doc.book_name, "expected_available_on", doc.expected_return_date)
        else:
            frappe.throw("Book status is not Available for now. You cannot issue this book")




def on_cancel(doc, method):
    # Check if the document has been submitted
    if doc.docstatus == 2:
        # Update the status of the book to "Not Available"
        frappe.db.set_value("Book", doc.book_name, "status", "Available")
        frappe.db.set_value("Book", doc.book_name, "last_issue_document", None)
        frappe.db.set_value("Book", doc.book_name, "current_user", None)
        frappe.db.set_value("Book", doc.book_name, "expected_available_on", None)