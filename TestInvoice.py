import pytest
from Invoice import Invoice


@pytest.fixture()
def invoice():
    invoice = Invoice()
    return invoice
    
@pytest.fixture()
def products():
    products = {'Pen': {'qnt': 10, 'unit_price': 3.75, 'discount': 5},
                'Notebook': {'qnt': 5, 'unit_price': 7.5, 'discount': 10}}
    return products
    

def test_CanCalcucalateTotalImpurePrice(invoice, products):
    invoice.totalImpurePrice(products)
    assert invoice.totalImpurePrice(products) == 75

def test_CanCalcucateTotalDiscount(invoice, products):
    invoice.totalDiscount(products)
    assert invoice.totalDiscount(products) == 5.62

def test_CanCalcucalateTotalPurePrice(invoice, products):
    invoice.totalPurePrice(products)
    assert invoice.totalPurePrice(products) == 69.38

def test_CanCalcucalatePercentDiscount(invoice, products):
    invoice.percentDiscount(products)
    assert invoice.percentDiscount(products) == 8.100317094263477

# Jaypatel- This is test for making sure that tax amount adds up correctly.
def test_addTotalTax(invoice, products):
    invoice.addTotalTax(products)
    assert invoice.addTotalTax(products) == 4.69

# Jaypatel- This is test for making sure that the total amount with tax is displayed correcly.
def test_canCalculateTax (invoice, products):
    invoice.calculateTotalTax(products)
    assert invoice.calculateTotalTax(products) == 74.07

