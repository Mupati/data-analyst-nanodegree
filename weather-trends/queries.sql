-- View all the cities and countries from the city_list table
SELECT
  *
FROM city_list;
-- Get Accra data from the city_data table.
SELECT
  year,
  avg_temp
FROM city_data
WHERE
  city = 'Accra';
-- Get The Global Data
SELECT
  *
FROM global_data;