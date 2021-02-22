# SMTPMailClient
##### It is a simple mail client that sends email to any recipient with SMTP protocol.
***
#### Features of SMTPMailClient
* Mail client establishes a TCP connection with a Google mail server.
* It dialogues with the mail server using the SMTP protocol.
* It sends an email message to a recipient via the Google mail server.
* It does not use `smtplib` which is a python module has built in methods to send mail using SMTP protocol.
***
#### Before Running
You have to change sender_mail_address, sender_mail_password and receiver_mail_address in the [SMTPMailClient.py](https://github.com/alihaydarkurban/Socket-Programming/blob/main/SMTPMailClient/SMTPMailClient.py) with yours.
```
sender_mail_address = 'sender_mail@example.com'
sender_mail_password = '**********'
receiver_mail_address = 'receiver_mail@example.com'
```
If your gmail account disable to less secure application you may need to enable "Access for less secure apps" in your gmail settings.<br/>
Following operations are for that:<br/>
1) Login into your Gmail account then go to [here](https://www.google.com/settings/security/lesssecureapps)
2) Select Turn On for Access for less secure apps.
***
#### Running
Open your terminal, go to the same path with the file and enter this:
```
py -2 SMTPMailClient.py
```
***
#### Test Results
You can see the test results [here](https://github.com/alihaydarkurban/Socket-Programming/blob/main/SMTPMailClient/TestResultsOfSMTPMailClient.pdf).
***
