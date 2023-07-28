# TSL Testing

I have tested my web application automatically and manually using Test Driven Development and Behaviour Driven Development.

## Automated Testing

### W3C Validation

#### HTML

All the following HTML documents (which are written using Jinja templates), have been validated using the [W3C Validator.](https://validator.w3.org/nu/#textarea)

##### Base

- Tha base URL only returned errors when misreading the Jinja templates. I will disregard these on future HTML documents.

##### Index

- The only issue on this page was the register button, there are four elements with the same ID. However, there will only ever be one of these elements actually visible on the page so this is okay.

##### Live Scores

- There was a stray closing tab on my datepicker input, which is self-closing.
- I'd also forgotten to add alt attributes to my flags, which are there now.

##### Teams

- Another stray end input tag.
- The switches were span elements, which could not have a type attribute. I tried changing to a p or a div, but the validator doesn't like whatever type it is. I have not moved the element outside the label in case it messes with the layout of the card.
- The teams-row wasn't closing because I had an if statement that opened two divs but never closed them both. I fixed this validation error by inserting another if statement below so there are the right amount of divs for the validator and the page itself.

##### Log In

- The login page received no further errors.

##### Register

- The register page received no further errors.

##### Create Team

- The create team page received no further errors.

##### Edit Team

- I had an element with two alt attributes, which has been changed.

##### Players

- The players page received no further errors.

##### Add Player

- The only error that wasn't a Jinja template was the kit numbers input, which had a pattern attribute checking for blank space. I removed this and the input still didn't accept empty space.

##### Edit Player

- This page had the same kit number input error, which has been corrected.

##### Team Profile

- This page had the same two alt attribute error on one of the elements, which has been fixed.

##### User Profile

- The user profile page has an error of duplicate ID's, but these are within an if statement and only one will ever show.

- The user picture had the same two alt attribbutes error, which has been fixed.

##### Edit User

- The user picture had the same two alt attribbutes error, which has been fixed.

##### Rules

- The rules page received no further errors.

#### CSS

Initially, the [W3C Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) came back with 3 errors on my style.css.

- 2 were the Aspect ratio's, which were set at 1 and 1.5 instead of 1/1 and 1.5/1.
- The other was a media query with a space not added.

Both have since been fixed.

<p>
  <a href="http://jigsaw.w3.org/css-validator/check/referer">
    <img  style="border:0;width:88px;height:31px;margin:auto;display:flex;"
          src="http://jigsaw.w3.org/css-validator/images/vcss"
          alt="Valid css!" />
    </a>
</p>

### Javascript Validation

I have tested all my JavaScript code using JSHint

#### JSHint

- The main [script.js](/torquay_sunday_league/static/js/script.js) file returned 9 warnings that were letting me know that "const" and "let" are available in ES6. No other errors were found.

- The [log_in.js](/torquay_sunday_league/static/js/log_inscript.js) file returned no errors.

- The [player_form_script.js](/torquay_sunday_league/static/js/player_form_script.js) file returned no errors.

- The [register_script.js](/torquay_sunday_league/static/js/register_script.js) file returned no errors.

- The [team_form_script.js](/torquay_sunday_league/static/js/team_form_script.js) file returned no errors.

- The [team_profile_script.js](/torquay_sunday_league/static/js/team_profile_script.js) file returned no errors.

- The [password_visibility.js](/torquay_sunday_league/static/js/password_visibility.js) file returned no errors.

#### Python Validation

The following py documents have been tested using [extendsclass.](https://extendsclass.com/python-tester.html)

- [run.py](run.py) returned with no errors.
- [models.py](torquay_sunday_league/models.py) returned with no errors.
- [__init__.py](torquay_sunday_league/__init__.py) returned with no errors.
- [routes.py](torquay_sunday_league/routes.py) returned with some errors. I have used f in strings to specify that the items in curly braces are not to be read as string.

<img src="/torquay_sunday_league/static/images/readme-images/testing-routes.webp" width="80%" alt="The teams page, viewed on desktop" style="display: inherit; ">

I have also played aroung with unittest to try and create tests, similar to my Jest JavaScript tests used in my last project.

### Lighthouse

- The only issues I had with my desktop lighthouse scores were my forgotten alt attribute on the smaller profile picture icon and the collapsibles contrast, both of which have now been resolved.

#### Homepage

<img src="/torquay_sunday_league/static/images/readme-images/home-desk.png" width="80%" alt="Homepage on desktop" style="display: inherit; ">

#### Live Scores

<img src="/torquay_sunday_league/static/images/readme-images/live-scores-desk.png" width="80%" alt="Live scores page on desktop" style="display: inherit; ">

#### Teams

<img src="/torquay_sunday_league/static/images/readme-images/teams-desk.png" width="80%" alt="Teams page on desktop" style="display: inherit; ">

#### Login

<img src="/torquay_sunday_league/static/images/readme-images/login-desk.png" width="80%" alt="The login page on desktop" style="display: inherit; ">

#### Register

<img src="/torquay_sunday_league/static/images/readme-images/register-desk.png" width="80%" alt="The register page on desktop" style="display: inherit; ">

#### Rules

<img src="/torquay_sunday_league/static/images/readme-images/rules-desk.png" width="80%" alt="The rules page on desktop" style="display: inherit; ">

#### Create Team

<img src="/torquay_sunday_league/static/images/readme-images/create-team-desk.png" width="80%" alt="The create team page on desktop" style="display: inherit; ">

#### Edit Team

<img src="/torquay_sunday_league/static/images/readme-images/edit-team-desk.png" width="80%" alt="The edit team page on desktop" style="display: inherit; ">

#### Team Profile

<img src="/torquay_sunday_league/static/images/readme-images/team-profile-desk.png" width="80%" alt="The team profile page on desktop" style="display: inherit; ">

#### Add Player

<img src="/torquay_sunday_league/static/images/readme-images/add-player-desk.png" width="80%" alt="The add player page on desktop" style="display: inherit; ">

#### Edit Player

<img src="/torquay_sunday_league/static/images/readme-images/edit-player-desk.png" width="80%" alt="The edit player page on desktop" style="display: inherit; ">

#### User Profile

<img src="/torquay_sunday_league/static/images/readme-images/user-profile-desk.png" width="80%" alt="The users profile on desktop" style="display: inherit; ">

#### User Edit

<img src="/torquay_sunday_league/static/images/readme-images/user-edit-desk.png" width="80%" alt="The user edit page on desktop" style="display: inherit; ">

#### Players

<img src="/torquay_sunday_league/static/images/readme-images/players-desk.png" width="80%" alt="The players page on desktop" style="display: inherit; ">

#### Mobile Lighthouse

- The only issue with the mobile lighthouse checks were the social media icon margins, which have also been resolved since these images were taken.

#### Homepage

<img src="/torquay_sunday_league/static/images/readme-images/home-mobile.png" width="80%" alt="Homepage on mobile" style="display: inherit; ">

#### Live Scores

<img src="/torquay_sunday_league/static/images/readme-images/live-scores-mobile.png" width="80%" alt="Live scores page on mobile" style="display: inherit; ">

#### Teams

<img src="/torquay_sunday_league/static/images/readme-images/teams-mobile.png" width="80%" alt="Teams page on mobile" style="display: inherit; ">

#### Login

<img src="/torquay_sunday_league/static/images/readme-images/login-mobile.png" width="80%" alt="The login page on mobile" style="display: inherit; ">

#### Register

<img src="/torquay_sunday_league/static/images/readme-images/register-mobile.png" width="80%" alt="The register page on mobile" style="display: inherit; ">

#### Rules

<img src="/torquay_sunday_league/static/images/readme-images/rules-mobile.png" width="80%" alt="The rules page on mobile" style="display: inherit; ">

#### Create Team

<img src="/torquay_sunday_league/static/images/readme-images/create-team-mobile.png" width="80%" alt="The create team page on mobile" style="display: inherit; ">

#### Edit Team

<img src="/torquay_sunday_league/static/images/readme-images/edit-team-mobile.png" width="80%" alt="The edit team page on mobile" style="display: inherit; ">

#### Team Profile

<img src="/torquay_sunday_league/static/images/readme-images/team-profile-mobile.png" width="80%" alt="The team profile page on mobile" style="display: inherit; ">

#### Add Player

<img src="/torquay_sunday_league/static/images/readme-images/add-player-mobile.png" width="80%" alt="The add player page on mobile" style="display: inherit; ">

#### Edit Player

<img src="/torquay_sunday_league/static/images/readme-images/edit-player-mobile.png" width="80%" alt="The edit player page on mobile" style="display: inherit; ">

#### User Profile

<img src="/torquay_sunday_league/static/images/readme-images/user-profile-mobile.png" width="80%" alt="The users profile on mobile" style="display: inherit; ">

#### User Edit

<img src="/torquay_sunday_league/static/images/readme-images/user-edit-mobile.png" width="80%" alt="The user edit page on mobile" style="display: inherit; ">

#### Players

<img src="/torquay_sunday_league/static/images/readme-images/players-mobile.png" width="80%" alt="The players page on mobile" style="display: inherit; ">

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

### API Scores Page
| Feature                                 | Expected Outcome                                       | Testing Performed                    | Result                                              | Pass/Fail |
| --------------------------------------- | ------------------------------------------------------ | ------------------------------------ | --------------------------------------------------- | --------- |
| Datepicker input | Doesn't accept text | Clicked tab until on datepicker | Could not enter text | Pass |
| Datepicker input | Opens Datepicker | Clicked on datepicker input field | Datepicker opened | Pass |
| Search button | Doesn't allow no data to be entered | Clicked on button with no data entered | Message opened, did not POST | Pass |
| Search button | Returns correct results when date entered | Entered dates with no matches and with some matches | Correct response | Pass |