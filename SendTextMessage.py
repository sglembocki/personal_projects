from twilio.rest import TwilioRestClient

#change values here

account_sid = ''
auth_token = ''
twilio_number = '+xxxxxxxxxxx'
my_number = '+xxxxxxxxxxx'

#send message

twilio_client = TwilioRestClient(account_sid, auth_token)
twilio_client.messages.create(body = 'hello world', from_ = twilio_number, to = my_number)