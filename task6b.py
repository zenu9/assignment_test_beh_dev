Scenario: Updating a Product
  Given the following products exist
    | name             | category | price | availability |
    | Sample Product   | Sample   | 9.99  | true         |
  When I update the product with id 1 to have name "Updated Product"
  Then the product with id 1 should have name "Updated Product"
