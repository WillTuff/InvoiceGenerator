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
address = Address('Acme Solutions', address = 'The Hague, Netherlands')

#inputs
itemQuantity = input("How many items would you like to add? ")

def GenerateInvoice():
    i, x = 0, 1
    invoice = Invoice(client, provider, creator)
    invoice.currency_locale = 'en_UK.UTF-8'
    invoice.currency = u'\u00a3'

    while i < itemQuantity:
        print('Please enter the details for Item ' + str(x))
        Quantity = raw_input("Please enter a quantity of good provided: ")
        Price = raw_input("Please enter the total price: ")
        Description = raw_input("Please enter a description: ")
        invoice.add_item(Item(Quantity, Price, Description))
        x += 1
        i += 1

    pdf = SimpleInvoice(invoice)
    invoiceName = "Invoice001.pdf"
    pdf.gen(invoiceName, generate_qr_code=True) 


GenerateInvoice()
print('Invoice Generated!')