## Track a DHL package with Python
# Python file that looks up the DHL delivery status for a package and 
# sends out an email with the latest status

import requests
import json
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

TRACKING_CODE = 'Tracking_Number_Goes_Here'
AWB_NO = 'Airway_Bill_Number_Goes_Here'

# Create a sendgrid account(free) to be able to send emails.
# Add the API KEY into the next variable as a string value
SENDGRID_KEY = 'SendGrid_API_KEY_Goes_Here'

res = requests.get('https://www.dhl.com/shipmentTracking?AWB={0}&countryCode=g0&languageCode=en&_='.format(TRACKING_CODE))
obj = json.loads(res.content)
latest_cp = obj['results'][0]['checkpoints'][0]

print(latest_cp['description'])

# Figure whats the latest counter number in the original tracking URL
# TODO: Modify this dynamically
if int(latest_cp['counter']) > 19:
    message = Mail(
        from_email='from@email.com',
        to_emails='to@email.com',
        subject='Delivery Status',
        html_content='<strong>{0}</strong>'.format(latest_cp['description'])
    )
        
    try:
        sg = SendGridAPIClient(SENDGRID_KEY)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)
