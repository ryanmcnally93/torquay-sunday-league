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

### Edit Player

| Feature                                 | Expected Outcome                                       | Testing Performed                    | Result                                              | Pass/Fail |
| --------------------------------------- | ------------------------------------------------------ | ------------------------------------ | --------------------------------------------------- | --------- |

### Players

| Feature                                 | Expected Outcome                                       | Testing Performed                    | Result                                              | Pass/Fail |
| --------------------------------------- | ------------------------------------------------------ | ------------------------------------ | --------------------------------------------------- | --------- |

### Teams

#### As a Manager

| Feature                                 | Expected Outcome                                       | Testing Performed                    | Result                                              | Pass/Fail |
| --------------------------------------- | ------------------------------------------------------ | ------------------------------------ | --------------------------------------------------- | --------- |

#### As Administrator

| Feature                                 | Expected Outcome                                       | Testing Performed                    | Result                                              | Pass/Fail |
| --------------------------------------- | ------------------------------------------------------ | ------------------------------------ | --------------------------------------------------- | --------- |

### Team Profile

| Feature                                 | Expected Outcome                                       | Testing Performed                    | Result                                              | Pass/Fail |
| --------------------------------------- | ------------------------------------------------------ | ------------------------------------ | --------------------------------------------------- | --------- |

### Edit User

| Feature                                 | Expected Outcome                                       | Testing Performed                    | Result                                              | Pass/Fail |
| --------------------------------------- | ------------------------------------------------------ | ------------------------------------ | --------------------------------------------------- | --------- |
