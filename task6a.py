Scenario: Reading a Product
  Given the following products exist
    | name             | category | price | availability |
    | Sample Product   | Sample   | 9.99  | true         |
  When I request to read a product with id 1
  Then I should receive a product with name "Sample Product"
