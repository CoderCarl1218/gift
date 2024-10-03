// Copyright (c) 2024, SERVIO Technologies and contributors
// For license information, please see license.txt

frappe.ui.form.on("Customers", {
	refresh: function (frm) {
        if (!frm.doc.customer_code){
            let random_code =  Math.floor(10000000 + Math.random()*90000000)
            frm.set_value('customer_code',random_code.toString())

        }

	},
    birthday: function(frm) {
        // Check if the birthday field has a value
        if (frm.doc.birthday) {
            // Get today's date
            let today = new Date();
            // Parse the birthday entered by the user
            let birthDate = new Date(frm.doc.birthday);
            
            // Calculate the age based on the difference between today and the birthday
            let age = today.getFullYear() - birthDate.getFullYear();
            let monthDiff = today.getMonth() - birthDate.getMonth();
            
            // Adjust if the birthday hasn't occurred yet this year
            if (monthDiff < 0 || (monthDiff === 0 && today.getDate() < birthDate.getDate())) {
                age--;
            }
            
            // Set the value in the age field
            frm.set_value('age', age);
        }
    }
});
