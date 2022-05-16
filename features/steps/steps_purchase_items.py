from behave import given, when, then, step
from assertpy import assert_that
from features.pages.home_page import HomePage
from features.pages.shop_page import ShopPage
from features.pages.cart_page import CartPage


@when('customer buys the following products')
def step_impl(context):
    page = ShopPage(context)
    page.click_shop_page()

    # Select product and click buy and throw prices in context
    context.prices = {}
    for row in context.table: 
        page.buy_products_by_name_and_quantity(row['Product'], int(row['Quantity']))
        context.prices[row['Product']] = page.get_product_price_by_name(row['Product'])


@then('product exists with correct prices and total in cart page')
def step_impl(context):
    page = CartPage(context)
    page.click_cart_page()

    # #Get all available purchase in cart
    purchase_list = page.get_all_purchases()

    #check item prices
    for item in context.prices:
        pruchase_price = purchase_list[item]['price']
        cart_price = context.prices[item]

        assert_that(pruchase_price).described_as('check currency').contains('$')  
        assert_that(cart_price).described_as('check currency').contains('$') 
        assert_that(pruchase_price).is_equal_to(cart_price)

    #Check if subtotal is correct
    for item in purchase_list:
        subtotal = purchase_list[item]['subtotal']
        price = float(purchase_list[item]['price'][1:])
        quantity = int(purchase_list[item]['quantity'])

        assert_that(subtotal).described_as('check currency').contains('$')
        currency = subtotal[:1]

        computed_subtotal = f'{currency}{(price * quantity)}'        
        assert_that(computed_subtotal).is_equal_to(subtotal)

    #Check if total is correct from subtotal and total
    computed_total = 0.00
    for item in purchase_list:
        subtotal = float(purchase_list[item]['subtotal'][1:])
        computed_total += subtotal

    assert_that(page.get_total()).described_as('check "total" text').contains('Total: ')
    
    total_amount = page.get_total()[7:]
    assert_that(f'{computed_total}').is_equal_to(total_amount)
