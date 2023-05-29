# Copyright (c) 2023, Anupam Kumar and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def boot_session(bootinfo):
    if frappe.session.user != 'Guest':
        customized_workspace_settings = frappe.get_doc("Customized Workspace Settings")

        bootinfo.customized_workspace_settings = {
            "hide_sidebar": customized_workspace_settings.hide_sidebar,
            "hide_edit_button": customized_workspace_settings.hide_edit_button,
            "hide_create_workspace_button": customized_workspace_settings.hide_create_workspace_button,
            "roles": customized_workspace_settings.get_roles(),
        }
