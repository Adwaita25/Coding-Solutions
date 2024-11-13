SELECT Employee.name, Bonus.bonus From Employee
LEFT JOIN Bonus ON Employee.empID = Bonus.empID
WHERE bonus < 1000 OR bonus IS NULL;
