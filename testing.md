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

<!-- This project has been tested using the following browsers: -->

<!--Chrome, Safari & Edge-->

<!-- On the following devices
Desktop Macbook
Ipad Air Simulator on Dev Tools
Smallest phone size IPhone 5/SE simulator on Dev Tools -->

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

#### Logged in as admin

| Feature                                 | Expected Outcome                                       | Testing Performed                    | Result                                              | Pass/Fail |
| --------------------------------------- | ------------------------------------------------------ | ------------------------------------ | --------------------------------------------------- | --------- |
| Create team button | Css change on hover, takes user to Create team page | Clicked button | Background turned darker green, taken to Create Team page | Pass |

#### Logged in as other manager, team already created

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

### User Profile

### Create Team

### Edit Team

### Add Player

### Edit Player

### Players

### Teams

### Team Profile

### Edit User

### Rules