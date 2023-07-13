# Simple_Website_Watchdog
A simple watchdog which will monitor the website, and send email to notify if the website cannot return code 200, 301 or 302

## How to use:
Put this script in either folder, edit the follow lines for email notify:
```
//Ensure your SMTP server's port is 587, is not, just change it
server = smtplib.SMTP('YOUR_SMTP_SERVER_HERE', 587)
```
&
```
server.login('SMTP_LOGIN_ID', 'SMTP_LOGIN_PASSWORD')
```
&
```
sender_email = 'SENDER_EMAIL_ADDRESS'
```

After that, create a text file called "sitelist.txt", and input the website link you want to test, with full domain name seperate in new lines, for example:
```
https://www.google.com
https://www.yahoo.com
```

Then create a text file called "email.txt", and input the website link you want to test, with full domain name seperate in new lines, for example:
```
abc@mail.com
def@mail.com
```

After all this is done, just run it as a cron job or task scheduler in your need.
