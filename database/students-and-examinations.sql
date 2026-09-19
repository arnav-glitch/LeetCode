# Write your MySQL query statement below
SELECT S.student_id, S.student_name, Su.subject_name, COUNT(E.student_id) AS attended_exams
FROM students S CROSS JOIN subjects Su LEFT JOIN examinations E 
ON E.student_id = S.student_id AND E.subject_name = SU.subject_name
GROUP BY S.student_id, S.student_name, SU.subject_name
ORDER BY S.student_id, S.student_name, SU.subject_name