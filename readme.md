# NHS Tutoring Management Tool: Specs


## Given description

People can log in with their email addresses and a password.

User entities have the following data:
-   Name
-   Date of graduation (will be useful for clearing people out of the system when they graduate)

Users can:
-   Sign up for tutoring dates
    -   Check boxes for subject preference and classes taken
-   Cancel a tutoring sign-up
-   Check which dates they’re signed up for
-   Check which tutoring sessions they showed up to in the past
-   Check how many tutoring hours they have accumulated

Each date will display how many slots are left, e.g. “January 17 (3 slots available)”.
Users cannot see which other users are signed up for each date.
A date will close once all slots are filled.

Admins can:
-   Access a list of people signed up for each date
-   Check people off for attendance at tutoring sessions
-   Edit user data and remove them from the system


## Database tables

Student

Column name             Datatype
--------------------    --------
USER ID                 primary
email/username          str
name                    str
password hash           str
graduation year         date obj; year only


Subjects

Column name             Datatype
--------------------    --------
SUBJECT ID              primary
name                    str
category                str; must be "humanities" or "math/science"


Preferred subjects

Column name             Datatype
--------------------    --------
user id                 USER ID
subject id              SUBJECT ID


Tutoring session

Column name             Datatype
--------------------    --------
SESSION ID              primary
date                    date obj
start time              time obj
spots available         int
category                str; must be "humanities" or "math/science"
description             str
location                str


Attendance list

Column name             Datatype
--------------------    --------
ATTENDANCE ID           primary
user id                 int
date registered         date obj
present                 bool
verified by             ADMIN ID


Admin

Column name             Datatype
--------------------    --------
ADMIN ID                primary
email/username          str
name                    str
password hash           str



## Privileges and views

### Student

-   Core
    -   Sign up for any session within current day + 4 weeks
    -   Cancel for any session
    -   Set and update subject preferences
-   Views
    -   View sessions they've signed up for
    -   View waitlisted sessions
    -   View past sessions
    -   View total hours accumulated
-   Convenient
    -   Change email/username
    -   Change password

### Admin

-   Core
    -   Create, delete, or modify tutoring dates
    -   Be able to check off and verify users who attend tutoring sessions
    -   Delete, modify, or add arbitrary users
    -   Ban users from further registering sessions
-   Views
    -   View all users who have less then required number of 
        tutoring hours at any time.
    -   View students who have an abnormally high number of tutoring hours
    -   View all students who will be attending a given tutoring session
    -   View all students who is on the waitlist for a given tutoring session
    -   Export/view all data
-   Convenient
    -   Change email/username
    -   Change password


## Order of implementation:

-   Setup basic webapp to test Google App Engine
-   Enable feature to push code directly from github to online, if possible
-   Setup a basic set of test tables
-   Setup a basic authentication system for students and admins
-   Architect and construct a very basic backend. 
    Add stubs for all needed behaviors.
-   Add the database, and add a way to populate basic data.
-   Construct a very basic, ugly backend. Stub out all expected behaviors
-   Test all interactions
-   Reskin using Bootstrap




