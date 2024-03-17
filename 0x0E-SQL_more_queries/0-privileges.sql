-- Check if user_0d_1 exists and list privileges
SELECT User, Host, Select_priv, Insert_priv, Update_priv, Delete_priv, Create_priv, Drop_priv
FROM mysql.user 
WHERE User='user_0d_1';

-- Check if user_0d_2 exists and list privileges
SELECT User, Host, Select_priv, Insert_priv, Update_priv, Delete_priv, Create_priv, Drop_priv
FROM mysql.user 
WHERE User='user_0d_2';
