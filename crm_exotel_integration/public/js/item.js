frappe.ui.form.on('Item', {
	refresh:function(frm) {

		frm.fields_dict.custom_repossession_date.datepicker.update({ // Here date is the Todo field name.
            maxDate: new Date(frappe.datetime.get_today()),
        });
		
	},
	custom_repossession_date:function(frm){
		var date_diff = frappe.datetime.get_day_diff(frm.doc.custom_repossession_date , frappe.datetime.nowdate())
		frm.set_value("custom_ageing_in_days",Math.abs(date_diff))
		frm.refresh_field("custom_ageing_in_days")
	}
})