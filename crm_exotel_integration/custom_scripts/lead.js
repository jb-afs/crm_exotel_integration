frappe.ui.form.on('Lead', {
	refresh(frm) {
		frm.add_custom_button(__(Call), function(){
            frappe.msgprint("in Button")    
        });
	}
})