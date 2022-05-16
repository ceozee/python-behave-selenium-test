Feature: Submit feedback - Behavior Driven

    Submit feedback in Jupiter site using different inputs and formats

    Background: user visits jupiter website
        Given user opens browser and is in home page

    @TC00 @negative
    Scenario: Unsuccessful submit feedback using invalid login email
        Given customer access contact page
        When following fields are entered
            | Field    | Value                         |
            | Forename | Zee                           |
            | Email    | thisisnotavalidemail          |
            | Message  | This message is a failed test |
        Then error in the field is displayed
            | Field | Message |
            | Email error | Please enter a valid email |


    Scenario: Successful validation of error messages in empty field in submit feedback page
        Given customer access contact page
        When submit button is clicked
        Then error in the field is displayed
            | Field          | Message              |
            | Forename error | Forename is required |
            | Email error    | Email is required    |
            | Message error  | Message is required  |
        When following fields are entered
            | Field    | Value                             |
            | Forename | Zee                               |
            | Email    | csims@planittesting.com           |
            | Message  | This message is a Successful test |
        Then errors will disappear in contact page


    @TC02 @positive @multiple
    Scenario Outline: Successful submission of feedback
        Given customer access contact page
        When customer submits feedback form with the following values
            | Field    | Value      |
            | Forename | <forename> |
            | Email    | <email>    |
            | Message  | <message>  |
        Then it should display that feedback submission is successful

        Examples:
            | forename | email                   | message         |
            | Zee      | csims@planittesting.com | Message for 1st |
            | Zee      | csims@planittesting.com | Message for 2nd |
            | Zee      | csims@planittesting.com | Message for 3rd |
            | Zee      | csims@planittesting.com | Message for 4th |
            | Zee      | csims@planittesting.com | Message for 5th |