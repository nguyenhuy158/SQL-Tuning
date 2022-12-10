-- Truong hop 1
-- 
-- 
-- 
-- query not tuning
SELECT s.fname,
    s.lname,
    r.signup_date
FROM student s
    INNER JOIN registration r ON s.student_id = r.student_id
    INNER JOIN class c ON r.class_id = c.class_id
WHERE c.name = 'SQL TUNING'
    AND r.signup_date BETWEEN @BeginDate AND @EndDate
    AND r.cancelled = 'N';
-- 
-- 
-- 
-- 
-- query tuning
SELECT ss.fname,
    ss.lname,
    rr.signup_date
FROM (
        SELECT s.student_id,
            s.fname,
            s.lname
        FROM student s
    ) ss
    JOIN (
        SELECT r.student_id,
            r.class_id,
            r.signup_date
        FROM registration r
        WHERE r.signup_date BETWEEN @BeginDate AND @EndDate
            AND r.cancelled = 'N'
    ) rr on ss.student_id == rr.student_id (
        SELECT c.class_id
        FROM class c
        WHERE c.name = 'SQL TUNING'
    ) cc on rr.class_id == cc.class_id