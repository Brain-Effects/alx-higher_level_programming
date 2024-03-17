-- This script lists all privileges of the MySQL users user_0d_1 and user_0d_2

-- Connect to the MySQL server as the root user
-- mysql -u root -p'password'

-- List all global privileges for user_0d_1
SELECT * FROM mysql.user WHERE User='user_0d_1';

-- List all global privileges for user_0d_2
SELECT * FROM mysql.user WHERE User='user_0d_2';

-- List all database-specific privileges for user_0d_1
SELECT * FROM mysql.db WHERE User='user_0d_1';

-- List all database-specific privileges for user_0d_2
SELECT * FROM mysql.db WHERE User='user_0d_2';
