# Torquay Sunday League


<img src="/torquay_sunday_league/static/images/readme-images/main-readme.webp" width="50%" alt="The TSL website on multiple devices" style="display: inherit; ">

This is a Sunday league football website, for a league based in Torquay. Languages include; HTML, CSS, JavaScript and Python. This application was created using the Flask framework, Postgres database and SQLAlchemy, and originally deployed on Heroku using ElephantSQL.

The season is about to begin in sunny Torquay but we have one more space open for a team to take part in the twelve teamed league. The user has the ability to register and upload their teams details for submission to the league.

They can create, read, update and delete any information and the same is set for their player and user information too. What players can view, edit and delete depends on whether the content is theirs or not, and security measures are in place to stop people from changing each others data in any way.

<p align="center">

<img src="https://img.shields.io/github/stars/ryanmcnally93/project-three-torquay-sunday-league?style=social" style="max-width: 100%; margin: 0 10px 10px 0;" alt="Stars">

<img src="https://img.shields.io/github/repo-size/ryanmcnally93/project-three-torquay-sunday-league" style="max-width: 100%; height: 20px; margin: 0 0 10px 10px;" alt="Size of repo">

<br>

<img src="https://img.shields.io/github/issues-raw/ryanmcnally93/project-three-torquay-sunday-league" style="max-width: 100%; height: 20px margin-right: 10px;" alt="Open issues">

<img src="https://img.shields.io/github/last-commit/ryanmcnally93/project-three-torquay-sunday-league?color=green&style=for-the-badge" style="max-width: 100%; height: 20px; margin-left: 10px;" alt="GitHub last commit">

</p>

## Deployment

To deploy my first Heroku project, I followed the steps set by Code Institute.

- Create an account on ElephantSQL
- Create new instance and copy database URL
- Create a Procfile and requirements.txt file
- Add an if statement to ensure SQLAlchemy can read my external database.
- Create new app on Heroku
- Enter config vars, including the copied URL
- Click on deploy, connect to github, find the repository
- Click Deploy Branch
- Once that is done, click more, and run console.

It was importing the database from torquay_sunday_league that first provided issues.

My requirements.txt hadn't created an instance for the 'requests' module which needed to be installed. I checked the version I had and provided it in the file.

- I tried again and it worked, after this I opened the app and entered the teams data into the database.

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

All the restricted pages need an identifier to load properly, so the non registered user can only see Index, Teams, Team Profile, Login and Register. The homepage button says register now. As a fan I can view the teams and players that are about to start the upcoming season.

<img src="/torquay_sunday_league/static/images/readme-images/unregistered.webp" width="50%" alt="Unregistered User's view" style="display: inherit; ">

This image shows the team page, which will only display the confirmed teams, and all we can do is read the information.

#### Manager One

Register, login and logout is successful. Delete account successful. Cannot edit or delete other managers, or access those buttons. You need to confirm password for registration and type current password to make changes to account.

Homepage button either says team name or create team, these are also available in the navbar.

On teams page I can only view all confirmed teams along with the team I create. I can only edit and delete my team however, and the create team button disappears when I have a team made. The switch is disabled and there is a paragraph element which tells me if the team is confirmed or not, but I cannot change this.

<img src="/torquay_sunday_league/static/images/readme-images/managerone.webp" width="50%" alt="Manager user's view" style="display: inherit; ">

If I attempt to load the create_team url again it lets me fill in information but returns an error saying I can only have one team.

My profile page displays my team name, month joined and email address. When I change my club name it changes with me, as does my email. My team profile tells me I don’t have enough players until I do. I can create, read, edit and delete my players.

#### ManagerTwo

I have exact same capabilities as Manager One.

I cannot see managerone’s team at all on the team page. I wouldn’t be able to access it without knowing their username and team details. I cannot change or edit their data in any way.

#### Administrator

An account has been made, which logs in and out successfully.

Once logged in homepage button now says create team, as does navbar link, as I can create multiple teams. This is also mentioned on my profile.

I can view all teams but cannot edit or delete any that aren’t mine, even by typing into the url, as I don’t need to have that functionality. I have the option to confirm the team I am viewing. I can keep creating teams and players, editing and deleting as I please.

<img src="/torquay_sunday_league/static/images/readme-images/admin.webp" width="50%" alt="Administrator's view" style="display: inherit; ">

User profile displays clubs: multiple, user data can be changed but gives warning that their admin status may be affected if they change email address. This is due to some of the python code using if statements that look through the users information.

### Design Choices

The website needs to be fun and inviting, with bright colours and imagery. This site has a lot of written text so it is important to break it up with some imagery.

#### Fonts

I wanted a font that looked professional and tidy, but also looked a bit different from the normal fonts. For this I chose Ysabeau Infant, with a backup of sans-serif if this doesn't work.

I added it to the body element's CSS then made sure the unaffected elements had the correct font-family attribute.

<img src="/torquay_sunday_league/static/images/readme-images/font.webp" width="50%" alt="The Font used" style="display: inherit; ">

#### Icons

The icons chosen were mostly used in the form pages. I tried, where possible, to relate them to football. I added shirt for kit number, a calendar for the datepicker, a flag for the country and a football for the position. I also added footballs to the homepage too.

<img src="/torquay_sunday_league/static/images/readme-images/icons.webp" width="25%" alt="Icons used" style="display: inherit; ">

The user is always referred to with the user icon, or the user plus icon if a new user is being added.

#### Colours

I decided before I even started coding that as this is a grassroots football league the base colour should be green, as a reference to the grass. I started by using different shades of the same green all over my site, with the only difference being in the images I had added.

<img src="/torquay_sunday_league/static/images/readme-images/green.webp" width="90%" alt="The index page, illustrating the green colour used" style="display: inherit; ">

I then decided later when creating forms, that a second colour should be decided for the icons. After going through many colours I landed on a dark turquoise colour that goes well with the greens.

<img src="/torquay_sunday_league/static/images/readme-images/turq-with-green.webp" width="50%" alt="The combination of turquoise and green" style="display: inherit; ">

Later discovered with the additional buttons on the teams page it would be beneficial to have a colour for each option, with a darker tone added when hovered over.

<img src="/torquay_sunday_league/static/images/readme-images/buttons.webp" width="40%" alt="The four colours used on the buttons on the teams page" style="display: inherit; ">

#### Styling

Most of my content is centered in the middle of the page, with a few exceptions. This is so the user is focused on the content, and nothing is missed or forgotten to the side.

I have used border radius throughout my site, with the number of px relevant to the size of the element.

Most margins are of 20px, and all elements have a decent amount of padding.

#### Backgrounds

On the Index and Players pages, we have two known premier league footballers. One on the left and one on the right. These players either face inwards or forwards but never outwards in any way, we want users focused on the center content. The players are wearing the same colour as one another.

<img src="/torquay_sunday_league/static/images/readme-images/trent-and-odegaard.webp" width="70%" alt="Trent Alexander-Arnold and Martin Odegaard, premier league players." style="display: inherit; ">

On the other pages we have a background image of a corner being taken in a sunday league game. This image is mostly horizontal, so not suitable for smaller, more vertical devices. For this, I've added an image change when the device is smaller, and the image is a vertical one of a pitch with a goalpost in the distance.

<img src="/torquay_sunday_league/static/images/background-image.webp" width="50%" alt="Sunday League corner kick" style="display: inherit; ">

#### Images

The images I have used are all showing sunday league teams and players. The images are aimed low so there is no stadium in the background, as we want them to be relevant to grassroots football.

<img src="/torquay_sunday_league/static/images/rules-two.webp" width="50%" alt="A football referee" style="display: inherit; ">

The only exception to this rule is the transparent images of the premier league footballers, which are just used for fun and familiarity.

### Wireframes

These wireframes were created using <a href="https://balsamiq.com/wireframes/?gad=1&gclid=Cj0KCQjwmN2iBhCrARIsAG_G2i4B-7yK8ylaMm-EgPZyIat6rzJi5BBNRLhY50Ej2SbjAHbQF2LMZocaAj9nEALw_wcB" target="_blank">Balsamiq Wireframes:</a>

<img src="/torquay_sunday_league/static/images/readme-images/index-wireframe.webp" width="50%" alt="Homepage Wireframe" style="display: inherit; ">

<img src="/torquay_sunday_league/static/images/readme-images/login-or-register-wireframe.webp" width="50%" alt="Login Wireframe" style="display: inherit; ">

<img src="/torquay_sunday_league/static/images/readme-images/create-team-wireframe.webp" width="50%" alt="Create Team Wireframe" style="display: inherit; ">

<img src="/torquay_sunday_league/static/images/readme-images/team-profile-wireframe.webp" width="50%" alt="Team Profile Wireframe" style="display: inherit; ">

<img src="/torquay_sunday_league/static/images/readme-images/players-wireframe.webp" width="50%" alt="Players Wireframe" style="display: inherit; ">

<img src="/torquay_sunday_league/static/images/readme-images/teams-wireframe.webp" width="50%" alt="Teams Wireframe" style="display: inherit; ">

<img src="/torquay_sunday_league/static/images/readme-images/add-edit-players-wireframe.webp" width="50%" alt="Add/Edit Players Wireframe" style="display: inherit; ">

<img src="/torquay_sunday_league/static/images/readme-images/user-profile-wireframe.webp" width="50%" alt="User Profile Wireframe" style="display: inherit; ">

<img src="/torquay_sunday_league/static/images/readme-images/rules-wireframe.webp" width="50%" alt="Rules Wireframe" style="display: inherit; ">

### Prototype

- This index prototype was created on Figma.com.

<img src="/torquay_sunday_league/static/images/readme-images/index-prototype.webp" width="70%" alt="Homepage Prototype" style="display: inherit; ">

### Q and A of Potential Users

Speak to a manager or captain of football team.
Speak to a regular sunday league player.
Speak to a footballing fan.

#### Q1 What makes a great football league website?

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

#### Q3 Would you use this site?

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

#### Torbay Clearance Services, South Devon Football League

Well, on the FA's website <a href="https://fulltime.thefa.com/index.html?league=316369219" target="_blank">the Torbay Clearance Services, South Devon Football League</a> has a page.

Pros:

- Managing to get yourself onto the FA's website isn't easy, and they have a hit counter at 3 million!

- The stats, matches and respect pages are fantastic. They are very well organised.

- The navbar drops down clickable results and the styling is very consistent with the branding.

- A fantastic webpage for any league.

Cons:

- The season is about to begin and no fixtures are displayed.

- There are adverts EVERYWHERE! The FA has a lot of brands advertising underneath the header, within the footer, and to the left and right.

- The footer links don't have any hover qualities.

- There's no player information.

- If you were a manager, you'd need to ask for team information to be updated by an FA representitive, you wouldn't have any control over it yourself.

- As this page is probably used by multiple leagues, it doesn't have that leagues branding. The page doesn't have its own stamp.

#### Same league, different website

As this is the only league local to Torquay, and they don't have their own site, there are multiple websites that have produced information for this league.

This one is <a href="https://clubnets.co.uk/southdevonleague/" target="_blank">Clubnets.</a>

Pros:

- This site actually has match information on the right hand side, and it looks like its coming from an FA API.

- There are contact details including name, email and phone numbers for all the contacts relevant to the league.

- News articles for the matches up and coming.

Cons:

- Design elements all over the place, badge covers the title of the page, which is so small in context to the rest of the page it's almost invisible.

<img src="/torquay_sunday_league/static/images/readme-images/clubnets-1.webp" width="50%" alt="Clubnet's design fault" style="display: inherit; ">

- Too many borders, everything is in a box within a box and its all visible.

<img src="/torquay_sunday_league/static/images/readme-images/clubnets-2.webp" width="50%" alt="Clubnet's border fault" style="display: inherit; ">

- Use of colours isn't consistent, and site looks messy.

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

- The navigation bar is smaller than on my other projects, the links are clear, visible, have hover properties and when made smaller, the burger icon is visible. There is a green shadowed line underneath it that was originally styled by materializecss, but I altered the colour and shadow properties.

<img src="/torquay_sunday_league/static/images/readme-images/navbar.webp" width="100%" alt="The Navbar" style="display: inherit; ">

#### Footer

- This is the same height as the Navbar, I gave the top the same green shadowed line as the navbar. I also included some social links, a link to take the user to the top of the page (which could really help if on a long mobile page), and the rules page link.

- I placed the rules page link as I've noticed a lot of professional looking sites tend to have their more official information in the footer, like terms and conditions, contact info, etc.

<img src="/torquay_sunday_league/static/images/readme-images/footer.webp" width="100%" alt="The Footer" style="display: inherit; ">

#### Logo

- I got the design idea from the Torquay United FC badge. The arrow is exactly the same, and I noticed that if you open canva and grab a triangle image, the default colour is the same as the Torquay United colour! (Coincidence? Surely not!).

- I created four of the arrows and made them my green colour to go with the site, using the abbreviation TSL for Torquay Sunday League.

<img src="/torquay_sunday_league/static/images/logo.webp" width="25%" alt="TSL Logo" style="display: inherit; ">

#### Index League Table

- The league table format contains a for loop and if statement, so only the confirmed teams will display within the table. This prevents more than 12 teams being visible within it and gives the administrator complete control over it.

- The "position" is determined by the loop.index of the team, meaning none of the numbers are skipped by unconfirmed teams.

<img src="/torquay_sunday_league/static/images/readme-images/table.webp" width="50%" alt="The table" style="display: inherit; ">

#### Last Year Section

- This section lets visitors know of the winners of last years competition, and gives recognition to the top goalscorer of that year.

<img src="/torquay_sunday_league/static/images/readme-images/winners-section.webp" width="70%" alt="The winners section" style="display: inherit; ">

#### Team Cards

- The team cards display the buttons that the viewer is allowed to see, there are two types of card that can be called, one with two buttons, and the other with four. They both have their own CSS properties making them all consistent in padding, margin and colours.

<img src="/torquay_sunday_league/static/images/readme-images/buttons.webp" width="40%" alt="The buttons used" style="display: inherit; ">

#### Profile Pages

- The profile pages of the users and teams are consistent, with the same backgrounds, edit forms and similar boxes of information underneath.

- There are also profile images which can be edited and deleted. If edited, the old picture is deleted from the dom, if the remove image option is chosen, the default image is set. The default images are never deleted.

<img src="/torquay_sunday_league/static/images/readme-images/profiles.webp" width="50%" alt="One of the profile pages" style="display: inherit; ">

#### Player Collapsibles

- The player collapsibles arrange by kit numbers, and they display this alongside their full name.

- When extended, they show information regarding the player, such as their nationality, the position they play and they date they joined their team.

<img src="/torquay_sunday_league/static/images/readme-images/player-collapsibles.webp" width="60%" alt="The player collapsibles" style="display: inherit; ">

#### Form Pages

- The form pages are consistent, with fields that have relevant icons and submit or create buttons.

- The forms that you can change profile images on display the old image, and have the upload image input above the other inputs.

<img src="/torquay_sunday_league/static/images/readme-images/forms.webp" width="50%" alt="One of the forms used" style="display: inherit; ">

#### Rules Page

- This page accurately displays all the rules relevant to most sunday leagues, displaying information regarding the appropriate kit wear, administration process and respect expectations.

<img src="/torquay_sunday_league/static/images/readme-images/rules-page.webp" width="50%" alt="The rules page" style="display: inherit; ">

### Features Left to Implement

#### Stats

- Once the teams are finalised, each teams stats should be visible, perhaps on their profile page. This could display their top goalscorers, cards, etc.

#### Matches

- Once the teams are finalised, another page should be created showing the fixture list and showing stats from previous results between the two teams being viewed.

#### Teams Bio

- Another future feature could be a textarea bio area for each teams profile page, containing a brief history of the club and its location, achievements and players.

## Testing

You can view all testing in [this document.](https://github.com/ryanmcnally93/project-three-torquay-sunday-league/blob/main/testing.md)

### Fixed Bugs

1). When trying to upload database using python3, I was getting an error saying "tsl" does not exist. This is because when setting up my env.py file, I short-handed the name of my project, not doing so anywhere else.

I fixed this issue by opening psql and changing the directory again to torquay_sunday_league, and when I tried again this worked.

2). Really struggled getting all of the main area content on one line. Salah (right player) was not staying on the same line as Odegaard (left player) and the table.

<img src="/torquay_sunday_league/static/images/readme-images/bug-2.webp" width="70%" alt="Salah bug" style="display: inherit; ">

I fixed this in several steps, first, I made the table inline-table and the two players inline-block. This placed the three elements in a line, but the table's margin: auto property no longer centered it. I fixed this issue by using the margin-left: 50%, left: (half the width of the element) trick.

3). I couldn't update postgres after I made changes to the model.py file. Max character length was originally twenty, but I needed it to be twenty-five.

<img src="/torquay_sunday_league/static/images/readme-images/bug-3.webp" width="80%" alt="A dataerror" style="display: inherit; ">

I fixed this by discovering the DROP DATABASE and CREATE DATABASE commands in psql. Then I typed python3, import torquay_sunday_league from db, db.create_all() and exit().

Once I ran my run.py file then the database has been recreated, at the loss of all the stored user, team and player information.

4). When adding a player, the user is supposed to be transported back to the players page for the team currently being worked on. However, my page would only either load an empty player page, or werksoid would interject with an error, stating that "ID" was either not defined or defined incorrectly.

<img src="/torquay_sunday_league/static/images/readme-images/bug-4.webp" width="60%" alt="ID code used" style="display: inherit; ">

I fixed this by copying the line from the players app.route, placing in the players variable, however, this loaded without the new player visible. I placed the variable declaration after the commit message but before the return, and this fixed the issue.

<img src="/torquay_sunday_league/static/images/readme-images/fix-4.webp" width="100%" alt="Line that fixed the issue" style="display: inherit; ">

5). I had an error showing when loading my login page, it said I didn’t have access.

<img src="/torquay_sunday_league/static/images/readme-images/bug-5.webp" width="70%" alt="Access denied" style="display: inherit; ">

I saw on Slack that other users discovered this issue on Code Anywhere, and when they switched to GitPod, the issue was gone. My belief was that this is because Code Anywhere has an issue with a file being called login.html, which probably refers to their own login page or something.

I fixed the issue by calling my login page and function log_in instead, which worked fine.

6). I had an issue with the Register and login pages when they loaded, if I backspaced, the inputs had both the label and last inputs, one of top of the other, it looked messy.

I added Javascript files to each page that had a form, to clear data as the page loads. Edit pages include old value but don't have the error now.

7). Originally I had number of players as a typed in property. I struggled to find the actual number of players from the team we were clicked onto.

I fixed this by searching the team table for the id passed in, and then realising that that table has a players attribute, iterated through that and incremented a variable with the original value of 0.

<img src="/torquay_sunday_league/static/images/readme-images/fix-7.webp" width="60%" alt="Number of players accumulator" style="display: inherit; ">

I then added a flash message for teams who have less than the required amount of players and added some javascript functionality so the css color and title attributes are added, giving the user more feedback on their number of players.

8). I had an issue with the delete team function, when creating the modal. I hadn’t watched the video all the way through and tried to add a script which called a function in js that called the jinja template which didn’t work.

I then was told on google to add it to in-line script. This didn’t work. I saw the modal tutorial on the video created by materialise and made changes.

<img src="/torquay_sunday_league/static/images/readme-images/bug-8.1.webp" width="100%" alt="Template Syntax Error" style="display: inherit; ">

I had a for loop error appear, which I discovered was because I had commented out a jinja template i was going to created in the future:

<img src="/torquay_sunday_league/static/images/readme-images/bug-8.2.webp" width="100%" alt="Commented out jinja template" style="display: inherit; ">

The issue was even though it was commented out, the {%%} symbols were being used as normal, and as there was no endfor line, this was throwing an error.

9). Edit players team dropdown wasn’t working, I had to edit the for loop and it’s placement so the selected item was outside the for loop, and the if statement only returned items that weren’t equal to the team already selected as it was duplicating teams at first.

I then realised that you could edit a player and put him in another team, which shouldn't be allowed. As you have to go onto the teams page to view and add this particular player, I thought it best that we cannot change the club of that player, and I deleted the field.

10). User was logged in but the login page could be viewed if typed into the URL, and potentially a second user could be logged in. I added an if statement that adds a message to the page to say you are logged in as (username).

<img src="/torquay_sunday_league/static/images/readme-images/bug-10.webp" width="100%" alt="Undefined Error" style="display: inherit; ">

This however did not work and returned this result:

<img src="/torquay_sunday_league/static/images/readme-images/fix-10.webp" width="70%" alt="Log in page message" style="display: inherit; ">

This was part of a larger issue I was having. With the help of a tutor I recognised that my code for testing the session was wrong. I believed that a session cookie meant I was logged in. So I was writing (if session:), which would give true on some incorrect pages.

I changed this to (if 'user' in session:) instead, which resolved a lot of issues I was having.

11). Had an error appear when trying to edit the create team route. I had added code to change the user.team_managed property but I realised I had typed user.team_managed == team.team_name when I should have typed user.team_managed = team.team_name.

12). I had an issue with the index page and teams page. These pages look through the user and team tables to view certain information, but when the user is not logged in they cannot access this.

<img src="/torquay_sunday_league/static/images/readme-images/bug-12.webp" width="50%" alt="KeyError" style="display: inherit; ">

I created an if statement that looks to see if there is a user logged in first and if there isn't one, the variables equal a string with the word None inside.

<img src="/torquay_sunday_league/static/images/readme-images/fix-12.webp" width="70%" alt="Code used to fix issue" style="display: inherit; ">

13). I had an issue with the datepicker returning american dates. At first entry I had changed the JavaScript so that the date would view on the front end correctly when entering the player join date. But when I went to edit a player this happened.

<img src="/torquay_sunday_league/static/images/readme-images/bug-13.webp" width="60%" alt="Datepicker bug" style="display: inherit; ">

As you can see, the month on the left and the month on the right are different. This is because the datepicker is confusing month and date. After hours with a tutor trying different bits of code and multiple attempts to fix I realised I had confused things more than necessary.

I changed the Db type to string instead of date, and disabled the input on the edit player page, as the date a player has joined a club doesn't change anyway!

14). During my CSS changes, I had originally decided to have the left and right players on the index, teams page and players pages. However, the teams page looked like this:

<img src="/torquay_sunday_league/static/images/readme-images/bug-14.webp" width="60%" alt="Players hidden on teams page" style="display: inherit; ">

You could not see the players and it was pointless having them on there. I decided to change the background so it was the same as the other pages. With the players page, I chose a different approach, moving one player to the side and the players collapsibles to the other.

15). I noticed on larger tablet devices that my footer element was not at the bottom of the page.

<img src="/torquay_sunday_league/static/images/readme-images/bug-15.webp" width="50%" alt="Footer issue" style="display: inherit; ">

Simply adding position: absolute, width: 100% and bottom: 0 didn't work, as when on bigger screens if you scroll down the footer didn't follow the scroll, it stayed in the wrong position.

I looked at using the sticky position too, but on mobile devices it takes up unnecessary space.

This issue was fixed with the help of a tutor, who showed me that by giving the body and html height 100% and making the flow direction go downwards, the footer would stay where it needs to.

16). I had an issue with my players page giving a result that I had no players in a team which had. I quickly realised this was because I was using a variable in my routes file to reference the number of players, even though I had already assigned a no_of_players attribute to my model! I wasn't utilising this at all.

I made the number increase and decrease with the creation and deletion of a player within that team.

17). I had an issue where if I was viewing someone elses team, the navbar anchor that displays my team name changes to theirs! This was because 'team' had the value of the team I was viewing.

I fixed this by creating two variables where needed, one with base team, which referenced the team which should be shown in the navbar. The other was current team, which is the team we are currently viewing.

19). My mentor Jubril showed me that my create team form allowed me to fill in every input with an empty string of spaces! This resulted in a team with blank spaces for properties.

<img src="/torquay_sunday_league/static/images/readme-images/bug-19.webp" width="80%" alt="The teams page, viewed on desktop" style="display: inherit; ">

To get around this I utilised the pattern attribute where I could. The syntax ^\S(?:.*\S)?$ doesn't allow a space at the start or end of the value. This meant a form could not be filled with spaces.

20). When calling the API I managed to get results populating and started the CSS for the page when I hit a keyerror issue on 'matches'. My code hadn't changed.

This was because the initial call to the API before the post didn't have header=header and therefore didn't have the token added to the header. Once the number of requests for a guest ran out, so did my access. I placed the headers=headers into the return statement and it worked again.

### Unfixed Bugs

To the best of my knowledge, there are no known bugs left to fix.

### Responsive Design

<img src="/torquay_sunday_league/static/images/readme-images/desktop.webp" width="80%" alt="The teams page, viewed on desktop" style="display: inherit; ">

- The teams page, viewed on desktop.

#### Ipad Air screen resolution

- On devices with a smaller screen width that 1200px, the background image changes to adapt for longer pages.

- On smaller screen widths, the navbar disappears and is replaced by the burger icon, which opens a sidenav. This is the same on mobile devices.

- The team cards on the teams page display from 4 across to 3 across, and then to 2 across when needed. 

- On the players page, The right footballer is more central than before and the left player disappears, leaving more space for the collapsibles.

<img src="/torquay_sunday_league/static/images/readme-images/ipad.webp" width="50%" alt="The teams page on IPad" style="display: inherit; ">

- On the live scores page, I added scroll to the list so it can handle any amount of matches, and made the players invisible below 1000px wide so as not to distract from the results on show.

#### IPhone 5/SE screen resolution

- All headings and their respective boxes change in size to adapt to a smaller page, keeping their centralisation.

- Social media links in the footer have less margin so they don't push one another onto the next line.

- On index page, the player on the right disappears and the left player is centralised behind the table, the winners and goalscorer images are stacked on top of each other instead of side-by-side.

- The footballs either side of the main header element disappear and the same icons appear around the button displayed under the sub-heading.

- The league table widens to allow room for the team names.

- The team cards on the team page are in one column.

- On the players page the second player disappears and the collapsibles centralise.

- The images on the rules page centralise within the div.

- Profil page content widens to make use of smaller screens.

<img src="/torquay_sunday_league/static/images/readme-images/mobile.webp" width="50%" alt="The teams page on Mobile" style="display: inherit; ">

### API Integration

For my API live scores page, I used [football-data.org.](https://www.football-data.org/) This has access to all the live scores from the biggest competitions in world football, and a lot of them can be accessed for free!

In an ideal scenario this page would display the scores from the league the site is for, but as this is fictional, I'm showing the results from the available top leagues of the world.

#### Process

I signed up for an account on the API website and received this email.

<img src="/torquay_sunday_league/static/images/readme-images/api-token.webp" width="50%" alt="API email" style="display: inherit; ">

I then created the live scores html and app.route. Within this route I added the header variable and passed it the credentials received within the email.

I gave the variable matches the value of all the matches today, and made that appear on screen loadup, while the post function returns the url for individual date results with todays date passed in using the correct format.

I then used Jinja templates to only show competitions that had matches in and added messages when there were no games, and gave it all CSS properties.

#### Issues

I watched the Code Institute videos on API integration and in particular, the star wars API integration. This was achieved in JavaScript, which I followed as much as I could, but was stumped on how to alter my header to add the credentials.

I discovered on a Stack Overflow the way to do this in Python so went from there. I managed to get the data to display all matches in JSON format like this:

<img src="/torquay_sunday_league/static/images/readme-images/api-data.webp" width="50%" alt="API issues" style="display: inherit; ">

However, I passed the data the wrong words, like winner and team instead of matches. I was stuck for a while until a tutor helped me find which word I needed to pass into data to deconstruct the JSON file and render what I wanted.

I struggled with the boxing of the matches and splitting them by competition, as in the JSON file the matches aren't a child of competition. I achieved this by using loop.index and loop.last and adding the start and eng tags of my div within them, creating a box around the results.

<img src="/torquay_sunday_league/static/images/readme-images/api-loops.webp" width="50%" alt="API loops" style="display: inherit; ">

## Credits

### Code

- The code environment was set up using the <a href="https://github.com/Code-Institute-Org/ci-full-template" target="_blank">Code Institute Template.</a>

- The modals, sidenav, datepicker, selects and collapsibles were created using <a href="materializecss.com" target="_blank">materializecss's</a> code.

- script.js contains some code from <a href="materializecss.com" target="_blank">materializecss</a> which initialises the modals, sidenav, datepicker, selects and collapsibles.

- The run.py, env.py, .gitignore, __init__.py, models.py and routes.py files were initially created by following the code institute tutorials, and making necessary changes and updates to adapt the code to my website.

### Web Tools

- To integrate user authentication on Postgres, I coded along with <a href="https://www.youtube.com/watch?v=7EeAZx78P2U" target="_blank">this YouTube video</a>, by user "Sandeep Sudhakaran", making my own changes for my site to function.

- When wanting to allow users to upload profile pictures I watched and followed along the steps shown in <a href="https://www.youtube.com/watch?v=803Ei2Sq-Zs" target="_blank">this YouTube video</a>, by "Corey Schafer", making my own changes for my site to function.

- This website was created on <a href="https://codeanywhere.com/" target="_blank">Code Anywhere.</a>

- This is the site I used for my <a href="https://shields.io/category/analysis" target="_blank">Shields.</a>

- I compressed images using <a href="https://tinypng.com/" target="_blank">tinypng</a> given to me by Jo_ci on Slack.

- I resized images using this <a href="https://www.simpleimageresizer.com/upload" target="_blank">simple image resizer.</a>

- The contrast of my colours was checked using this contrast checker <a href="https://webaim.org/resources/contrastchecker/" target="_blank">Webaim</a>

- I changed the format of my images from jpg, png and jpeg to webp using <a href="https://convertio.co/png-webp/" target="_blank">convertio.</a>

### Media

- The default user image was obtained from <a href="https://www.pngwing.com/en/free-png-vyecs">Pngwing</a>, the uploader's name says "Non-commercial use, DMCA" - No user credited.

- The squad default image was obtained from <a href="http://www.arbitrosfutbolgalicia.com/pnfg/NPcd/NFG_Sel_WebSeleccion?cod_primaria=5001577&tipo_juego=5&cod_delegacion=100&cod_seleccion=2265328&carga_filtro=1">Aibitros</a>, no author has been credited.

- The image of Kevin De Bruyne was obtained from <a href="https://www.pngplay.com/image/494974">Pngplay</a>, the uploader's name is "Arsh".

- The image of Enzo Fernández was obtained from <a href="https://www.footyrenders.com/premier-league/chelsea/enzo-fernandez-2/">Footyrenders</a>, Cut by: "crisssnw".

- The image of Martin Ødegaard was obtained from <a href="https://www.footyrenders.com/premier-league/arsenal/martin-odegaard-45/">Footyrenders</a>, Cut by: JvierGfx.

- The image of Trent Alexander-Arnold was obtained from <a href="https://www.footyrenders.com/premier-league/liverpool/trent-alexander-arnold-72/">Footyrenders</a>, Cut by: crisssnw.

- The image of Aleksandar Mitrovic was obtained from <a href="https://www.footyrenders.com/nations/serbia/aleksandar-mitrovic-3/">Footyrenders</a>, Cut by: szwejzi.

- The image of Son Heung-min was obtained from <a href="https://www.footyrenders.com/premier-league/tottenham/son-heung-min-29/">Footyrenders</a>, Cut by: Lacen99.

- The rules one image was obtained from <a href="https://www.pexels.com/photo/action-activity-adult-athletes-262524/">Pexels</a>, posted by "Pixabay".

- The rules two image was obtained from <a href="https://pixabay.com/photos/soccer-ball-referee-sports-6679088/">Pixabay</a>, posted by "Planet_fox".

- The rules three image was obtained from <a href="https://pixabay.com/photos/sport-soccer-athlete-player-2177155/">Pixabay</a>, posted by "Keithjj".

- The background image was obtained from <a href="https://pixabay.com/photos/soccer-ball-sports-goal-kick-1678992/">pixabay</a>, posted by "seppH".

- The longer background image was obtained from <a href="https://pixabay.com/photos/stadium-soccer-santiago-grass-1525534/">Pixabay</a>, By "Voltamax".

- The Hele Cross Rangers image was obtained from <a href="https://pixabay.com/photos/people-soccer-players-athlete-1355497/">pixabay</a>, posted by "Ben_Kerckx".

- The Shiphay District image was obtained from <a href="https://www.mirror.co.uk/sport/football/news/best-sunday-league-side-ever-12566783">Mirror</a>, posted by "Image: Birmingham Mail WS".

- The Torre Town image was obtained from <a href="https://iamjimtaylor.com/posts/running-a-sunday-league-football-team/">I am Jim Taylor</a>, Posted by Jim Taylor on 28th March 2016.

- The Wellswood United image was obtained from <a href="http://www.lancssundayleague.co.uk/photo.php?action=news&pid=11487&title=Ashton%20on%20Ribble%20celebrate%2010%20years%20in%20the%20League">Lancssundayleague</a>, posted by "Ashton" on Ribble FC.

- The Barton Albion image was obtained from <a href="https://www.huffingtonpost.co.uk/entry/men-mental-health-sunday-league_uk_5c487879e4b025aa26beea8b">Huffingtonpost</a>, image of Enate United article By Rob Kazandjian.

- The winners image on the index page was obtained from <a href="https://www.nottinghampost.com/news/local-news/gallery/pictures-nottinghamshire-sunday-league-football-5689848">Nottinghampost</a>, By "Joe Rayner".

- The goalscorer image was obtained from <a href="https://pixabay.com/photos/soccer-football-athlete-player-1473669/">Pixabay</a>, By "Keithjj".

- The following country flags were obtained on [Flaticon]() with the author being "Freepik". They asked to be credited in their website and so I have placed a message on the live scores page.

- [World Flag](torquay_sunday_league/static/images/world.webp)
- [Europe Flag](torquay_sunday_league/static/images/europe.webp)
- [South America Flag](torquay_sunday_league/static/images/south-america.webp)
- [England Flag](torquay_sunday_league/static/images/england.webp)
- [Germany Flag](torquay_sunday_league/static/images/germany.webp)
- [France Flag](torquay_sunday_league/static/images/france.webp)
- [Italy Flag](torquay_sunday_league/static/images/italy.webp)
- [Spain Flag](torquay_sunday_league/static/images/spain.webp)
- [Portugal Flag](torquay_sunday_league/static/images/portugal.webp)
- [Brazil Flag](torquay_sunday_league/static/images/brazil.webp)
- [Netherlands Flag](torquay_sunday_league/static/images/netherlands.webp)

- The champions league logo was obtained from [pngwing](https://www.pngwing.com/en/free-png-nfain) with no author credited.

### Acknowledgements

- My Mentor Jubril Akolade for continuous helpful feedback.

- My college contact Ben Smith for his support throughout.

- My other college contact Pasquale Fasulo for his support too.

- Tutor support and the Slack community at Code Institute for their help.

This readme.md was spellchecked using the spell checker extension for Chrome.