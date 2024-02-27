// Copyright (c) 2024, Blue Cloud and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Book", {
// 	refresh(frm) {

// 	},
// });


frappe.ui.form.on('Book', {
    validate: function(frm) {
        if (frm.doc.status === 'Select' && frm.doc.docstatus === 0 ) {
            frappe.msgprint(__('Please select a valid Book Status for the book.'));
            frappe.validated = false;
        }
    }
});
