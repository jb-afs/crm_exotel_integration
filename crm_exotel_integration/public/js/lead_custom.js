frappe.ui.form.on('Lead', {
	refresh:function(frm) {
		if(frappe.user_roles.includes("Exotel Outbound Call") === true){
			frm.add_custom_button('Call', async function(){
				frappe.msgprint("Call Initiated.")
				let user_id = frappe.session.user
				const to_user_data = await frappe.db.get_doc('Exotel Caller ID Mapping', null, { 'user': user_id })
				if(to_user_data){
					frappe.call({
						method: 'crm_exotel_integration.api.call.initiating_call_numbers',
						args: {
							from_no: to_user_data.mobile_no,
							to_no:frm.doc.mobile_no,
							caller_id :to_user_data.exotel_caller_id
						},
						// freeze the screen until the request is completed
						freeze: true,
						callback: (r) => {
							// on success
							console.log(r)
						},
						
					})
				}else{
					frappe.throw("Please set your Exotel Caller ID before initiating a call.");
				}
				
			});
		}

		frm.fields_dict.custom_repossession_date.datepicker.update({ // Here date is the Todo field name.
            minDate: new Date(frappe.datetime.get_today()),
        });
		
	},
	custom_repossession_date:function(frm){
		var date_diff = frappe.datetime.get_day_diff(frm.doc.custom_repossession_date , frappe.datetime.nowdate())
		console.log(date_diff)
		frm.set_value("custom_ageing_in_days",date_diff)
		frm.refresh_field("custom_ageing_in_days")
	}
})