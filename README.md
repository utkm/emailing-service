# Personalized Mass Emailing Service

Sending out numerous emails can get tedious, especially if they have to be personalized. This situation led me to think about ways I can automate this process myself other than using existing mailing software. My knowledge of automative tools in Python was a solid start, but I learned a lot about templating and dealing with high volume requirements while building this script. This personalized mass emailing service is a secure and robust tool and has been used by my team members at STEM Fellowship to send over 500 emails to date!

## How it works
To get started, you must...
1. Enter your email and app password corresponding to the email service which you can find in your Google account. 
2. Set up a two-column database. The first column is the name, and the second is their email.
3. Run the program!

After this, the script will automatically process and log the requests in the console including the elapsed time at each sent email. It reads the template from the `template.html` file, and writes to the `message.html` file based on the information from the database using Jinja templating. The script will re-write to the `message.html` file for every row in the database and send emails every iteration. 

If you have any questions/concerns/suggestions, feel free to get in touch!
