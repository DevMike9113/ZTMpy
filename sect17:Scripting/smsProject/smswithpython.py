from twilio.rest import Client

account_sid = 'AC012ba88b032f986b31b09817ac191fff'
auth_token = '87c393b3539225262f8feb4e2135a721'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+18339660380',
    body='Too much to do.',
    to='+18139575911'
)

print(message.sid)
