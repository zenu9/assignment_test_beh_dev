Scenario: Searching a Product based on Name
  Given the following products exist
    | name             | category | price | availability |
    | Product X       | Toys      | 15.00 | true        |
    | Product Y       | Toys      | 20.00 | false       |
  When I search for the product "Product X"
  Then I should receive the product "Product X"
