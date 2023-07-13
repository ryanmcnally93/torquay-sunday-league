# Torquay Sunday League


<!--Image on all devices-->

This is a Sunday league football website, for a league based in Torquay. Languages include; HTML, CSS, JavaScript and Python. This application was created using the Flask framework, Postgres database and SQLAlchemy, and originally deployed on Heroku using ElephantSQL.

The season is about to begin in sunny Torquay but we have one more space open for a team to take part in the twelve teamed league. The user has the ability to register and upload their teams details for submission to the league.

They can create, read, update and delete any information and the same is set for their player and user information too. What players can view, edit and delete depends on whether the content is theirs or not, and security measures are in place to stop people from changing each others data in any way.

<!--Shields-->

## Deployment

<!--New deployment method and links-->

## UX

### Project Goal

To allow a user to input their team and players information, and give them the opportunity to edit that information before the finalization date.

#### Manager Goals

As a manager it's important to have full control over my account, my team information and player information in case of incorrect input, or a change in decision. I should be able to create, read, update and delete all information on the three subjects of user, team and player.

If the team I am submitting will be automatically rejected in any way I need clear indication as to how I can stop this from happening. I need to know the rules of this league and its application stage.

I also need to know my data is secure and cannot be changed by another manager.

- Create an account, which I can log in and out of
- Create a team and make changes or delete
- Add a player and make changes or delete
- View confirmed teams in the league
- Know my data is secure
- View the rules

| Goals | How are they achieved? |
| :----------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------- |
| Create an account, which I can log in and out of | User register, login and logout pages have been created, logging in creates a session cookie which is deleted when logged out. |
| Create a team and make changes or delete | There are buttons on the navbar, index page and the user is automatically taken to the create team once registered. The option to edit or delete the team is on the teams page. |
| Add a player and make changes or delete | Once a team has been created the user can view players and add to that list, with the option to edit or delete each one. |
| View confirmed teams in the league | These can be viewed by name in the table on the index page, and in more detail on the teams page. |
| Know my data is secure | Message on user edit page explains users can only edit and delete their accounts. Typing into the url can view another manager at best, but edit and delete buttons are missing and typing the functions into the url flashes a warning message that they cannot make changes. |
| View the rules | There is a page dedicated specifically to the rules of the league, the game itself and the application process. |

#### Player Goals

I could be viewing this website as a player without a team, in which case I would need to know the teams involved. If I view a teams page I should have some sort of contact information or location I can find the team at.

If I am an already signed player, I want to see my correct name and information has been confirmed on the website. I cannot edit it as I would need to speak to my manager to do that and I am informed on the register page that I do not need to create an account. I also need to know the rules of the league, game and application process.

Once the league starts I would also like to see my stats, including matches played and goals scored, etc.

View:
- Teams in the league
- Information of each team
- Players in teams
- Rules

| Goals | How are they achieved? |
| :----------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------- |
| Teams in the league | This information is on the index table and the teams page. Players cannot view unconfirmed teams. |
| Information of each team | Each team has a profile page with its location, contact information and number of players. |
| Players in teams | Once clicked onto the team profile you have the option to view its players. |
| Rules | There is a page dedicated specifically to the rules of the league, the game itself and the application process. |

#### Fan Goals

As a fan I want to know when the league starts, and when the fixture list will be confirmed so I can make relevant travel plans. I want to know what teams are playing and what players they have.

I also need to know of any rules that apply to me.

View:
- League start date
- Fixture list date
- Teams and info
- Players and info
- Rules

| Goals | How are they achieved? |
| :----------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------- |
| League start date | Included on index page and rules page |
| Fixture list date | Included on index page and rules page |
| Teams and info | On teams page |
| Players and info | View from team profile page |
| Rules | Page created |

#### Developer and Business Goals

Football is a fantastic sport for people of all ages and backgrounds to enjoy, it improves physical and mental capabilities whilst also creating a great social circle, whether you like to play, watch, officiate or manage. It can even lead to exciting and lucrative careers.

Our league in Torquay will consist of twelve teames, which play each other twice, home and away. The relevent match information will be included at a later date once all teams have been confirmed, as will player and team statistics. The league is for males participants only.

Torquay Sunday League needs to know that the managers can make relevent but restricted changes and that players and fans can find the information they need.

We also want to promote the league wherever possible.

- To promote football within the community
- To promote a fun footballing environment
- To give full access to confirmed teams and players
- To allow managers to submit teams
- To inform everyone of important dates and rules
- To create a site that responds to its user
- To create a secure site

| Goals | How are they achieved? |
| :----------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------- |
| To promote football within the community | All teams are within the local area, each has a name associated with a town or district within Torquay. Twelve teams with a minimum of sixteen players who will all have families is a lot of people! |
| To promote a fun footballing environment | The images across the site of very well known footballers, all either celebrating or fighting for the win in some way promote the fun aspect of the game. The site is bright in colours too. |
| To give full access to confirmed teams and players | All users, and unregistered viewers can get to know the names and faces of the teams and players within this league |
| To allow managers to submit teams | Once a managerial account has been created they can add a team with all the information and it's player information. |
| To inform everyone of important dates and rules | All included on index and rules pages. |
| To create a site that responds to its user | Flash and "invaid" messages appear across the site whenever incorrect or insufficient data is submitted. The flash messages also let the user know of any successful changes or submissions. |
| To create a secure site | All urls have been checked multiple times and edit and delete functions take parameters not known to other teams. Even if these parameters are discovered, the user needs to login with the correct hash-protected password written twice to make changes, as if done by the wrong user, changes will not be made.|

### User Stories

#### Unregistered User

All the restricted pages need an identifier to load properly, so the non registered user can only see Index, Teams, Team Profile, Login and Register. The homepage button says register now.

<!-- IMAGE -->

#### Manager One

Register, login and logout is successful. Delete account successful. Cannot edit or delete other managers, or access those buttons. You need to confirm password for registration and type current password to make changes to account.

Homepage button either says team name or create team, these are also available in the navbar.

On teams page I can view all the confirmed teams along with the team I create. I can only edit and delete my team however, and the create team button disappears when I have a team made. I can only view confirmed teams and players.

<!-- IMAGE -->

If I attempt to load the create_team url again it lets me fill in information but returns an error saying I can only have one team.

My profile page displays my team name, month joined and email address. When I change my club name it changes with me, as does my email. My team profile tells me I don’t have enough players until I do. I can create, read, edit and delete my players.

#### ManagerTwo

I have exact same capabilities as Manager One.

I cannot see managerone’s team at all on the team page. I wouldn’t be able to access it without knowing their username and team details. I cannot change or edit their data in any way.

#### Administrator

An account has been made, which logs in and out successfully.

Once logged in homepage button now says create team, as does navbar link, as I can create multiple teams. This is also mentioned on my profile.

<!-- IMAGE -->

I can view all teams but cannot edit or delete any that aren’t mine, even by typing into the url, as I don’t need to have that functionality. I have the option to confirm the team I am viewing. I can keep creating teams and players and deleting, but cannot repeat kit number in a team. I also cannot repeat a player name.

User profile displays clubs: multiple, user data can be changed but gives warning that their admin status may be affected if they change email address. This is due to some of the python code using if statements that look through the users information.

### Design Choices

The website needs to be fun and inviting, with bright colours and imagery. This site has a lot of written text so it is important to break it up with some imagery. I have viewed these websites for inspiration:

<a href="#">Site One</a>

#### Fonts

Undecided

#### Icons

Undecided

#### Colours

Undecided

#### Styling

Undecided

#### Backgrounds

On the Index, Teams and Players pages, we have two known premier league footballers. One on the left and one on the right. These players either face inwards or forwards but never outwards in any way, we want users focused on the center content. The players are wearing the same colour as one another.

IMAGE 2 Background pitch image Undecided

#### Images

Undecided, add gallery page?

### Wireframes

These wireframes were created using <a href="https://balsamiq.com/wireframes/?gad=1&gclid=Cj0KCQjwmN2iBhCrARIsAG_G2i4B-7yK8ylaMm-EgPZyIat6rzJi5BBNRLhY50Ej2SbjAHbQF2LMZocaAj9nEALw_wcB" target="_blank">Balsamiq Wireframes:</a>

<img src="/static/images/readme-images/index-wireframe.webp" width="50%" alt="Homepage" style="display: inherit; margin: auto;">

<img src="/static/images/readme-images/login-or-register-wireframe.webp" width="50%" alt="Homepage" style="display: inherit; margin: auto;">

<img src="/static/images/readme-images/create-team-wireframe.webp" width="50%" alt="Homepage" style="display: inherit; margin: auto;">

<img src="/static/images/readme-images/team-profile-wireframe.webp" width="50%" alt="Homepage" style="display: inherit; margin: auto;">

<img src="/static/images/readme-images/players-wireframe.webp" width="50%" alt="Homepage" style="display: inherit; margin: auto;">

<img src="/static/images/readme-images/teams-wireframe.webp" width="50%" alt="Homepage" style="display: inherit; margin: auto;">

<img src="/static/images/readme-images/add-edit-players-wireframe.webp" width="50%" alt="Homepage" style="display: inherit; margin: auto;">

<img src="/static/images/readme-images/user-profile-wireframe.webp" width="50%" alt="Homepage" style="display: inherit; margin: auto;">

<img src="/static/images/readme-images/rules-wireframe.webp" width="50%" alt="Homepage" style="display: inherit; margin: auto;">

### Prototype

- This index prototype was created on Figma.com.

<img src="/static/images/readme-images/index-prototype.webp" width="50%" alt="Index Prototype" style="display: inherit; margin: auto;">

### Q and A of Potential Users

Speak to a manager or captain of football team.
Speak to a regular sunday league player.
Speak to a footballing fan.

#### Q1 What makes a good website for football?

Manager:

- ""

Player:

- ""

Fan:

- ""

#### Q2 What information would you be looking for?

Manager:

- ""

Player:

- ""

Fan:

- ""

#### Q3 If you lived in Torquay, would you use this site?

Manager:

- ""

Player:

- ""

Fan:

- ""

#### Q4 Why?

Manager:

- ""

Player:

- ""

Fan:

- ""

#### Q5 What changes could I make?

Manager:

- ""

Player:

- ""

Fan:

- ""

#### Q6 What other information might managers/players/fans need?

Manager:

- ""

Player:

- ""

Fan:

- ""

#### Q7 Are the rules what you would expect? Should any be added?

Manager:

- ""

Player:

- ""

Fan:

- ""

#### Q8 Did you find it easy to achieve what you would want to achieve?

Manager:

- ""

Player:

- ""

Fan:

- ""

### Competitor Review

What other footballing leagues/teams are there in or near Torquay?

<a href="#">Site One</a>

Pros:

-

Cons:

-

### Roadmap

This roadmap indicates the importance and viability of specific opportunities.

| Opportunities/Problems               | Importance | Viability |
| ------------------------------------ | ---------- | --------- |
| League Table | 3          | 5         |
| User authentication       | 5          | 5         |
| CRUD functionality for users                    | 5          | 5         |
| CRUD functionality for teams            | 5          | 5         |
| CRUD functionality for players             | 5          | 5         |
| Rules page | 5          | 5         |
| Gallery                        | 3          | 4         |
| Team and Player statistics | 1 | 4 |
| Match information | 5 | 1 |

## Features

### Existing Features

#### Navigation Bar

- Explain

#### Footer

- Explain

#### Logo

- Explain

#### Index League Table

- Explain

#### Buttons

- Explain

#### Team Cards

- Explain

#### Profile pages

- Explain

#### Player Collapsibles

- Explain

#### Add/Edit/login and register form page elements

- Explain

#### Rules elements

- Explain

#### Gallery elements

- Explain

### Features Left to Implement

#### Stats

- Explain

#### Matches

- Explain

## Testing

CREATE TESTING DOCUMENT

I have tested my web application automatically and manually using Test Driven Development and Behaviour Driven Development.

### Automated Testing

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



### Manual Testing

<!-- This project has been tested using the following browsers: -->

<!--Chrome, Safari & Edge-->

<!-- On the following devices
Desktop Macbook
Ipad Air Simulator on Dev Tools
Smallest phone size IPhone 5/SE simulator on Dev Tools -->

<!-- `Homepage`

| Feature                                 | Expected Outcome                                       | Testing Performed                    | Result                                              | Pass/Fail |
| --------------------------------------- | ------------------------------------------------------ | ------------------------------------ | --------------------------------------------------- | --------- |
| Navbar links                            | Links take user to correct pages, CSS changes on hover | Clicked Links                        | All four links work, CSS changes on hover           | Pass      |
| All five other buttons (including logo) | Take user to the correct page, CSS changes on hover    | Clicked Buttons                      | All links work and change colour when hovered over  | Pass      |
| Burger icon on IPhone 5/SE              | Item is clickable and navbar readable                  | Clicked burger icon                  | Navbar opens vertically, links work                 | Pass      |
| Page layout                             | Layout changes to accommodate for smaller devices      | Opened site on IPhone 5/SE simulator | Every element visible through scrolling, links work | Pass      | -->

### Fixed Bugs

1). When trying to upload database using python3, I was getting an error saying "tsl" does not exist. This is because when setting up my env.py file, I short-handed the name of my project, not doing so anywhere else.

I fixed this issue by opening psql and changing the directory again to torquay_sunday_league, and when I tried again this worked.

2). Really struggled getting all of the main area content on one line. Salah (right player) was not staying on the same line as Odegaard (left player) and the table.

<!-- IMAGE -->

I fixed this in several steps, first, I made the table inline-table and the two players inline-block. This placed the three elements in a line, but the table's margin: auto property no longer centered it. I fixed this issue by using the margin-left: 50%, left: (half the width of the element) trick.

3). I couldn't update postgres after I made changes to the model.py file. Max character length was originally fifteen, but I needed it to be twenty-five.

<!-- CAUSE ERROR FOR IMAGE -->

I fixed this by discovering the DROP DATABASE and CREATE DATABASE commands in psql. Then I typed python3, import torquay_sunday_league from db, db.create_all() and exit().

Once I ran my run.py file then the database has been recreated, at the loss of all the stored user, team and player information.

4). When adding a player, the user is supposed to be transported back to the players page for the team currently being worked on. However, my page would only either load an empty player page, or werksoid would interject with an error, stating that "ID" was either not defined or defined incorrectly.

<!-- IMAGE -->

I fixed this by copying the line from the players app.route, placing in the players variable, however, this loaded without the new player visible. I placed the variable declaration after the commit message but before the return, and this fixed the issue.

<!-- IMAGE -->

5). I had an error showing when loading my login page, it said I didn’t have access.

<!-- CAUSE ERROR FOR IMAGE -->

I saw on Slack that other users discovered this issue on Code Anywhere, and when they switched to GitPod, the issue was gone. My belief was that this is because Code Anywhere has an issue with a file being called login.html, which probably refers to their own login page or something.

I fixed the issue by calling my login page and function log_in instead, which worked fine.

6). I had an issue with the Register and login pages when they loaded, if I backspaced, the inputs had both the label and last inputs, one of top of the other, it looked messy.

<!-- CAUSE ERROR FOR IMAGE -->

I added Javascript files to each page that had a form, to clear data as the page loads. Edit pages include old value but don't have the error now.

7). Originally I had number of players as a typed in property. I struggled to find the actual number of players from the team we were clicked onto.

I fixed this by searching the team table for the id passed in, and then realising that that table has a players attribute, iterated through that and incremented a variable with the original value of 0.

I then added a flash message for teams who have less than the required amount of players and added some javascript functionality so the css color and title attributes are added, giving the user more feedback on their number of players.

8). I had an issue with the delete team function, when creating the modal. I hadn’t watched the video all the way through and tried to add a script which called a function in js that called the jinja template which didn’t work.

I then was told on google to add it to in-line script. This didn’t work. I saw the modal tutorial on the video created by materialise and made changes.

<!-- CAUSE ERROR FOR IMAGE -->

I had a for loop error appear, which I discovered was because I had commented out a jinja template i was going to created in the future:

if team.created_by == session.user

The issue was even though it was commented out, the {%%} symbols were being used as normal, and as there was no endfor line, this was throwing an error.

9). Edit players team dropdown wasn’t working, I had to edit the for loop and it’s placement so the selected item was outside the for loop, and the if statement only returned items that weren’t equal to the team already selected as it was duplicating teams at first.

I then realised that you could edit a player and put him in another team, which shouldn't be allowed. As you have to go onto the teams page to view and add this particular player, I thought it best that we cannot change the club of that player, and I deleted the field.

12). User was logged in but the login page could be viewed if typed into the URL, and potentially a second user could be logged in. I added an if statement to the register and log_in pages to make sure there isn't somebody already logged in.

13). Had an error appear when trying to edit the create team route. I had added code to change the user.team_managed property but I realised I had typed user.team_managed == team.team_name when I should have typed user.team_managed = team.team_name.

14). I had an issue with the index page and teams page. These pages look through the user and team tables to view certain information, but when the user is not logged in they cannot access this.

<!-- IMAGE -->

I created an if statement that looks to see if there is a user logged in first and if there isn't one, the variables equal a string with the word None inside.

### Unfixed Bugs



### Responsive Design

#### Ipad Air screen resolution

Changes on each page

#### IPhone 5/SE screen resolution

Changes on each page

### API Integration

- Explain What, Why and How

## Credits

### Code

- The code environment was set up using the Code Institute template <!-- LINK TO TEMPLATE -->

- The modals, sidenav, datepicker, selects and collapsibles were created using <a href="materializecss.com" target="_blank">materializecss's</a> code.

- script.js contains some code from <a href="materializecss.com" target="_blank">materializecss</a> which initialises the modals, sidenav, datepicker, selects and collapsibles.

- The run.py, env.py, .gitignore, __init__.py, models.py and routes.py files were initially created by following the code institute tutorials, and making necessary changes and updates to adapt the code to my website.

### Web Tools

- This website was created on <!-- Link for Code Anywhere -->

- This is the site I used for my <a href="https://shields.io/category/analysis" target="_blank">Shields.</a>

- I compressed images using <a href="https://tinypng.com/" target="_blank">tinypng</a> given to me by Jo_ci on Slack.

<!-- - I resized images using this <a href="https://www.simpleimageresizer.com/upload" target="_blank">simple image resizer.</a> -->

- The colours were chosen using <a href="https://coolors.co/" target="_blank">Coolors.</a>

- The contrast was then checked using this contrast checker <a href="https://webaim.org/resources/contrastchecker/" target="_blank">Webaim</a>

- I changed the format of my images from jpg, png and jpeg to webp using <a href="https://convertio.co/png-webp/" target="_blank">convertio.</a>

### Media

- The image of Kevin De Bruyne was obtained from <a href="https://www.pngplay.com/image/494974">pngplay</a>, the uploader's name is "Arsh".

- The image of Enzo Fernández was obtained from <a href="https://www.footyrenders.com/premier-league/chelsea/enzo-fernandez-2/">footyrenders</a>, Cut by: "crisssnw".

- The image of Marcus Rashford was obtained from <a href="https://www.pinterest.co.uk/pin/marcus-rashford-render-england-view-and-download-football-renders-in-png-now-for-free-by-may-22-2018--655977501949397871/">footyrenders on pinterest</a>, the pinterest account is under "RilkeRainer".

- The image of Martin Ødegaard was obtained from <a href="https://www.footyrenders.com/premier-league/arsenal/martin-odegaard-45/">footyrenders</a>, Cut by: JvierGfx.

- The image of Aleksandar Mitrović was obtained from <a href="https://www.footyrenders.com/nations/serbia/aleksandar-mitrovic-3/">footyrenders</a>, Cut by: szwejzi.

- The image of Trent Alexander-Arnold was obtained from <a href="https://www.footyrenders.com/premier-league/liverpool/trent-alexander-arnold-72/">footyrenders</a>, Cut by: crisssnw.

### Acknowledgements

- My Mentor Jubril Akolade for continuous helpful feedback.

- My college contact Ben Smith for his support throughout.

- My other college contact Pasquale Fasulo for his support too.

- Tutor support and the Slack community at Code Institute for their help.

This readme.md was spellchecked using the spell checker extension for Chrome. <!-- BE SURE TO CHECK -->