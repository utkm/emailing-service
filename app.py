from csv import reader
from smtplib import SMTP
from jinja2 import Template
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime as dt
import time
import ssl

# Your email
my_email = ""

# Enter your mail app password (requires 2-Factor Authentication to be enabled) 
app_pswd = ""

# If you would like to cc anyone, you can add their emails in the following list
#cc = [""]

# Enter the message subject
message_subject = "(Test) Personalized Mass Emailing Service"

# Start the server
server = SMTP("smtp.gmail.com", 587)
server.starttls()
server.ehlo()
server.login(my_email, app_pswd)

# The sendmail function
def sendmail(first_name, email_addr, cnt):
    first_name = first_name.capitalize()

    # Write up the email. First open the template html file
    html_string = open("template.html", "r", encoding="utf-8").read()
    my_templ = Template(html_string)

    # Write the name of the recipient in the {{ username }} area
    with open("message.html", "w", encoding="utf-8") as copy:
        copy.write(my_templ.render(first_name=first_name))

    # MIMEText() object contains HTML version and error message version.
    # The MIMEMultipart("alternative") combines them into a single message
    # with 2 rendering options. The email client will try to render the last part first
    backup = "Error. Sorry, we'll get back to you soon!"
    p1 = MIMEText(backup, "plain")
    fmsg = open("message.html", "r", encoding="utf-8").read()
    p2 = MIMEText(fmsg, "html")

    # Parameters of the email
    message = MIMEMultipart("alternative") 
    message.attach(p1)
    message.attach(p2)
    message["Subject"] = message_subject
    message["From"] = my_email
    message["To"] = email_addr

    # Send Email
    # server = SMTP("localhost")

    # recipients = [email_addr] + cc
    # server.sendmail(my_email, recipients, message.as_string())
    server.send_message(message)
 
    print("Email sent to " + first_name + ". [Total: " + str(cnt+1) + "]")


def main():
    start_time = time.time()
    # Open the CSV and parse the desire parameters
    with open("trial.csv", "r") as csvfile:
        csv_reader = reader(csvfile)
        next(csv_reader)
        i = 0
        for row in csv_reader:
            # This value indicates the number of emails (rows) to be sent
            if (i <= 101):
                first_name = row[0].strip()
                email_addr = row[1].strip()
                # print(first_name + " " + email_addr + " " + str(i))
                sendmail(first_name, email_addr, i)
                # track number of seconds taken
                print("---- %s seconds ----" % (time.time() - start_time))
                i += 1
        server.quit()

if __name__ == "__main__":
    main()