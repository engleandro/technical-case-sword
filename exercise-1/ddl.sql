-- Create the table
CREATE TABLE scores (
    id INTEGER PRIMARY KEY,
    patient_id INTEGER,
    scores TEXT,
    date DATE
);

-- Insert data into the table
INSERT INTO patient_scores (id, patient_id, scores, date) VALUES
(1, 1323, '{"satisfaction": 9, "pain": 2, "fatigue": 2}', '2020-06-25'),
(2, 9032, '{"satisfaction": 2, "pain": 7, "fatigue": 5}', '2020-06-30'),
(3, 2331, '{"satisfaction": 7, "pain": 1, "fatigue": 1}', '2020-07-05'),
(4, 2303, '{"satisfaction": 8, "pain": 9, "fatigue": 0}', '2020-07-12'),
(5, 1323, '{"satisfaction": 10, "pain": 0, "fatigue": 0}', '2020-07-09'),
(6, 2331, '{"satisfaction": 8, "pain": 9, "fatigue": 5}', '2020-07-20');
