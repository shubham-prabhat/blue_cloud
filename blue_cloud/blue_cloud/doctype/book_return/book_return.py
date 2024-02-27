# Copyright (c) 2024, Blue Cloud and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class BookReturn(Document):
	pass














import frappe

# def on_update(doc, method):
#     # Check if the document has been in Draft
#     if doc.docstatus == 0:
#         # Fetch the current status of the book
#         current_status = frappe.get_value("Book", doc.book_name, "status")
        
#         # Check if the current status is "Available"
#         if current_status == "Not Available":
#             frappe.msgprint(f"Submit this document '{doc.name}' to return the book.")
#         else:
#             frappe.throw("The book does not belong to the selected user. Therefore, the user cannot return this book.")


def on_update(doc, method):
    # Check if the document has been in Draft
    if doc.docstatus == 0:
        # Fetch the current status of the book
        current_status = frappe.get_value("Book", doc.book_name, "status")
        
        # Check if the current status is "Available"
        if current_status == "Not Available":
            frappe.msgprint(f"Submit this document '{doc.name}' to return the book.")
        else:
            frappe.throw("The book does not belong to the selected user. Therefore, the user cannot return this book.")

    if doc.docstatus == 1:
        # Fetch the current status of the book
         current_status = frappe.get_value("Book", doc.book_name, "status")
        
        # Check if the current status is "Available"
         if current_status == "Not Available":
            # Update the status of the book to "Not Available"
            frappe.db.set_value("Book", doc.book_name, "status", "Available")
            # frappe.db.set_value("Book", doc.book_name, "last_issue_document", doc.name)
            frappe.db.set_value("Book", doc.book_name, "last_return_document", doc.name)
            frappe.msgprint("Book status updated to 'Available'.")
            frappe.db.set_value("Book", doc.book_name, "current_user", None)
            frappe.db.set_value("Book", doc.book_name, "expected_available_on", None)
            frappe.db.set_value("Book Issue", doc.select_issue_document, "book_returned_on", doc.return_date)
         else:
            frappe.throw("The book does not belong to the selected user. Therefore, the user cannot return this book.")



# def on_cancel(doc, method):
#     # Check if the document has been submitted
#     if doc.docstatus == 2:
#         # Update the status of the book to "Not Available"
#         frappe.db.set_value("Book", doc.book_name, "status", "Available")
#         frappe.db.set_value("Book", doc.book_name, "last_issue_document", None)
#         frappe.db.set_value("Book", doc.book_name, "current_user", None)
#         frappe.db.set_value("Book", doc.book_name, "expected_available_on", None)
            





import frappe

# Define a function to be called on submission of Book Return
def create_penalty_on_submit(doc, method):
    # Check if the penalty_days field value is more than 0
    if doc.penalty_days > 0:
        # Create a new Penalty document
        penalty_doc = frappe.new_doc("Penalty")
        # Set relevant fields in the Penalty document
        penalty_doc.issued_date = doc.issued_date
        penalty_doc.book_name = doc.book_name
        penalty_doc.student_id = doc.student_id
        penalty_doc.book_return_document = doc.name
        penalty_doc.return_date = doc.return_date
        penalty_doc.expected_return_date = doc.expected_return_date
        penalty_doc.student_name = doc.student_name
        penalty_doc.penalty_days = doc.penalty_days
        penalty_doc.penalty_amount = doc.penalty_amount
        penalty_doc.docstatus = 1
        # Save the Penalty document
        penalty_doc.save()







# # # Validate selected book  and throw error on real time
# @frappe.whitelist()
# def validate_book_status(doc, method):
#     if doc.book_name:
#         book_status = frappe.get_value("Book", doc.book_name, "status")
#         if book_status and book_status != "Available" and hasattr(doc, 'status') and doc.status != "Not Available":
#             frappe.throw(f"Please return only books that are marked as 'Available'. Current status: {getattr(doc, 'status', 'Unknown')}")

        



# # # # # Below script is validating the book_name field on real time using frappe.call client Script

@frappe.whitelist()
def get_book_status(book_name):
    book_status = frappe.get_value("Book", book_name, "status")
    return book_status
