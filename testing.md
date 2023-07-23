# TSL Testing

I have tested my web application automatically and manually using Test Driven Development and Behaviour Driven Development.

## Automated Testing

### W3C Validation

<!-- <p>
  <a href="http://jigsaw.w3.org/css-validator/check/referer">
    <img  style="border:0;width:88px;height:31px;margin:auto;display:flex;"
          src="http://jigsaw.w3.org/css-validator/images/vcss"
          alt="Valid css!" />
    </a>
</p> -->

### Javascript Validation

<!--Jest Tests-->

#### JSHint



#### Python Validation

<!-- Unit tests -->

### Lighthouse



#### Mobile Lighthouse



## Manual Testing

This project has been tested using the following browsers:

Chrome
<!--Safari & Edge-->

On the following devices:

Desktop Macbook

<!-- Ipad Air Simulator on Dev Tools & Smallest phone size IPhone 5/SE simulator on Dev Tools -->

### Base

### Navbar

| Feature                                 | Expected Outcome                                       | Testing Performed                    | Result                                              | Pass/Fail |
| --------------------------------------- | ------------------------------------------------------ | ------------------------------------ | --------------------------------------------------- | --------- |
| Home Anchor | Css change on hover, takes user to Homepage | Clicked Home | Background turned grey, taken to home| Pass |
| Logo Anchor | Css change on hover, takes user to Homepage | Clicked the Logo | Background turned grey, taken to home| Pass |
| Teams Anchor | Css change on hover, takes user to Teams page | Clicked Teams | Background turned grey, taken to Teams page | Pass |
| Login Anchor | Css change on hover, takes user to Login page | Clicked Log In | Background turned grey, taken to Login page| Pass |
| Register Anchor | Css change on hover, takes user to Register page | Clicked Register | Background turned grey, taken to Register page | Pass |

### Footer

| Feature                                 | Expected Outcome                                       | Testing Performed                    | Result                                              | Pass/Fail |
| --------------------------------------- | ------------------------------------------------------ | ------------------------------------ | --------------------------------------------------- | --------- |
| Facebook Anchor | Css change on hover, takes user to Facebook on different tab | Clicked anchor | Text turned lighter green, new tab opened onto Facebook homepage| Pass |
| Twitter Anchor | Css change on hover, takes user to Twitter on different tab | Clicked anchor | Text turned lighter green, new tab opened onto Twitter homepage | Pass |
| Instagram Anchor | Css change on hover, takes user to Instagram on different tab | Clicked anchor In | Text turned lighter green, new tab opened onto Instagram homepage| Pass |
| TikTok Anchor | Css change on hover, takes user to TikTok on different tab | Clicked anchor | Text turned lighter green, new tab opened onto TikTok homepage | Pass |

### Homepage

#### Not logged in

| Feature                                 | Expected Outcome                                       | Testing Performed                    | Result                                              | Pass/Fail |
| --------------------------------------- | ------------------------------------------------------ | ------------------------------------ | --------------------------------------------------- | --------- |
| Register now button | Css change on hover, takes user to Register page | Clicked button | Background turned darker green, taken to Register page | Pass |

#### As Administrator

| Feature                                 | Expected Outcome                                       | Testing Performed                    | Result                                              | Pass/Fail |
| --------------------------------------- | ------------------------------------------------------ | ------------------------------------ | --------------------------------------------------- | --------- |
| Create team button | Css change on hover, takes user to Create team page | Clicked button | Background turned darker green, taken to Create Team page | Pass |

#### As Manager with team

| Feature                                 | Expected Outcome                                       | Testing Performed                    | Result                                              | Pass/Fail |
| --------------------------------------- | ------------------------------------------------------ | ------------------------------------ | --------------------------------------------------- | --------- |
| TEAM NAME Button | Css change on hover, takes user to Team Profile page | Logged in as managerone, with created team Liverpool, clicked Liverpool button on homepage | Background turned darker green, taken to Team Profile page | Pass |

### Log In

| Feature                                 | Expected Outcome                                       | Testing Performed                    | Result                                              | Pass/Fail |
| --------------------------------------- | ------------------------------------------------------ | ------------------------------------ | --------------------------------------------------- | --------- |
| Log in form | User is rejected as account doesn't exist | used random made up name to log in | Incorrect messsage appeared | Pass |
| Log in form | User is rejected as password is incorrect | used admin name but wrong password to log in | Same incorrect messsage appeared | Pass |
| Log in form | User is logged in, session cookie is created | Used admin credentials to log in | Taken to User Profile page, session cookie created | Pass |

### Register

| Feature                                 | Expected Outcome                                       | Testing Performed                    | Result                                              | Pass/Fail |
| --------------------------------------- | ------------------------------------------------------ | ------------------------------------ | --------------------------------------------------- | --------- |
| Username field | Red line error and message | Entered name less than 5 letters, Ryan | Red line appeared, if the rest of the information is entered and submit clicked, an error message appears | Pass |
| Username field | Red line error and message | Entered name more than 25 letters, ryanistryingtotestthisusername | Same line and incorrect messsage appeared | Pass |
| Email field | Red line error and message | Entered fake email without @ symbol | Same line and incorrect messsage appeared | Pass |
| Email field | Email is corrected to lowercase | Entered email with random uppercase letter, ryanmcNally@outlook.com | Clicked on profile and it had been made lowercase | Pass |
| Submit button | Doesn't submit | Clicked button when there was a red line | form did not post | Pass |
| Submit button | Account created, session created and user taken to create team page | Filled in information correctly, all green lines | Form posted, account created, session cookie created, create team page loaded | Pass |

### User Profile

| Feature                                 | Expected Outcome                                       | Testing Performed                    | Result                                              | Pass/Fail |
| --------------------------------------- | ------------------------------------------------------ | ------------------------------------ | --------------------------------------------------- | --------- |
| Edit User Button | CSS change and takes user to edit user form | Hovered then clicken on edit user button | Green button darkened, click took me to the correct form | Pass |
| Delete user button | Modal popup | Clicked on delete user | Modal popped up | Pass |
| Modal no button | Closes modal, user still on profile page | Clicked on no | Modal closed, still on page | Pass |
| Modal yes button | Modal closes, account deletes, session cookie deletes, user taken to login page | Clicked on yes | Modal closed, account deleted, session cookie deleted, taken to login page. Message to confirm deletion appeared. | Pass |

### Create Team

| Feature                                 | Expected Outcome                                       | Testing Performed                    | Result                                              | Pass/Fail |
| --------------------------------------- | ------------------------------------------------------ | ------------------------------------ | --------------------------------------------------- | --------- |
| Team Name Input | Red line error and message | Entered name less than 3 letters, "No" | Red line appeared, if the rest of the information is entered and submit clicked, an error message appears | Pass |
| Team Name Input | Cannot enter more than 25 letters | Entered name more than 25 letters, "ryanistryingtotestthisteamname" | Text stopped typing on 25th letter | Pass |
| Team Colour Input | Red line error and message | Entered colour less than 3 letters, "No" | Red line appeared, if the rest of the information is entered and submit clicked, an error message appears | Pass |
| Team Colour Input | Cannot enter more than 30 letters | Entered colour more than 30 letters, "ryanistryingtotestthisteamcolourinput" | Text stopped typing on 30th letter | Pass |
| Team Address Input | Red line error and message | Entered address less than 3 letters, "No" | Red line appeared, if the rest of the information is entered and submit clicked, an error message appears | Pass |
| Team Address Input | Cannot enter more than 25 letters | Entered address more than 25 letters, "ryanistryingtotestthisaddress" | Text stopped typing on 25th letter | Pass |
| Contact Input | Red line error and message | Entered input with a letter, "0796473615d" | Red line appeared, if the rest of the information is entered and submit clicked, an error message appears | Pass |
| Contact Input | Red line error and message | Entered number less than 11 characters long, "1234567890" | Red line appeared, if the rest of the information is entered and submit clicked, an error message appears | Pass |
| Contact Input | Red line error and message | Entered number more than 11 characters long, "123456789012" | Red line appeared, if the rest of the information is entered and submit clicked, an error message appears | Pass |
| Create Team button | Doesn't submit | Clicked button when there was a red line | form did not post | Pass |
| Create Team button | Team creates and user taken to teams page | Filled in information correctly, all green lines | Form posted, team created, teams page loaded | Pass |

### Edit Team

| Feature                                 | Expected Outcome                                       | Testing Performed                    | Result                                              | Pass/Fail |
| --------------------------------------- | ------------------------------------------------------ | ------------------------------------ | --------------------------------------------------- | --------- |
| All inputs | Red line appears | Tried to enter no data | Form wouldn't submit, asked for data | Pass
| All inputs | Red line appears | Tried to enter data outside min and max attributes | Form wouldn't submit, asked for correct data format | Pass
| File Upload element | Error message appears underneath | Tried to enter an ico image | Form wouldn't submit, error message appeared | Pass
| Remove Image button | Modal opens | Clicked button | Modal opened | Pass
| Modal No button | Takes me back to page | Clicked button | Took me back | Pass
| Modal Yes button | Image cannot be removed, as is default | Clicked button even though picture was already default image | Taken back to profile page, message given explaining image cannot be deleted | Pass
| Upload Correct image | Image uploads | Uploaded a jpg image | Image uploaded and even resized to fit circle | Pass
| Remove image button, Modal yes | Image deletes, default is set again | Clicked on remove image, then on modal's yes button | Image deleted, default image set. Image also removed from directory | Pass
| Team name input | Name changes | Typed in a new name and clicked submit | Name changed | Pass
| Colours input | Colours property changes | Typed in a new colours and clicked submit | Colours changed | Pass
| Address input | Address property changes | Typed in a new address and clicked submit | Address changed | Pass
| Contact input | Contact number changes | Typed in a new contact number and clicked submit | Contact number changed | Pass

### Add Player

| Feature                                 | Expected Outcome                                       | Testing Performed                    | Result                                              | Pass/Fail |
| --------------------------------------- | ------------------------------------------------------ | ------------------------------------ | --------------------------------------------------- | --------- |
| All inputs | Red line appears | Tried to enter data outside min and max attributes | Form wouldn't submit, asked for correct data format | Pass
| Name input | Player name is taken, so won't be added | Typed the name of a player I'd already created | Form did not submit, message displayed | Pass
| Kit Number input | Kit number is taken, so won't be added | Typed a used kit number | Form did not submit, message displayed | Pass
| Kit Number input | Kit number is taken by another team, so should still pass here | Typed a used kit number from a different team | Form submitted | Pass
| Kit Number input | Cannot go higher than 99, red line error | Typed in 100 | Red line and error message appeared | Pass
| Datepicker input | Cannot type into input | Clicked on input in several places | Could not enter anything other than a date | Pass
| Datepicker input | Cannot add future date, error message displays | Selected a future date | Error messaged displayed | Pass
| Add Player button | Red line appears, form doesn't send | Clicked button with 1 red line showing | form did not post | Pass |
| Add Player button | Player is created, user is taken to players page | Filled in information correctly, all green lines | Form posted, player created, players page loaded | Pass |

### Edit Player

| Feature                                 | Expected Outcome                                       | Testing Performed                    | Result                                              | Pass/Fail |
| --------------------------------------- | ------------------------------------------------------ | ------------------------------------ | --------------------------------------------------- | --------- |
| All inputs | Red line appears | Tried to enter data outside min and max attributes | Form wouldn't submit, asked for correct data format | Pass
| Datepicker input | Cannot change date | Clicked onto date | Date is grey, clicking does nothing | Pass
| Name input | Player name is taken, so won't be added | Typed the name of a player I'd already created | Form did not submit, message displayed | Pass
| Kit Number input | Kit number is taken, so won't be added | Typed a used kit number | Form did not submit, message displayed | Pass
| Kit Number input | Kit number is taken by another team, so should still pass here | Typed a used kit number from a different team | Form submitted | Pass
| Kit Number input | Cannot go higher than 99, red line error | Typed in 100 | Red line and error message appeared | Pass
| Name input | Player name updates | Typed in a new, untaken name | Name changed | Pass
| Kit number input | Player kit number updates | Typed in a number not taken | Kit number changed | Pass
| Position input | Player position updates | Typed in different position | Position changed | Pass
| Country input | Player country updates | Typed in different country | Country changed | Pass
| Edit Player button | Red line appears, form doesn't send | Clicked button with 1 red line showing | form did not post | Pass |
| Edit Player button | Player is edited, user is taken to players page | Filled in information correctly, all green lines | Form posted, player edited, players page loaded | Pass |

### Players

#### As Unregistered User or other manager

| Feature                                 | Expected Outcome                                       | Testing Performed                    | Result                                              | Pass/Fail |
| --------------------------------------- | ------------------------------------------------------ | ------------------------------------ | --------------------------------------------------- | --------- |
| Add Player button | Button should not be visible | Clicked onto players page | No button was visible | Pass |
| Player collapsibles | Player information is shown | Clicked collapsible player name | Information was visible underneath, other collapsibles close aswell | Pass |
| Player edit and remove buttons | Buttons should not be visible | Clicked collapsibles | No edit or delete buttons were visible | Pass |


#### As the Team's Manager

| Feature                                 | Expected Outcome                                       | Testing Performed                    | Result                                              | Pass/Fail |
| --------------------------------------- | ------------------------------------------------------ | ------------------------------------ | --------------------------------------------------- | --------- |
| Add Player button | CSS changes and button takes me to add player form | Clicked button | CSS visible and taken to form | Pass |
| Player collapsibles | Clicking on name produces info on player | Clicked collapsible | Players information and two buttons appeared, other collapsibles closed | Pass |
| Edit Button | CSS changes and button takes me to edit player form | Clicked button | CSS visible and taken to form | Pass |
| Delete Button, modal yes | Modal opens and allows me to delete the player | Clicked button | CSS visible and Modal opens, when yes is clicked player is deleted and modal closes revealing players page | Pass |

### Teams

#### As Unregistered User

| Feature                                 | Expected Outcome                                       | Testing Performed                    | Result                                              | Pass/Fail |
| --------------------------------------- | ------------------------------------------------------ | ------------------------------------ | --------------------------------------------------- | --------- |
| Teams cards | I can only read information | Looking through all teams | No edit or delete buttons are available, I can only read information | Pass |
| Confirm switch | I cannot change the switch setting | Clicked switch | Switch did not change | Pass |

#### As a Manager

| Feature                                 | Expected Outcome                                       | Testing Performed                    | Result                                              | Pass/Fail |
| --------------------------------------- | ------------------------------------------------------ | ------------------------------------ | --------------------------------------------------- | --------- |
| Other Teams cards | I can only read information | Looking through all teams | No edit or delete buttons are available, I can only read information | Pass |
| My Team's card | Edit and Delete buttons are visible | Viewing my team card on teams page | Buttons are visible | Pass |
| Edit Button | CSS changes and button takes me to edit team form | Clicked button | CSS visible and taken to form | Pass |
| Delete Button, modal yes | Modal opens and allows me to delete the team | Clicked button | CSS visible and Modal opens, when yes is clicked team is deleted and modal closes revealing teams page | Pass |
| Confirm switch | I cannot change the switch setting | Clicked switch | Switch did not change | Pass |

#### As Administrator

| Feature                                 | Expected Outcome                                       | Testing Performed                    | Result                                              | Pass/Fail |
| --------------------------------------- | ------------------------------------------------------ | ------------------------------------ | --------------------------------------------------- | --------- |
| Managers cards | I can only read information | Looking through all teams | No edit or delete buttons are available, I can only read information | Pass |
| My team cards | Edit and Delete buttons are visible | Viewing my team cards on teams page | Buttons are visible | Pass |
| Confirm switch | I can change the switch setting | Clicked switch, then submit | Team confirmation status changed, message shown | Pass |

### Team Profile

#### As Manager

| Feature                                 | Expected Outcome                                       | Testing Performed                    | Result                                              | Pass/Fail |
| --------------------------------------- | ------------------------------------------------------ | ------------------------------------ | --------------------------------------------------- | --------- |
| Edit Team button | CSS changes, user is taken to edit team form | Clicked button | CSS changed, edit team form opened | Pass |
| View Players button | CSS changes, user is taken to players page | Clicked button | CSS changed, players page opened | Pass |

#### As anyone else

| Feature                                 | Expected Outcome                                       | Testing Performed                    | Result                                              | Pass/Fail |
| --------------------------------------- | ------------------------------------------------------ | ------------------------------------ | --------------------------------------------------- | --------- |
| Edit team button | Button is not visible | Clicked onto teams page | Button was not visible | Pass |

### Edit User

| Feature                                 | Expected Outcome                                       | Testing Performed                    | Result                                              | Pass/Fail |
| --------------------------------------- | ------------------------------------------------------ | ------------------------------------ | --------------------------------------------------- | --------- |
| All inputs | Red line appears | Tried to enter data outside min and max attributes | Form wouldn't submit, asked for correct data format | Pass
| Image upload element | Does not accept wrong file type | Gave an ico image | Form did not submit, error message shown | Pass |
| Image upload element | Image changes | Gave correct image type | Picture changed and even resized | Pass |
| Removing default image | Cannot remove | Clicked remove image on default image | Was given error message and taken back to user profile | Pass |
| Removing my image | Removes image, reverts back to default image | Clicked on remove image when IO had one uploaded | Picture removed, fault set, old picture deleted from directory | Pass |
| Email address input | Email address changes | Typed in new address, correct format and current password | Information updated | Pass |
| New password input | Can change the password | Typed in new password and current password correctly | Password changed | Pass |
| Confirmation input | Could not change any data with wrong password | Typed in random string | Form did not post any new data, error message received | Pass |
| Email and password inputs | Can change both at same time | New information given in both, correct current password entered | Data updated successfully | Pass |
| Submit button | Red line appears, form doesn't send | Clicked button with 1 red line showing | form did not post | Pass |
| Submit Player button | User info is edited, user is taken to their profile page | Filled in information correctly, all green lines | Form posted, user info edited, users profile page loaded | Pass |

### Logout
| Feature                                 | Expected Outcome                                       | Testing Performed                    | Result                                              | Pass/Fail |
| --------------------------------------- | ------------------------------------------------------ | ------------------------------------ | --------------------------------------------------- | --------- |
| Log out Navbar anchor | User logs out | Clicked anchor whilst logged in | Session cookie is deleted, user is taken to log in page | Pass |