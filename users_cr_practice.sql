SELECT * FROM users;

INSERT INTO users (first_name, last_name, email)
VALUES ('Ang', 'Avatar', 'avatar1000@gmail.com'), ('Toph', 'Beifong', 'blindsight@gmail.com'), ('Sokka', 'Water', 'boomerangguy@gmail.com'), ('Appa', 'Arrow', 'flyingfloof@gmail.com'), ('Katara', 'Water', 'waterheals@gmail.com');


UPDATE users
SET first_name = 'Zuko', email = 'redisbetterthanblue@gmail.com'
WHERE id = 6;