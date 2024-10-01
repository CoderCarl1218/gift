// your_app/your_module/public/js/items.js

frappe.ui.form.on('Items', {
    refresh: function(frm) {
        // Remove existing custom buttons to prevent duplicates
        frm.page.remove_inner_button(__("Add Quantity"));
        frm.page.remove_inner_button(__("Create Transaction"));

        // Add the "Add Quantity" button
        let add_qty_btn = frm.add_custom_button(__('Add Quantity'), function() {
            // Open a dialog to input the quantity to add
            let dialog = new frappe.ui.Dialog({
                title: __('Add Quantity'),
                fields: [
                    {
                        label: __('Quantity to Add'),
                        fieldname: 'quantity',
                        fieldtype: 'Float',
                        reqd: 1,
                        default: 0,
                        description: __('Enter the quantity you wish to add.')
                    }
                ],
                primary_action_label: __('Add'),
                primary_action: function(values) {
                    let qty_to_add = values.quantity;

                    // Validate the input quantity
                    if (qty_to_add <= 0) {
                        frappe.msgprint(__('Please enter a quantity greater than zero.'));
                        return;
                    }

                    // Optionally, confirm the action with the user
                    frappe.confirm(
                        __('Are you sure you want to add {0} to the current quantity?', [qty_to_add]),
                        function() {
                            // Set 'item_quantity' to the entered quantity
                            frm.set_value('item_quantity', qty_to_add);

                            // Save the form to trigger server-side hooks
                            frm.save().then(() => {
                                frappe.msgprint(__('Quantity added successfully.'));

                                // Clear the 'item_quantity' field after saving
                                frm.set_value('item_quantity', 0);
                            }).catch((err) => {
                                frappe.msgprint(__('Failed to add quantity: ') + (err.message || 'Unknown error'));
                            });

                            // Close the dialog
                            dialog.hide();
                        },
                        function() {
                            // User canceled the action
                            dialog.hide();
                        }
                    );
                }
            });

            dialog.show();
        });

        // Assign the desired CSS classes to the "Add Quantity" button
        add_qty_btn.addClass('btn btn-primary btn-sm primary-action');

        // Add the "Create Transaction" button
        let create_txn_btn = frm.add_custom_button(__('Create Transaction'), function() {
            // Navigate to the Transactions DocType
            frappe.set_route('List', 'Transaction');
        });

        // Assign the desired CSS classes to the "Create Transaction" button
        create_txn_btn.addClass('btn btn-primary btn-sm primary-action');
    }
    
});
