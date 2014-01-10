Reddit-To-Twitter-Bot
=====================

Grabs posts from a subreddit and posts them to Twitter using the Twitter API.
Developed by JC300 using Python.


Please feel free to let me know what you think!  (Or if you find
bugs!)

**DISCLAIMER:** Wouldn't have made this without help from some friends.

Wanna send some DOGE my way? :)  DQhtQFgS2gtE1WtvtNeBUyFCoaJ8zMPniS

#### How to Install/Run

If you wish to edit the subreddit you wish to grab posts from, edit the reddit_bot.py with a text editor and find the 'setup_connection_reddit('dogecoinscamwatch') string and edit the 'dogecoinscamwatch' to any subreddit you want.

To change the hot/new/rising/controversial setting, find the 'for submission in subreddit_info.get_new' string and edit 'new' to either of these:

hot

rising

controversial

top

gilded

##First, download the .zip or clone the package using GitHub desktop.

When opening and extracting, you should find these files:

'reddit_bot.py'

'posted_posts.txt'

'/docs'



reddit_bot.py - this is what you will be running.

posted_posts.txt - this is to keep a log of what goo.gl/[insert post url here] url's are posted to Twitter

/docs - Documentation


##Edit the reddit_bot.py file and look for:

'access_token'

'access_token_secret'

'consumer_key'

'consumer_secret'


##Then, go to http://dev.twitter.com (assuming you already made a Twitter account for your bot) and enter your Twitter (bot)'s credentials. 

It should show a page with a 'create application' button on it. If there is not, simply press the dropdown menu at the end of the navbar, and press 'View Applications'.

After this, create an application, and call it whatever you wish. Then create an access token and copy that into the reddit_bot.py file, the same with the access token secret, consumer key, etc.

Then save it.


##After that, on Windows, simply run the .py and it should show up and do it automatically.

Considering if you have Mac or Linux, open up Terminal and type:
'python reddit_bot.py' (you must have it in your home folder)

Feel free to get in touch with me if you have any issues!

