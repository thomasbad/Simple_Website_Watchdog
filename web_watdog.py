import requests
import smtplib

# Read URLs from sitelist.txt
with open('sitelist.txt', 'r') as file:
    urls = file.read().splitlines()

# Read email addresses from email.txt
with open('email.txt', 'r') as file:
    email_addresses = file.read().splitlines()

down_websites = []

# Check website status
for url in urls:
    try:
        response = requests.get(url)
        if response.status_code != 200:
            down_websites.append(url)
    except requests.exceptions.RequestException:
        down_websites.append(url)

# Send email notifications for down websites
if down_websites:
    message = f"The following websites are down:\n\n"
    message += "\n".join(down_websites)

    # Connect to SMTP server
    server = smtplib.SMTP('your_smtp_server', 587)

    # Start TLS encryption
    server.starttls()

    # Login to SMTP server
    server.login('your_username', 'your_password')

    # Send email
    sender_email = 'your_email_address'
    subject = 'Website Down Notification'
    body = f'Subject: {subject}\n\n{message}'
    for receiver_email in email_addresses:
        server.sendmail(sender_email, receiver_email, body)

    # Close the connection
    server.quit()
