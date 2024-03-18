import os
import csv
from frappeclient import FrappeClient

# ERPNext credentials and URL
erpnext_url = "https://finance-staging.qoala.app/"
erpnext_username = "Administrator"
erpnext_password = "Qoala@321"

# Connect to ERPNext
client = FrappeClient(erpnext_url, erpnext_username, erpnext_password)

def post_items_to_erpnext(row):
    
    name = client.get_value('Item',{'name':row.get('Item Code')},'item_code')
    if not name:
        doc = {'doctype':'Item',
        'item_code' : row.get('Item Code'),
        'item_name': row.get('Item Name'),
        'stock_uom': row.get('Default Unit of Measure'),
        'gst_hsn_code': row.get('HSN/SAC'),
        'description': row.get('Description'),
        'item_group': row.get('Item Group'),
        'allow_alternative_item' : row.get('Allow Alternative Item') or 0,
        'allow_negative_stock': row.get('Allow Negative Stock') or 0,
        'is_purchase_item': row.get('Allow Purchase') or 1,
        'is_sales_item': row.get('Allow Sales') or 1,
        'disabled': row.get('Disabled'),
        'is_stock_item' : row.get('Maintain Stock'),
        'has_variants': row.get('Has Variants') or 0,
        'include_item_in_manufacturing': row.get('Include Item In Manufacturing') or 0,
        'opening_stock': row.get('Opening Stock'),
        'valuation_rate': row.get('Valuation Rate'),
        'standard_rate' : row.get('Standard Selling Rate'),
        'is_fixed_asset': row.get('Is Fixed Asset') or 0,
        'auto_create_assets': row.get('Auto Create Assets on Purchase') or 0,
        'is_grouped_asset': row.get('Create Grouped Asset') or 0,
        'asset_category': row.get('Asset Category'),
        'asset_naming_series': row.get('Asset Naming Series'),
        'over_delivery_receipt_allowance': row.get('Over Delivery/Receipt Allowance (%)'),
        'over_billing_allowance': row.get('Over Billing Allowance (%)'),
        'brand': row.get('Brand'),
        'shelf_life_in_days': row.get('Shelf Life In Days'),
        'end_of_life': row.get('End of Life'),
        'default_material_request_type': row.get('Default Material Request Type'),
        'valuation_method': row.get('Valuation Method'),
        'warranty_period': row.get('Warranty Period (in days)'),
        'weight_per_unit': row.get('Weight Per Unit'),
        'weight_uom': row.get('Weight UOM'),
        'allow_negative_stock': row.get('Allow Negative Stock') or 0,
        'has_batch_no': row.get('Has Batch No') or 0,
        'create_new_batch': row.get('Automatically Create New Batch') or 0,
        'batch_number_series': row.get('Batch Number Series'),
        'has_expiry_date': row.get('Has Expiry Date') or 0,
        'retain_sample': row.get('Retain Sample') or 0,
        'sample_quantity': row.get('Max Sample Quantity'),
        'has_serial_no': row.get('Has Serial No') or 0,
        'serial_no_series': row.get('Serial Number Series'),
        'variant_of': row.get('Variant Of'),
        'variant_based_on': row.get('Variant Based On'),
        'enable_deferred_expense': row.get('Enable Deferred Expense') or 0,
        'no_of_months_exp': row.get('No of Months (Expense)'),
        'enable_deferred_revenue': row.get('Enable Deferred Revenue'),
        'no_of_months': row.get('No of Months (Revenue)'),
        'purchase_uom': row.get('Default Purchase Unit of Measure'),
        'min_order_qty': row.get('Minimum Order Qty'),
        'safety_stock': row.get('Safety Stock'),
        'lead_time_days': row.get('Lead Time in days'),
        'last_purchase_rate': row.get('Last Purchase Rate'),
        'is_customer_provided_item': row.get('Is Customer Provided Item') or 0,
        'customer': row.get('Customer'),
        'delivered_by_supplier': row.get('Delivered by Supplier (Drop Ship)') or 0,
        'country_of_origin': row.get('Country of Origin'),
        'customs_tariff_number': row.get('Customs Tariff Number'),
        'sales_uom': row.get('Default Sales Unit of Measure'),
        'grant_commission': row.get('Grant Commission') or 0,
        'max_discount': row.get('Max Discount (%)'),
        'inspection_required_before_purchase': row.get('Inspection Required before Purchase'),
        'quality_inspection_template': row.get('Quality Inspection Template'),
        'inspection_required_before_delivery': row.get('Inspection Required before Delivery'),
        'is_sub_contracted_item': row.get('Supply Raw Materials for Purchase'),
        'default_bom': row.get('Default BOM'),
        'customer_code': row.get('Customer Code'),
        'default_item_manufacturer': row.get('Default Item Manufacturer'),
        'default_manufacturer_part_no': row.get('Default Manufacturer Part No'),
        'published_in_website': row.get('Published in Website') or 0,
        'total_projected_qty': row.get('Total Projected Qty'),

        }

        client.insert(doc)
        print("Inserted Item " + row['Item Code'])
    else:
        print('Item ' + str(name['name']) + ' already present.')
    
def post_customers_to_erpnext(row):
    name = client.get_value('Customer',{'name':row.get('Customer Name')},'name')
    if not name:
        doc = {'doctype':'Customer',
               'salutation': row.get('Salutation'),
               'customer_name': row.get('Customer Name'),
               'customer_type': row.get('Customer Type'),
               'customer_group': row.get('Customer Group'),
               'territory': row.get('Territory'),
               'gender': row.get('Gender'),
               'lead_name': row.get('From Lead'),
               'opportunity_name': row.get('From Opportunity'),
               'account_manager': row.get('Account Manager'),
               'default_price_list': row.get('Default Price List'),
               'default_bank_account': row.get('Default Company Bank Account'),
               'default_currency': row.get('Billing Currency'),
               'is_internal_customer': row.get('Is Internal Customer'),
               'represents_company': row.get('Represents Company'),
               'market_segment': row.get('Market Segment'),
               'industry': row.get('Industry'),
               'customer_pos_id': row.get('Customer POS id'),
               'website': row.get('Website'),
               'language': row.get('Print Language'),
               'customer_details': row.get('Customer Details'),
               'customer_primary_contact': row.get('Customer Primary Contact'),
               'mobile_no': row.get('Mobile No'),
               'email_id': row.get('Email Id'),
               'customer_primary_address': row.get('Customer Primary Address'),
               'primary_address': row.get('Primary Address'),
               'tax_id': row.get('Tax ID'),
               'tax_category': row.get('Tax Category'),
               'tax_withholding_category': row.get('Tax Withholding Category'),
               'payment_terms': row.get('Default Payment Terms Template'),
               'loyalty_program': row.get('Loyalty Program'),
               'loyalty_program_tier': row.get('Loyalty Program Tier'),
               'default_sales_partner': row.get('Sales Partner'),
               'default_commission_rate': row.get('Commission Rate'),
               'so_required': row.get('Allow Sales Invoice Creation Without Sales Order'),
               'dn_required': row.get('Allow Sales Invoice Creation Without Delivery Note'),
               'is_frozen': row.get('Is Frozen'),
               'disabled': row.get('Disabled'),
               '': row.get(''),

            }
        client.insert(doc)
        print("Inserted Customer " + row['Customer Name'])
    else:
        print('Customer ' + str(name['name']) + ' already present.')

def post_supplier_to_erpnext(row):
    name = client.get_value('Supplier',{'name':row.get('Supplier Name')},'name')
    if not name:
        doc = {'doctype':'Supplier',
            'supplier_name': row.get('Supplier Name'),
            'country': row.get('Country'),
            'supplier_group': row.get('Supplier Group'),
            'supplier_type': row.get('Supplier Type'),
            'is_transporter': row.get('Is Transporter'),
            'default_currency': row.get('Billing Currency'),
            'default_bank_account': row.get('Default Company Bank Account'),
            'default_price_list': row.get('Price List'),
            'payment_terms': row.get('Default Payment Terms Template'),
            'is_internal_supplier': row.get('Is Internal Supplier'),
            'represents_company': row.get('Represents Company'),
            'supplier_details': row.get('Supplier Details'),
            'website': row.get('Website'),
            'language': row.get('Print Language'),
            'tax_id': row.get('Tax ID'),
            'tax_category': row.get('Tax Category'),
            'tax_withholding_category': row.get('Tax Withholding Category'),
            'supplier_primary_contact': row.get('Supplier Primary Contact'),
            'mobile_no': row.get('Mobile No'),
            'email_id': row.get('Email Id'),
            'supplier_primary_address': row.get('Supplier Primary Address'),
            'primary_address': row.get('Primary Address'),
            'allow_purchase_invoice_creation_without_purchase_order': row.get('Allow Purchase Invoice Creation Without Purchase Order'),
            'allow_purchase_invoice_creation_without_purchase_receipt': row.get('Allow Purchase Invoice Creation Without Purchase Receipt'),
            'is_frozen': row.get('Is Frozen'),
            'disabled': row.get('Disabled'),
            'warn_rfqs': row.get('Warn RFQs'),
            'warn_pos': row.get('Warn POs'),
            'prevent_rfqs': row.get('Prevent RFQs'),
            'prevent_pos': row.get('Prevent POs'),
            'on_hold': row.get('Block Supplier'),
            'hold_type': row.get('Hold Type'),
            'release_date': row.get('Release Date'),

            }
        client.insert(doc)
        print("Inserted Supplier " + row['Supplier Name'])
    else:
        print('Supplier ' + str(name['name']) + ' already present.')
        



# Find and process CSV files in the repository
repo_path = os.getcwd()

for root, dirs, files in os.walk(repo_path):
    for file in files:
        if file.endswith(".csv"):
            csv_path = os.path.join(root, file)

            print('Reading the file '+str(csv_path))
            
            # Read the entire CSV file into memory
            with open(csv_path, 'r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                rows = list(csv_reader)

            # Extract values from the second row
            header = rows[0]
            doctype = header.get('Doctype')
            inserted = header.get('Inserted')

            if inserted == '0':
                if doctype == 'Item':
                    # Use the remaining rows as data to push to ERPNext
                    for row in rows[1:]:
                        post_items_to_erpnext(row)

                elif doctype == 'Customer':
                    for row in rows[1:]:
                        post_customers_to_erpnext(row)

                elif doctype == 'Supplier':
                    for row in rows[1:]:
                        post_supplier_to_erpnext(row)

                # Update the 'Inserted' column in the second row
                header['Inserted'] = '1'

                # Write the modified data back to the CSV file
                with open(csv_path, 'w', newline='') as updated_csv_file:
                    csv_writer = csv.DictWriter(updated_csv_file, fieldnames=csv_reader.fieldnames)
                    csv_writer.writeheader()
                    csv_writer.writerows(rows)
