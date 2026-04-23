// Copyright (c) 2026, AdilKM and contributors
// For license information, please see license.txt

frappe.ui.form.on("Rider Order", {
	refresh(frm) {
        if(frm.doc.status !== "Accepted"){
            frm.add_custom_button("Accepet",()=>{
                frm.set_value("status","Accepted");
                frm.save();
            }, "Actions");
            frm.add_custom_button("Reject",()=>{
                frm.set_value("status","Rejectedd");
                frm.save();
            }, "Actions");
        }
	},
});
