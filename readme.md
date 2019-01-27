### Simple SMS and MMS app with Twilio  

This app uses two APIs: one for a favourite quote and one for cat's images. The idea is: a Twilio phone number is connected with the app to send and receive SMS. If someone sends an SMS that says the word "Yes", then the app will reply with a phrase and a cat picture from the APIs. If the user says "No" it won't receive the phrase and picture, and if the user sends something else they'll be asked to respond "Yes" or "No".

For this app, you need to get a twilio account, and purchase a phone number. Then you need to programme that phone number to receive and respond to messages. You can use the twilio.com tutorials for doing so.

I wrote the app on flask, and run it locally then opened a tunnel with ngrok. I pasted the app's url with the /sms to my twilio phone number in the option webhook.

That's all! Please get in touch with questions, feedback or discussion.