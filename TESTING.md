# Testing

Below is a list of test that have been carried out with screenshots.

## Browser Compatibility

The below browsers have been tested with the deployed site.

__Google Chrome__

![Google Chrome](documentation/testing/fullscreen-google-chrome.jpg)

__Microsoft Edge__

![Microsoft Edge](documentation/testing/microsoft-edge.jpg)

__Firefox__

![Firefox](documentation/testing/firefox.jpg)

__Samsung Internet App__

![Samsung App](documentation/testing/samsung.jpg)

__Apple Safari App__

![Safari App](documentation/testing/safari.png)

## Responsiveness

Below are the test that I have run with regards to responsiveness.

__1920x1080__

![1920X1080](documentation/testing/1920x1080.jpg)

__1280x850__

![1280x850](documentation/testing/1280x850.JPG)

__1024x840__

![1024x840](documentation/testing/1024x840.j%5Bg.JPG)

__768x1024__

![768x1024](documentation/testing/768x1024.jpg)

__600x960__

![600x960](documentation/testing/600x960.jpg)

__412x869__

![412x869](documentation/testing/412x869.jpg)

__375x812__

![375x812](documentation/testing/375x812.jpg)

## Code Validation
__Code Validation__

__HTML__

No errors were returned when passing through the official W3C Validation

- [W3C validator - Index](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fcadiusforum.herokuapp.com%2F#l134c20)

![Index Screenshot](documentation/testing/index-validation.jpg)
- [W3C validator - Category Detail](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fcadiusforum.herokuapp.com%2Freplys%2Fcategory%2F2%2F#l134c20)

![Category Detail Screenshot](documentation/testing/category-detail-validation.jpg)
- [W3C validator - Topic Detail](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fcadiusforum.herokuapp.com%2Freplys%2Fcategory%2F2%2Ftopic%2F1%2F)

![Topic Detail Screenshot](documentation/testing/topic-detail-validation.jpg)
- [W3C validator - Login](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fcadiusforum.herokuapp.com%2Faccounts%2Flogin%2F)

![Login Screenshot](documentation/testing/signin-validation.jpg)
- [W3C validator - signup](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fcadiusforum.herokuapp.com%2Faccounts%2Fsignup%2F)

![Signup Screenshot](documentation/testing/signup-validation.jpg)
- [W3C validator - Signout](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fcadiusforum.herokuapp.com%2Faccounts%2Flogout%2F)

![Signout Screenshot](documentation/testing/signout-validation.jpg)

__CSS__

No errors were returned when passing through the official W3C Validation

- W3C validator - CSS file

![CSS Screenshot](documentation/testing/css-validation.jpg)

__Python__

No errors were returned when passing throught the offical PEP8 Validation

__Cadiusforum Project Files__

- Settings.py

![Settings.py](documentation/testing/project-settings-validator.jpg)
- urls.py

![urls.py](documentation/testing/project-url-validation.jpg)

__Category App__

- admin.py

![admin.py](documentation/testing/category-admin-validation.jpg)
- models.py

![models.py](documentation/testing/category-model-validation.jpg)
- views.py

![views.py](documentation/testing/category-views-validation.jpg)

__Topic App__

- admin.py

![admin.py](documentation/testing/topic-admin-validation.jpg)
- forms.py

![forms.py](documentation/testing/topic-forms-validation.jpg)
- models.py

![models.py](documentation/testing/topic-models-validation.jpg)
- urls.py

![urls.py](documentation/testing/topic-urls-validation.jpg)
- views.py

![views.py](documentation/testing/topic-views-validation.jpg)

__Reply App__

- admin.py

![admin.py](documentation/testing/reply-admin-validation.jpg)
- forms.py

![forms.py](documentation/testing/reply-forms-validation.jpg)
- models.py

![models.py](documentation/testing/reply-models-validation.jpg)
- urls.py

![urls.py](documentation/testing/reply-urls-validation.jpg)
- views.py

![views.py](documentation/testing/reply-views-validation.jpg)

## User Story Tests
- As a User I can Create new topics so that I can get other peoples help or opinions

![Create Topic](documentation/testing/new-topic.jpg)
- As a User I can edit my own topics or replys so that I can correct mistakes

![Create Topic](documentation/testing/edit-topic.jpg)
![Edit Reply](documentation/testing/edit-reply.jpg)
- As a User I can delete any of my topics so that I can manage my own entries

![Delete Topic](documentation/testing/delete-topic.jpg)
- As a User I can create replys to topics so that I can be involved in the conversation

![New Reply](documentation/testing/new-reply.jpg)
- As a Site Admin I can create, edit and delete topics / replys so that I can manage any bad behaviour

![Admin Site](documentation/testing/admin.jpg)
- As a User I can view Categories and Topics so that I can select what I want to read

![View Category](documentation/testing/category-view.jpg)
![Veiw Topics](documentation/testing/topic-view.jpg)
- As a User I can register and account so that I can create Topics / replys

![Sign up](documentation/testing/sign-up.jpg)

## Fixed Bugs
During development, I ran into some bugs, errors, and issues which I have successfully debugged and troubleshot.

You can find them on the issues tracker on the repository. [Here](https://github.com/robcole-dev/cadius-forum/issues?q=is%3Aissue+is%3Aclosed)

- Bug Report: Unable to view Topic detail (Issue [#10](https://github.com/robcole-dev/cadius-forum/issues/10))
- Bug Report: Template Syntax Error (Issue [#11](https://github.com/robcole-dev/cadius-forum/issues/11))
- Bug Report: Edit not loading on deployed site (Issue [#12](https://github.com/robcole-dev/cadius-forum/issues/12))
- Bug Report: Warning on Editor (Issue [#13](https://github.com/robcole-dev/cadius-forum/issues/13))
- Bug report: Footer blocks content (Issue [#14](https://github.com/robcole-dev/cadius-forum/issues/14))
- Bug report: Background image not displayed (Issue [#15](https://github.com/robcole-dev/cadius-forum/issues/15))
- Bug Report: Unable to view Topic detail (Issue [#16](https://github.com/robcole-dev/cadius-forum/issues/16))

![Closed Tickets](documentation/testing/closed-tickets.jpg)

## Unfixed Bugs

Currently there is 1 issue outstanding

- Bug Report: Error in console (Issue [#9](https://github.com/robcole-dev/cadius-forum/issues/9))

![Open Tickets](documentation/testing/open-tickets.jpg)