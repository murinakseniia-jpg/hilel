-- завдання 1
SELECT name, breed, weight
FROM Dogs;

-- завдання 2
SELECT *
FROM Dogs
WHERE weight > 25;

-- завдання 3
SELECT name, email
FROM Owners
WHERE city = 'Kyiv';

-- завдання 4
SELECT name, birth_year
FROM Dogs
WHERE breed = 'mixed';

-- завдання 5 
SELECT reason, visit_date, price
FROM Visits
ORDER BY price DESC
LIMIT 5;