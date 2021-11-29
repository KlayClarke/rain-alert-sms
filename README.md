# rain-alert-sms

Rain alert that uses weather api to recieve predictive weather information and twilio.rest to send sms when the forecast predicts showers within the next 12-hours.

The code worked once, sending me an sms stating that (for testing purposes) in Zurich, Switzerland it would be raining soon. After attempting to run the code again, I was met with a few errors. After trying to resolve these errors on the Twilio site, it seems that none of the solutions work for me - if I solve the authentication error, I am hit with an HTTPS error. Once I find a work around to the latter, I am hit with a key error, and so on. 

Luckily, I know that the code was sufficient because it sent a successful sms at first.
