# Write your MySQL query statement below
SELECT 
    teacher_id, COUNT(DISTINCT subject_id) as cnt
From Teacher
GROUP BY teacher_id
