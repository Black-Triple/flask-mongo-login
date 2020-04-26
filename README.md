# flask-mongo-login
Login APIs using MongoDB and Flask

## Getting Started
- Modify the DB name in config.py located inside server which you are going to use/connect
- Modify the DB connection URI as well, make sure MongoDB server is running on specified port
- Change the configuration for Development or Production by setting:
  ```sh
  $ export APP_SETTINGS="server.config.DevelopmentConfig"
  ```
- Set a secret key
  ```sh
  $ export SECRET_KEY="change_me"
  ```
  
### Create Schema
- Execute following to create the DB schema
  ```sh
  $ python triplespades.py create_db
  ```

### Run the Application
```sh
$ python triplespades.py runserver
```

Access the application at the address [http://localhost:5000/](http://localhost:5000/)
