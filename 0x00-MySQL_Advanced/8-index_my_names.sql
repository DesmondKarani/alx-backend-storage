-- 8-index_my_names.sql
-- Script to create an index idx_name_first on the table names and the first letter of name

-- Drop the index if it exists
DROP INDEX IF EXISTS idx_name_first ON names;

-- Create the index
CREATE INDEX idx_name_first ON names (name(1));
