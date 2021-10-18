# Dream11 Leaderboard

[Dream11](https://www.dream11.com/) is a fantasy sports platform based in India that allows users to play fantasy cricket, hockey, football, kabaddi and basketball.
The platform has gained immense popularity with millions of users particpating in contests daily, especially during the **IPL Season**. Everyone claims to be the biggest fan of their team, but there is no way that can be quantified. However, your tactics for the match of your team and analysis of the opppostion team surely tells a lot about how much you are into the game. One match victory can be called off as a fluke. So, here's the solution to judge your performance for the matches your favourite team played accross the entire season.  

Dream11 site requires us to **login** to our contest inorder to view these details, through our **registered mobile number** and **OTP**.
So, for scraping these details multiple times in between the match requires us to login every time. As authorization is done using OTP, 
this task will be very annoying. So we need to persist our login session through cookies. So, first run the script [login.py]
and login as you normally do. This script will grab and export the cookie into a text file (*cookie.txt*).

For every match you want to consider the results for, add the leaderboard link to the file [matchLinks.txt], and all the usernames of the particpants to an excel file under the header `Usernames`. Make the required changes to the [scrapper.py] i.e. adding the file name and sheet name. Also, adjust the sleep time as per your internet speed inorder to ensure smooth scrapping. Now run the script [scrapper.py]which loads the cookie from **cookie.txt**, inorder to bypass the login process. Give it a few time to scrap the necessary details from the site. You can view the entire automation happening in your web browser. After all the leaderboards are scrapped, you can view your performace for each team under their respective sheets. 

- **:timer_clock: Scraping time depends on the numbers of players participating in the contest.**
- **:warning: Do not tamper with the site elements while script is running.**

## Requirements :
  - **Selenium**  :point_right: [(Read DOC)](https://selenium-python.readthedocs.io/)
      * Run the command ``` pip install selenium ``` on your terminal :computer: to install the library.
  - **BS4**  :point_right: [(Read DOC)](https://beautiful-soup-4.readthedocs.io/en/latest/)
      * Run the command ``` pip install bs4 ``` on your terminal :computer: to install the library.
  
  - I have used Google Chrome browser for opening the web page.
      * Web driver for chrome can be downloaded from :paperclip: http://chromedriver.chromium.org/downloads
  - Extract the downloaded folder and copy **chromedriver** to :file_folder: **/usr/bin/**

---
