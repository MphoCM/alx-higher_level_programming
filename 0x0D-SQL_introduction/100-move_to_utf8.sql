-- converts the entire database hbtn_0c_0 to UTFB.
USE hbtn_0c-0
ALTER TABLE first_table
CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
