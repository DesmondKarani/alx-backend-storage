-- 3-glam_rock.sql
-- Script to list all bands with Glam rock as their main style, ranked by their longevity

SELECT band_name,
       IF(split IS NOT NULL AND split <> '', 2022 - formed, YEAR(CURDATE()) - formed) AS lifespan
FROM metal_bands
WHERE main_style = 'Glam rock'
ORDER BY lifespan DESC;
