Scenario: Deleting a Product
  Given the following products exist
    | name             | category | price | availability |
    | Sample Product   | Sample   | 9.99  | true         |
  When I delete the product with id 1
  Then the product with id 1 should not exist
