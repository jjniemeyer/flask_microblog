# Flask Microblog

This project is for getting an understanding of the structure of a flask app.
The code is from the [Flask Mega Tutorial](http://blog.miguelgirnberg.com)
I will likely customize this app a little but I'm primarily keeping it around for reference and practice with containerization and deployment.


## Environment Variables for Email server

The following environment variable need to be set in order to send emails from the app.

### Gmail
In order to use a gmail account as an email server we need to explicitly allow "less secure apps" access to the gmail account.

```
(venv) $ export MAIL_SERVER=smtp.googlemail.com
(venv) $ export MAIL_PORT=587
(venv) $ export MAIL_USE_TLS=1
(venv) $ export MAIL_USERNAME=<your-gmail-username>
(venv) $ export MAIL_PASSWORD=<your-gmail-password>
```

## Docker

The tutorial says to run the container like this:
```
docker run --name microblog -d -p 8000:5000 --rm microblog:latest
```
However, according the man page for docker run: `--rm` 
is incompatible with detached mode `-d`. 
In order to get the container running I'm using:
```
docker run --name microblog -d -p 8000:5000 microblog:latest
```