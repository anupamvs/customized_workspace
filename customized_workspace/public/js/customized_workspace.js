// Copyright (c) 2023, Anupam Kumar and contributors
// For license information, please see license.txt

$(window).on('load', function() {
    frappe.after_ajax(function () {
        if(frappe.session.user == "Administrator")
            return

        let has_role = frappe.boot.customized_workspace_settings.roles.filter(v => frappe.boot.user.roles.includes(v));
        if(!frappe.boot.customized_workspace_settings.roles.length || has_role.length > 1) {
            if (frappe.boot.customized_workspace_settings.hide_sidebar) {
                $('.layout-side-section').hide().empty();
            }
            if (frappe.boot.customized_workspace_settings.hide_edit_button) {
                $('.layout-side-section').hide().empty();
            }
            if (frappe.boot.customized_workspace_settings.hide_create_workspace_button) {
                $('.layout-side-section').hide().empty();
            }
        }
    });
})