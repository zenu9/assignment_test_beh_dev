Scenario: Searching a Product based on Availability
  Given the following products exist
    | name             | category | price | availability |
    | Available Product| Home      | 25.00 | true        |
    | Unavailable Product| Home    | 25.00 | false       |
  When I search for available products
  Then I should receive only products that are available
