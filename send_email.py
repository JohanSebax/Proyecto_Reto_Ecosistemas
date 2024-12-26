import smtplib
from email.message import EmailMessage
import os

def send_email_with_attachment(sender_email, recipient_email, subject, body, attachment_path):
    """
    Sends an email with the specified attachment.

    Args:
        sender_email (str): The sender's email address.
        recipient_email (str): The recipient's email address.
        subject (str): The subject of the email.
        body (str): The body text of the email.
        attachment_path (str): The file path to the attachment.
    """
    # SMTP server configuration
    smtp_server = 'smtp.office365.com'
    smtp_port = 587  # Use 465 for SSL connections
    smtp_username = ' ' # Input your username to test it
    smtp_password = ' ' # Input your password to test it

    # Create the email message
    msg = EmailMessage()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.set_content(body)

    # Attach the Excel file
    try:
        with open(attachment_path, 'rb') as f:
            file_data = f.read()
            file_name = os.path.basename(attachment_path)
        msg.add_attachment(file_data, maintype='application',
                           subtype='vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                           filename=file_name)
    except FileNotFoundError:
        print(f"Attachment file {attachment_path} not found.")
        return
    except Exception as e:
        print(f"Error attaching file: {e}")
        return

    # Send the email
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection
            server.login(smtp_username, smtp_password)
            server.send_message(msg)
        print(f"Email sent successfully to {recipient_email}")
    except smtplib.SMTPException as e:
        print(f"SMTP error occurred: {e}")
    except Exception as ex:
        print(f"An error occurred: {ex}")