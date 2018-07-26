# MessageMedia Enterprise WebHooks Python Code Guide
[![Pull Requests Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat)](http://makeapullrequest.com)

The MessageMedia Enterprise WebHooks code guide demonstrates how you can verify WebHooks signed and sent to you by MessageMedia.

![Isometric](http://i64.tinypic.com/2aalw86.jpg)

## Table of Contents
* [Information](#newspaper-information)
  * [Slack and Mailing List](#slack-and-mailing-list)
  * [Bug Reports](#bug-reports)
  * [Contributing](#contributing)
* [Prerequisite](#star-prerequisite)
* [Get Started](#clapper-get-started)
* [API Documentation](#closed_book-api-documentation)
* [Need help?](#confused-need-help)
* [License](#page_with_curl-license)

## :newspaper: Information

#### Slack and Mailing List

If you have any questions, comments, or concerns, please join our Slack channel:
https://developers.messagemedia.com/collaborate/slack/

Alternatively you can email us at:
developers@messagemedia.com

#### Bug reports

If you discover a problem with the code guide, we would like to know about it. You can raise an [issue](https://github.com/messagemedia/enterprise-webhooks-python-sdk/issues) or send an email to: developers@messagemedia.com

#### Contributing

We welcome your thoughts on how we could best provide you with SDKs that would simplify how you consume our services in your application. You can fork and create pull requests for any features you would like to see or raise an [issue](https://github.com/messagemedia/enterprise-webhooks-python-sdk/issues)

## :star: Prerequisite
To be able to use this SDK, you will need a public key provided by MessageMedia. You can find out how to do this by going through the [Signature Key Management documentation](https://developers.messagemedia.com/code/signature-key-management-api-documentation/). You can then make use of the [Signature Key Management Python SDK](https://github.com/messagemedia/signingkeys-python-sdk) to create and manage your keys.

This SDK assumes that you have pre-configured a WebHook that sends data to a url. If you haven't done this, you can read about how to set one up in the [WebHooks API Documentation](https://developers.messagemedia.com/code/webhooks-api-documentation/) or the [WebHooks Python SDK](https://github.com/messagemedia/webhooks-python-sdk). Alternatively, you can specify a callback_url in the message body of a [send message request](https://github.com/messagemedia/messages-python-sdk#send-an-sms).

## :clapper: Get Started
To keep this guide simple and easy to understand, we've used BaseHTTPServer to set up a server which will monitor for incoming WebHooks. You can setup your own production server and use it instead of the BaseHTTPServer one if needed.

### Initialisation and Installation
Create an empty directory for your project, let’s name it “testApp”. Now, open up your command prompt and clone this repository into the directory created.

### Adding in the public key
Create a file for your public key and set the `PUB_KEY_PATH` to the path for the file containing your public key.

### Testing
You are now ready to test the application. Run the web server on your computer that has PHP installed and configured.
If all goes well, you should receive a JSON response with an object that contains a `verified` property. This property indicates if the verification was a success.

## :closed_book: API Reference Documentation
Check out the [full API documentation](https://developers.messagemedia.com/code/secure-webhooks-api-documentation/) for more detailed information.

## :confused: Need help?
Please contact developer support at developers@messagemedia.com or check out the developer portal at [developers.messagemedia.com](https://developers.messagemedia.com/)

## :page_with_curl: License
Apache License. See the [LICENSE](LICENSE) file.
