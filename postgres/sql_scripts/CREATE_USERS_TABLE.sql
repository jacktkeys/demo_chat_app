CREATE TABLE users (
    id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    username varchar(100),
    CONSTRAINT unique_username UNIQUE(username)
);