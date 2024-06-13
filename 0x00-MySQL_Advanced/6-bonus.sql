-- 6-bonus.sql
-- Script to create a stored procedure AddBonus that adds a new correction for a student

-- Drop the procedure if it exists
DROP PROCEDURE IF EXISTS AddBonus;

-- Create the procedure
DELIMITER //
CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
    DECLARE project_id INT;

    -- Check if project exists, otherwise insert it
    SELECT id INTO project_id FROM projects WHERE name = project_name;
    IF project_id IS NULL THEN
        INSERT INTO projects (name) VALUES (project_name);
        SET project_id = LAST_INSERT_ID();
    END IF;

    -- Insert the correction
    INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, project_id, score);
END //
DELIMITER ;
