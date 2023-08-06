from erp_sync.Resources.resource import Resource


class Invoices(Resource):

    urls = {}

    def set_client_id(self, client_id):
        super().set_client_id(client_id)
        self._set_urls()
        return self

    def set_company_id(self, company_id):
        super().set_company_id(company_id)
        self._set_urls()
        return self

    def _set_urls(self):

        self.urls = {
            "new": f"/companies/{super().get_company_id()}/invoices",
            "edit": f"/companies/{super().get_company_id()}/invoices",
            "read": f"/companies/{super().get_company_id()}/invoices",
            "delete": f"/companies/{super().get_company_id()}/invoices",
            "import": f"/companies/{super().get_company_id()}/import_invoices"
        }

        super().set_urls(self.urls)

        return self

    def edit(self, ledger_id=None, payload=None, method='PUT', endpoint=None):
        
        self._set_urls()

        self.urls["edit"] = f'{self.urls["edit"]}/{ledger_id}'

        super().set_urls(self.urls)

        return super().edit(payload, method, endpoint)

    def read(self, invoice_id=None, payload=None, method='GET', endpoint=None):
        
        self._set_urls()

        if invoice_id is not None:
            self.urls["read"] = f'{self.urls["read"]}/{invoice_id}'
            super().set_urls(self.urls)

        return super().read(payload, method, endpoint)

    def delete(self, ledger_id=None, payload=None, method='DELETE', endpoint=None):
        
        self._set_urls()

        payload= { "type" : "SalesInvoice" }

        self.urls["delete"] = f'/{self.urls["delete"]}/{ledger_id}'

        super().set_urls(self.urls)

        return super().delete(payload, method, endpoint)

    def import_data(self, ledger_id=None, payload=None, method='GET', endpoint=None):
        
        self._set_urls()

        if ledger_id is not None:
            self.urls["import"] = f'{self.urls["import"]}/{ledger_id}'
            super().set_urls(self.urls)

        return super().import_data(payload, method, endpoint)

    def apply_credits(self, ledger_id=None, payload=None, method='POST', endpoint=None):

        endpoint = f'{self.urls["read"]}/{ledger_id}/apply_credits'

        return super().read(payload, method, endpoint)

    def invoice_payments(self, invoice_id=None, payload=None, method='GET', endpoint=None):

        endpoint = f'{self.urls["read"]}/{invoice_id}/payments'

        return super().read(payload, method, endpoint)

    def credits_applied(self, invoice_id=None, payload=None, method='GET', endpoint=None):

        endpoint = f'{self.urls["read"]}/{invoice_id}/credits_applied'

        return super().read(payload, method, endpoint)

    def invoice_types(self, endpoint="/invoice_types"):

        return super().read(endpoint=endpoint)

    def import_bills(self, invoice_id=None, payload=None, method='GET', endpoint=None):
        endpoint = f'/companies/{super().get_company_id()}/import_bills'

        if invoice_id is not None:
            endpoint = f'{endpoint}/{invoice_id}'

        return super().read(payload, method, endpoint)

    def payload(self):

        data = {
            "customer_ledger_id ": "<Enter customer id>",
            "item_ledger_id": "<Enter item id>",
            "amount": "<Enter amount>",
            "reference": "<reference>",
            "due_date": "<Enter invoice due date>",
        }

        # If client type is XERO
        if super().get_client_type() == super().XERO:
            data["chart_of_account_id"] = "<Enter chart of account id>"

        # If client type is ZOHO
        elif super().get_client_type() == super().ZOHO or super().get_client_type() == super().QBO:
            data.pop("reference")
            data.pop("due_date")

        return data

    def serialize(self, payload = None, operation = None):

        data = {}

        if operation is None:
            return "Specify the operation: Resource.READ, Resource.NEW or Resource.UPDATE"
        
        if operation == super().NEW or operation == super().UPDATE:

            data["type"] = "SalesInvoice"

            additional_properties = payload.get("additional_properties", {})

            # If client type is ZOHO
            if super().get_client_type() == super().ZOHO:

                if 'customer_ledger_id' in payload.keys():
                    data.update({
                        "customer_id": payload.get("customer_ledger_id", "")
                    })

                if 'reference' in payload.keys():
                    data.update({
                        "reference_number": payload.get("reference", "")
                    })

                if 'due_date' in payload.keys():
                    data.update({
                        "due_date": payload.get("due_date", "")
                    })

                line_items = {}

                if 'item_ledger_id' in payload.keys():
                    line_items.update({
                        "item_id": payload.get("item_ledger_id", "")
                    })

                if 'amount' in payload.keys():
                    line_items.update({
                        "rate": payload.get("amount", "")
                    })

                # if tax_components has data in it
                if bool(line_items):
                    data.update({
                        "line_items": [line_items]
                    })

            # If client type is Quickbooks Online
            elif super().get_client_type() == super().QBO:

                if 'customer_ledger_id' in payload.keys():
                    data.update({
                        "CustomerRef": {
                            "value": payload.get("customer_ledger_id", "")
                        }
                    })

                line_items = {}

                if 'amount' in payload.keys():
                    line_items.update({
                        "Amount": payload.get("amount", "")
                    })

                if 'item_ledger_id' in payload.keys():
                    line_items.update({
                        "SalesItemLineDetail": {
                                "ItemRef": {
                                    "value": payload.get("item_ledger_id", 0)
                                }
                            }
                    })

                # if tax_components has data in it
                if bool(line_items):
                    data.update({
                        "Line": [line_items]
                    })

            # If client type is XERO
            elif super().get_client_type() == super().XERO:

                invoices = {
                    "Status": f'{additional_properties.get("Status", "AUTHORISED")}'
                }

                if 'customer_ledger_id' in payload.keys():
                    invoices.update({
                        "Contact": {
                                "ContactID": payload.get("customer_ledger_id", "")
                            }
                    })

                if 'amount' in payload.keys():
                    invoices.update({
                        "LineItems": [
                                        {
                                            "TaxType": f'{additional_properties.get("Status", "NONE")}',
                                            "LineAmount": payload.get("amount", 0)
                                        }
                                    ]
                    })

                if 'date' in payload.keys():
                    invoices.update({
                        "DueDate": payload.get("due_date", "")
                    })

                if 'reference' in payload.keys():
                    invoices.update({
                        "Reference": payload.get("reference", "")
                    })                       

                if 'AccountID' in additional_properties.keys():
                    invoices["LineItems"][0].update({
                        "AccountID": f'{additional_properties.get("AccountID", 0)}'
                    })

                    additional_properties.pop("AccountID")
                
                if 'Status' in additional_properties.keys():
                    additional_properties.pop("Status")
                
                if 'TaxType' in additional_properties.keys():
                    additional_properties.pop("TaxType")

                # if tax_components has data in it
                if bool(invoices):
                    data.update({
                        "Invoices": [invoices]
                    })

            data.update(additional_properties)

            return data

        elif operation == super().READ:

            payload = super().response()

            data = payload

            # confirms if a single object was read from the database
            if isinstance(payload, dict):
                if 'resource' in payload.keys():
                    data = payload.get("resource", [])
                elif 'invoices' in payload.keys():
                    data = payload.get("invoices", [])
                
            # confirms if a single object was read from the database
            if isinstance(data, dict):
                data = [data]
            
            # confirms if data is a list
            if isinstance(data, list):

                if len(data) > 0:
                    for i in range(len(data)):                    
                        if 'total_amount' in data[i].keys():
                            data[i]['amount'] = data[i].pop('total_amount')
                        
            if 'invoices' in payload.keys():
                payload["invoices"] = data
            elif 'resource' in payload.keys():
                payload["resource"] = data

            super().set_response(payload)

            return self