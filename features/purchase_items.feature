Feature: Purchase Item flow

    Flow when purchasing itme in shop and out to cart

    @TC03
    Scenario: Successful Purchase
        Given user opens browser and is in home page
        When customer buys the following products
            | Product        | Quantity |
            | Stuffed Frog   | 2        |
            | Fluffy Bunny   | 5        |
            | Valentine Bear | 3        |
        Then product exists with correct prices and total in cart page