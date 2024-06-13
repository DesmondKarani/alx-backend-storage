-- 10-div.sql
-- Script to create a function SafeDiv that divides the first by the second number or returns 0 if the second number is equal to 0

-- Drop the function if it exists
DROP FUNCTION IF EXISTS SafeDiv;

-- Create the function
DELIMITER //
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS DECIMAL(10, 4)
BEGIN
    DECLARE result DECIMAL(10, 4);
    
    IF b != 0 THEN
        SET result = a / b;
    ELSE
        SET result = 0;
    END IF;
    
    RETURN result;
END //
DELIMITER ;
