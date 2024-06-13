-- 5-valid_email.sql
-- Script to create a trigger that resets the attribute valid_email only when the email has been changed

-- Drop the trigger if it exists
DROP TRIGGER IF EXISTS reset_valid_email_trigger;

-- Create the trigger
DELIMITER //
CREATE TRIGGER reset_valid_email_trigger
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF NEW.email <> OLD.email THEN
        SET NEW.valid_email = 0;
    END IF;
END //
DELIMITER ;
