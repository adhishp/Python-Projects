from twilio.rest import TwilioRestClient

# Find these values at https://twilio.com/user/account
account_sid = "AC020d66ccd8e3f1e45f13880614cb74a6"
auth_token = "586c3ae07404759f07f4d7ed6cf98244"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(to="+16465988889", from_="+16507535939",
                                     body="Hi Aryan! Why are you so AWESOME?")
