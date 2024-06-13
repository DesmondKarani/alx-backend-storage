-- 4-store.sql
-- Script to create a trigger that decreases the quantity of an item after adding a new order

-- Drop the trigger if it exists
DROP TRIGGER IF EXISTS decrease_quantity_trigger;

-- Create the trigger
DELIMITER //
CREATE TRIGGER decrease_quantity_trigger
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END //
DELIMITER ;
