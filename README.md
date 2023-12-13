The file is for a basic understanding of what this project will entail and how it will work. 

Step 1: The script will start the process by logging into Mobile Link by sending the login credentials in a format that will mimic what a
browser would send if it were to be done manually. 

After that, the script uses a session object from the requests library. This session object maintains a consistent session across multiple requests - 
it keeps track of cookies and other HTTP headers required for maintaining a logged-in state.

Step 2: Once logged in, the script will be able to access the pages that are only available to users, and it will make requests to these pages 
within the same session. 

The script will then parse through the HTML data using BeautifulSoup and will extract the necessary data

Step 3: The script will organize the data into the format that Bigin needs. The script will use the APIs to update. 

Step 4: This entire process above can be automated and set to run at regular intervals, we would have to use a task scheduler in order to make this happen. 
We need to make sure that the script has robust error handling and reporting in case someone can't be updated, network errors, login failures, or changes
to the Mobile Link's website. 
# MLScraperNew
