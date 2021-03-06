# -*- coding: utf-8 -*-
# Copyright (c) 2018, Digitalprizm and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from bnd.api.attendance_list import load_data
import json
import requests

class AttendanceProcess(Document):
	def onload(self):
		alist=load_data()
		#frappe.msgprint("hii")
		self.get("__onload").attendance_list = alist


@frappe.whitelist()
def calling_attendance_api(process_date,enroll_number):
	r = requests.get('http://192.168.16.194/subtest/api/Aprocess?_date={0}&_enroll={1}'.format(process_date,enroll_number))
	api=r.text
	return api




@frappe.whitelist()
def calling_attendance_date_api(process_date):
	r = requests.get('http://192.168.16.194/subtest/api/Aprocess?_date={0}'.format(process_date))
	api=r.text
	return api

	
