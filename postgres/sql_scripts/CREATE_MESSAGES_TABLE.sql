CREATE TABLE messages (
    id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    content TEXT,
    room_id uuid,
    created_by uuid,
    created_date timestamp NOT NULL DEFAULT now(),
    CONSTRAINT fk_room
        FOREIGN KEY(room_id)
            REFERENCES chatrooms(id)
            ON DELETE CASCADE,
    CONSTRAINT fk_user
        FOREIGN KEY(created_by)
            REFERENCES users(id)
            ON DELETE CASCADE
);