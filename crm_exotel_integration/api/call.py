import frappe
import requests
import json



@frappe.whitelist()
def initiating_call_numbers(from_no, to_no, caller_id, call_type):
    try:
        exotel_details = frappe.get_doc("CRM Exotel Settings")
        if not exotel_details.enabled:
            frappe.throw("Please enable CRM Exotel Settings!")

        exotel_api_key = exotel_details.api_key
        exotel_api_token = exotel_details.api_token
        exotel_account_sid = exotel_details.account_sid
        subdomain = exotel_details.subdomain
        app_id = exotel_details.app_id

        logs_url = f"https://{exotel_api_key}:{exotel_api_token}@{subdomain}/v1/Accounts/{exotel_account_sid}/Calls/connect"
        # logs_url = f"https://{subdomain}/v1/Accounts/{exotel_account_sid}/Calls/connect"

        # frappe.log_error(title="Exotel API Request", message=f"From: {from_no}, To: {to_no}, CallerId: {caller_id}, CallType: {call_type}")
        
        data = {
            'From': from_no,
            'To': to_no,
            'CallerId': caller_id,
            'CallType': call_type,
            'Url': f"http://my.exotel.com/{exotel_account_sid}/exoml/start_voice/{app_id}"
        }
        auth = (exotel_api_key, exotel_api_token)
        res = requests.post(logs_url, data=data, auth=auth)

        frappe.log_error("post call initiated",message=res.content)

        if res.status_code == 200:
            if res.content:
                res_json = res.json()
                frappe.log_error(title="Exotel API Response", message=res_json)
            else:
                frappe.throw("Empty response received from Exotel API")
        else:
            frappe.log_error(title="API Debug Information", message=f"URL: {logs_url}, Status Code: {res.status_code}, Response Content: {res.text}")
            frappe.throw(f"API call failed with status code {res.status_code}")
    except Exception as e:
        frappe.log_error(title="Exotel Api Call Failed", message=str(e))
