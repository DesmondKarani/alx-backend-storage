-- 101-average_weighted_score.sql
-- Script to create a stored procedure ComputeAverageWeightedScoreForUsers that computes and stores the average weighted score for all students.

-- Drop the procedure if it exists
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;

-- Create the procedure
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE user_id INT;
    DECLARE total_score FLOAT;
    DECLARE total_weight INT;
    DECLARE avg_score FLOAT;

    -- Cursor to iterate over each user
    DECLARE user_cursor CURSOR FOR
        SELECT id FROM users;
    
    -- Handler for when no more rows are found
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    -- Open the cursor
    OPEN user_cursor;

    -- Loop through each user
    user_loop: LOOP
        FETCH user_cursor INTO user_id;
        IF done THEN
            LEAVE user_loop;
        END IF;

        -- Calculate the total weighted score and total weight for the user
        SELECT SUM(c.score * p.weight), SUM(p.weight)
        INTO total_score, total_weight
        FROM corrections c
        JOIN projects p ON c.project_id = p.id
        WHERE c.user_id = user_id;

        -- Calculate the average weighted score
        IF total_weight > 0 THEN
            SET avg_score = total_score / total_weight;
        ELSE
            SET avg_score = 0;
        END IF;

        -- Update the user's average_score in the users table
        UPDATE users
        SET average_score = avg_score
        WHERE id = user_id;
    END LOOP;

    -- Close the cursor
    CLOSE user_cursor;
END //

DELIMITER ;
