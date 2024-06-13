-- 7-average_score.sql
-- Script to create a stored procedure ComputeAverageScoreForUser that computes and stores the average score for a student


DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(
  IN user_id INT
)
BEGIN
  DECLARE total_score FLOAT;
  DECLARE num_corrections INT;

  -- Initialize variables
  SET total_score = 0;
  SET num_corrections = 0;

  -- Calculate total score and number of corrections for the user
  SELECT SUM(score), COUNT(*)
  INTO total_score, num_corrections
  FROM corrections
  WHERE user_id = user_Id;

  -- Update user's average score (handle division by zero)
  IF num_corrections > 0 THEN
    UPDATE users
    SET average_score = total_score / num_corrections
    WHERE id = user_id;
  END IF;
END //

DELIMITER ;
