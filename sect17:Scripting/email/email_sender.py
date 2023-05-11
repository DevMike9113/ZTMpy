# hupembokeyjczuws

import smtplib
from email.message import EmailMessage
from pathlib import Path
from string import Template

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Mike Skin'
email['to'] = 'micheal.skinner@gmail.com'
email['subject'] = 'You won billions'

email.set_content(html.substitute({'name': 'Butthole'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('micheal.skinner@gmail.com', 'hupembokeyjczuws')
    smtp.send_message(email)
    print('yo peep')
