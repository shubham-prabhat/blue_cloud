// Copyright (c) 2024, Blue Cloud and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Book Issue", {
// 	refresh(frm) {

// 	},
// });







frappe.ui.form.on('Book Issue', {
    onload: function(frm) {
        // Filter available books
        frm.set_query('book_name', function() {
            return {
                filters: [
                    ['status', '=', 'Available']
                ]
            };
        });
    }
});



// // // validating 'expected_return_date' this script

frappe.ui.form.on('Book Issue', {
    expected_return_date: function(frm) {
        // Ensure expected_return_date is not before issue_on date
        if (frm.doc.expected_return_date < frm.doc.issue_on) {
            // frappe.msgprint(__("Expected return date cannot be before the issue date."));
            frm.set_value('expected_return_date', '');
        }
    }
});

// // // validating 'issue_date' this script

frappe.ui.form.on('Book Issue', {
    issue_on: function(frm) {
        // Get today's date
        var today = frappe.datetime.get_today();

        // Get the value of the issue_on field
        var issueDate = frm.doc.issue_on;

        // Ensure issue_on date is not before or after today
        if (issueDate < today) {
            // frappe.msgprint("Issue date cannot be before today.");
            frm.set_value('issue_on', '');
        } else if (issueDate > today) {
            // frappe.msgprint("Issue date cannot be after today.");    
            frm.set_value('issue_on', '');
        }
    }
});






