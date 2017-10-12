Feature: Baidu search test case
Scenario: search selenium
	Given I go to "http://www.baidu.com/"
	When I fill in field with id "kw" with "selenium"
	And I click id "su" with baidu once
	Then I should see "selenium" within 10 second


Scenario: search selenium2
	Given I go to "http://www.baidu.com/"
	When I fill in field with id "kw" with "selenium2"
	And I click id "su" with baidu once
	Then I should see "selenium2" within 10 second
	Then I close browser