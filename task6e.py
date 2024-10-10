Scenario: Searching a Product based on Category
  Given the following products exist
    | name             | category | price | availability |
    | Product A       | Electronics| 20.00| true        |
    | Product B       | Apparel   | 30.00 | false       |
  When I search for products in the category "Electronics"
  Then I should receive products in the category "Electronics"
