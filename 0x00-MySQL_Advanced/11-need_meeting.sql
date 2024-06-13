-- 11-need_meeting.sql
-- Script to create a view need_meeting that lists all students that have a score under 80 (strict) and no last_meeting or more than 1 month

-- Drop the view if it exists
DROP VIEW IF EXISTS need_meeting;

-- Create the view
CREATE VIEW need_meeting AS
SELECT name
FROM students
WHERE (score < 80)
AND (last_meeting IS NULL OR last_meeting < DATE_SUB(CURDATE(), INTERVAL 1 MONTH));
