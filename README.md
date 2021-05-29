GIT HUB Branch Protection using Python
-----------------------------------------
![GitHub Pipenv locked Python version](https://img.shields.io/github/pipenv/locked/python-version/RahulMR42/GITHub-Branch-Protector) ![GitHub Pipenv locked dependency version](https://img.shields.io/github/pipenv/locked/dependency-version/RahulMR42/GITHub-Branch-Protector/fastapi)

A pythonic webservices to react based on GIT HUB Organizational events and add protection rule to GIT HUB Branches.Once done update the user via an issue and notified with '@' tagging.


:white_check_mark: Python 3 :white_check_mark: FAST API :white_check_mark:GITHub Webhook :white_check_mark:Uvicorn

:eight_spoked_asterisk: Objective:

- A pythonic way to act based on [GIT HUB webhook events](https://docs.github.com/en/developers/webhooks-and-events/webhooks/about-webhooks#events) and add GitHub [branch protection rules](https://docs.github.com/en/rest/reference/repos#update-branch-protection).
- Powerfull lightweight and scalable api using [FAST API](https://fastapi.tiangolo.com/).
- Create an issue and notify the user with '@' tagging by leaveraging [GIT HUB APIs](https://docs.github.com/en/rest/reference/issues#create-an-issue).
- It also provide a scalable asynchronous gatway interface powered to expose the api using [Uvicorn.](https://www.uvicorn.org/)
  

:eight_spoked_asterisk: Quick Install & Refer [Wiki](https://github.com/RahulMR42/GITHub-Branch-Protector/wiki) for deep dive:
* We will be leveraging Ngork to intercept the github events.
* Install [Ngork](https://ngrok.com/) to your host.
* Run Ngork on your machine.
  ```
  ngrok.exe http 8000 
  ```
* Make a note of http forwarding link from the ngork output.
  ```
  Example:  http://a97c37bd61ee.ngrok.io
  ```
* Create Git HUB Webhook for your GIT HUB organization,with payload as **http://(ngrok forwarding url)/repoevent**.
```
Exmaple of payload: http://137be156ccd0.ngrok.io/repoevent
```
* Clone the repo.
  ```
  $ git clone https://github.com/RahulMR42/GITHub-Branch-Protector
  ```
* Install python pipenv and dependecies.
  ```
    $ cd GITHub-Branch-Protector
    $ pip install pipenv
    $ pipenv sync -d .
     ```
* Set below OS variables to authorize to the Git HUB repo .
```
    git_user : (Git Hub User name )
    git_pat  : (Git Hub Personal Access Token)
```
* Run the application 
```
pipenv run uvicorn app:app --reload
```
* Create a new repo in the concerned Git Hub organization with at least one file (Example `README.md`or `.gitignore`) at the time of creation.

* The ngrok will pick up the event and using the api it will add a protection rule and a new issue will be added and notified to the user.

* Refer our [wiki page](https://github.com/RahulMR42/GITHub-Branch-Protector/wiki) to know in details and add customizations in the protection rules.


:eight_spoked_asterisk: Technical Deep Dive:

- Refer [wiki](https://github.com/RahulMR42/GITHub-Branch-Protector/wiki) for more informations.

:eight_spoked_asterisk: Objective: Enhancements 

- The code can be enhanced for any other GIT HUB Webhook events.
- The code can be enhanced /scaled with https and for othe type of webhook listerns as well .


  
