import imaplib
import email

imap_server = "imap.gmail.com"
email_address = "tester2022testy@gmail.com"
password = ""

imap = imaplib.IMAP4_SSL(imap_server)
imap.login(email_address, password)

imap.select("Inbox")

_, msgnums = imap.search(None, "ALL")

for msgnum in msgnums[0].split():
    _, data = imap.fetch(msgnum, "(RFC822)")

    message = email.message_from_bytes(data[0][1])


    headline = message.get('From')

    result = headline.find('@gmail.com')
    if result >= 0:
        print(headline)

imap.close()