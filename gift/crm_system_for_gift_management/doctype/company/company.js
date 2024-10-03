// Copyright (c) 2024, SERVIO Technologies and contributors
// For license information, please see license.txt

frappe.ui.form.on("Company", {
    refresh: function(frm) {
        // Check if the company_code is empty, only generate a new one if it's empty
        if (!frm.doc.company_code) {
            // Generate a random number between 10000000 and 999999999
            let random_code = Math.floor(10000000 + Math.random() * 900000000);
            // Set the value of company_code with the generated random code
            frm.set_value('company_code', random_code.toString());
        }
    }
});
