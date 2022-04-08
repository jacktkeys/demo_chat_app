CREATE TABLE chatrooms (
    id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    name varchar(200),
    created_by uuid,
    CONSTRAINT unique_roomname UNIQUE(name),
    CONSTRAINT fk_user
        FOREIGN KEY(created_by)
            REFERENCES users(id)
            ON DELETE SET NULL
);