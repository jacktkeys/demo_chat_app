# DEMO CHAT APP

## Data Storage

Data storage and retrieval is provided by Postgres. The data is structured in a relational pattern for easy access

1. Users
    1. ID - GUID 
        1. Automatically generated on insert
        1. Primary Key
    1. Username - VARCHAR(100)
        1. Unique constraint
1. Chatrooms
    1. ID - GUID
        1. Automatically generated on insert
        1. Primary Key
    1. Name - VARCHAR(200)
        1. Unique constraint
    1. Created By - GUID
        1. Foreign Key to Users ID
        1. On delete behavior is `set to null`
1. Messages
    1. ID - GUID
        1. Automatically generated on insert
        1. Primary Key
    1. Content - TEXT
        1. Actual text of the message
        1. TEXT data type used so there would be no limit on size of message
    1. Room ID - GUID
        1. Foreign Key to Chatroons ID
        1. On delete behavior is `cascade`
    1. Created By - GUID
        1. Foreign Key to Users ID
        1. On delete behavior is `casecade`
    1. Created Date - TIMESTAMP
        1. Datetime when the message was created
        1. Automatically set using `now()` function on insert
        1. An index is created on this column in descending order to speed up the `ORDER BY` query

## API

API uses the Flask framework to server requests

1. Flast-Restful
    1. Used to provide a restful interface into the API
    1. HTTP verbs are automatically mapped to functions of the same name
    1. Ability to easily pass parameters into functions
1. Blueprint
    1. Used for the ability to break the application in modules
    1. Easily maps routes into application code

## UI

UI is written using the ReactJS library

1. Login data is stored in LocalStorage
1. React state hook is used to trigger data loads and dynamic value changes

## Running the app

1. Each component is built and deployed in its own docker container
1. Docker-Compose is used to start and orchestrate all three containers
1. The Postgres container runs on the default port of `5432`
1. The API listens on port `4000`
1. The UI is served on port `3000`

## Learnings

1. There was an issue when using docker compose and trying to connect the API to `localhost`. The following URL describes pretty well what is going on and how to fix it.
- https://nayak.io/posts/docker-compose-postgres-and-connection-refused/
1. It took me a while to find a reference to the hook to use when the `Location` changes (URL path)
- https://9to5answer.com/detect-route-change-with-react-router