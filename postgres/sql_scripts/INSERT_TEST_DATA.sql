WITH Y AS (
  INSERT INTO users (username)
  VALUES ('jacktkeys')
  RETURNING id as user_id
), x as (
  INSERT INTO chatrooms (name, created_by)
  SELECT 'Jax Room', user_id
  FROM Y
  RETURNING id as room_id
)
INSERT INTO messages (content, room_id, created_by)
SELECT 'Hello', room_id, user_id
FROM X, Y;

WITH Y AS (
  INSERT INTO users (username)
  VALUES ('extreme160')
  RETURNING id as user_id
), x as (
  INSERT INTO chatrooms (name, created_by)
  SELECT 'Extreme Room', user_id
  FROM Y
  RETURNING id as room_id
)
INSERT INTO messages (content, room_id, created_by)
SELECT 'Hello', room_id, user_id
FROM X, Y;

INSERT INTO messages (content, room_id, created_by) VALUES ('Hey', '3322d96b-69b9-4547-9e41-9609a1214202', 'bb309047-f98c-4a2e-8165-5ed3c42d2142');
INSERT INTO messages (content, room_id, created_by) VALUES ('Hey there', '40b3856e-5de3-44a5-b610-5b59bafb2e9d', 'bb309047-f98c-4a2e-8165-5ed3c42d2142');
INSERT INTO messages (content, room_id, created_by) VALUES ('Hey', '40b3856e-5de3-44a5-b610-5b59bafb2e9d', '43902064-1d7c-49c6-8c8d-18ee6237d208');
INSERT INTO messages (content, room_id, created_by) VALUES ('Hey there', '3322d96b-69b9-4547-9e41-9609a1214202', '43902064-1d7c-49c6-8c8d-18ee6237d208');