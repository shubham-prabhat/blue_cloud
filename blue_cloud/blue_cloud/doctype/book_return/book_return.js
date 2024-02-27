// Copyright (c) 2024, Blue Cloud and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Book Return", {
// 	refresh(frm) {

// 	},
// });






// frappe.ui.form.on('Book Return', {
//     onload: function(frm) {
//         if (frm.doc.docstatus === 0) {
//             // // // Set the value of book_receiver field to frappe.session.user
//             frm.set_value('book_receiver', frappe.session.user);

//             // // // Filter available books based on student_id
//             frm.set_query('select_issue_document', function() {
//                 return {
//                     filters: [
//                         ['student_id', '=', frm.doc.student_id],
//                         ['book_name', '=', frm.doc.book_name]
//                     ]
//                 };
//             });

//             // // // Filter available books based on Not Available
//             frm.set_query('book_name', function() {
//                 return {
//                     filters: [
//                         ['status', '=', "Not Available"],
//                         ['current_user', '=', frm.doc.student_id]
//                     ]
//                 };
//             });
//         }
//     }
// });









frappe.ui.form.on('Book Return', {
    onload: function(frm) {
        if (frm.doc.docstatus === 0) {
            // Set the value of book_receiver field to frappe.session.user
            frm.set_value('book_receiver', frappe.session.user);

            // Filter available books based on student_id and book_name
            frm.set_query('select_issue_document', function() {
                return {
                    filters: [
                        ['student_id', '=', frm.doc.student_id],
                        ['book_name', '=', frm.doc.book_name]
                    ]
                };
            });

            // Filter available books based on Not Available and current user
            frm.set_query('book_name', function() {
                return {
                    filters: [
                        ['status', '=', "Not Available"],
                        ['current_user', '=', frm.doc.student_id]
                    ]
                };
            });
        }
    },

    return_date: function(frm) {
        // Calculate penalty days when return_date changes and docstatus is 0
        if (frm.doc.docstatus === 0) {
            calculatePenalty(frm);
        }
    },

    expected_return_date: function(frm) {
        // Calculate penalty days when expected_return_date changes and docstatus is 0
        if (frm.doc.docstatus === 0) {
            calculatePenalty(frm);
        }
    }
});

function calculatePenalty(frm) {
    var return_date = frm.doc.return_date;
    var expected_return_date = frm.doc.expected_return_date;

    // Ensure both dates are not null
    if (return_date && expected_return_date) {
        // Parse date strings into Date objects
        var return_date_obj = frappe.datetime.str_to_obj(return_date);
        var expected_return_date_obj = frappe.datetime.str_to_obj(expected_return_date);

        // Calculate the difference in days
        var penalty_days = frappe.datetime.get_diff(return_date_obj, expected_return_date_obj);

        // Update the penalty days field
        frm.set_value('penalty_days', Math.max(penalty_days, 0));

        // Calculate penalty amount
        if (penalty_days > 0) {
            var penalty_amount = penalty_days * 15; // Assuming penalty amount is $15 per day
            frm.set_value('penalty_amount', penalty_amount);
        } else {
            frm.set_value('penalty_amount', 0);
        }
    }
}







// // // Validate Return Date

frappe.ui.form.on('Book Return', {
    return_date: function(frm) {
        // Get the current date
        var currentDate = frappe.datetime.now_date();

        // Get the value of the return_date field
        var returnDate = frm.doc.return_date;

        // Check if the return_date is before or after today's date
        if (returnDate < currentDate) {
            // Clear the return_date field
            frm.set_value('return_date', '');

            // Display a validation error message
            frappe.msgprint({
                title: __('Validation Error'),
                indicator: 'red',
                message: __('Return Date cannot be before today\'s date')
            });
        } else if (returnDate > currentDate) {
            // Clear the return_date field
            frm.set_value('return_date', '');

            // Display a validation error message
            frappe.msgprint({
                title: __('Validation Error'),
                indicator: 'red',
                message: __('Return Date cannot be later than today\'s date')
            });
        }
    }
});









frappe.ui.form.on('Book Return', {
    book_name: function(frm) {
        var book_name = frm.doc.book_name;
        if (book_name) {
            frappe.call({
                method: 'blue_cloud.blue_cloud.doctype.book_return.book_return.get_book_status',
                args: {
                    book_name: book_name
                },
                callback: function(r) {
                    var status = r.message;
                    if (status !== "Not Available") {
                        frappe.msgprint('Selected book is still ' + status + '. Please return only books that are marked as "Not Available".');
                        frm.set_value('book_name', '');
                    }
                }
            });
        }
    }
});



