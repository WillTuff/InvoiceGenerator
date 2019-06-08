import os
from tempfile import NamedTemporaryFile
from InvoiceGenerator.api import Invoice, Item, Client, Provider, Creator, Address
from InvoiceGenerator.pdf import SimpleInvoice

#choose english as language
os.environ["INVOICE_LANG"] = "en"

accNumber = '00000000'
sortCode = '000000'
client = Client('The Inside Story')
provider = Provider('Totness Web Services, 4 Broadway, Guiseley, Leeds', 
    bank_account=accNumber, bank_code=sortCode)
creator = Creator('')
# address = Address('Acme Solutions', address = 'The Hague, Netherlands')

Quantity = raw_input("Please enter a quantity of good provided: ")
Price = raw_input("Please enter the total price: ")
Description = raw_input("Please enter a description: ")

def GenerateInvoice():
    invoice = Invoice(client, provider, creator)
    invoice.currency_locale = 'en_UK.UTF-8'
    invoice.currency = u'\u00a3'
    invoice.add_item(Item(Quantity, Price, Description))

    pdf = SimpleInvoice(invoice)

    invoiceName = "Invoice001.pdf"

    pdf.gen(invoiceName, generate_qr_code=True) 


GenerateInvoice()
print('Invoice Generated!')
