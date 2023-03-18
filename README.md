# FYP-Smart-Speaker

See requirements file for all installed packages.

## Building

To get the project working,

1. Using Docker navigate to /Docker from the project directory in the terminal
2. run the docker-compose.yml file using `docker-compose up`, this will start the caldav docker file.
3. Once running navigate to `http://localhost` to access the baikal setup.
    - Setup details however you like (user: admin, password: password) used for testing.
    - Navigate to users, create a user with a username and password.
    - Once set, in the `test.py` file when creating a calDav object (line 6) set the username and password to that set user, for the calendar link copy and paste it from the baikal user url.
    - Extra calendars do not need to be created as the caldav services uses the default ([0])
4. Run one of the commands in test.py after the connection (create event or event today f.e)
5. Profit

## Sources and Extra Reading

- <https://github.com/voice-engine/make-a-smart-speaker>
