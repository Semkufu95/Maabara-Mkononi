CREATE TABLE test_bookings (
   id INT AUTO_INCREMENT PRIMARY KEY,
   user_id INT,
   test_type VARCHAR(100),
   date DATE,
   FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE test_results (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    test_type VARCHAR(100),
    result VARCHAR(255),
    result_date DATE,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
