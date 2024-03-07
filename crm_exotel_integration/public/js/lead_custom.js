frappe.ui.form.on('Lead', {
	refresh:function(frm) {
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
						caller_id :to_user_data.exotel_caller_id,
						call_type:"Transactional Calls"
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
})