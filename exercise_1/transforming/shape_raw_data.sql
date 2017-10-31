DROP TABLE IF EXISTS my_hospitals;

CREATE TABLE my_hospitals AS
SELECT
	provider_id,
	hospital_name,
	city,
	state,
	hospital_type AS type,
	hospital_ownership AS ownership,
	CAST(hospital_overall_rating AS DECIMAL(1,0)) AS rating
FROM hospitals
WHERE hospital_overall_rating NOT LIKE 'Not%';

DROP TABLE IF EXISTS my_readmissions;

CREATE TABLE my_readmissions AS
SELECT
	provider_id,
	hospital_name,
	measure_name,
	measure_id,
CASE compared_to_national
WHEN 'Better than the National Rate' THEN 3
WHEN 'No Different than the National Rate' THEN 2
WHEN 'Worse than the National Rate' THEN 1
ELSE NULL
END AS relative_score,
CAST(score AS DECIMAL(5,2)) AS numeric_score,
CASE denominator
WHEN 'Not Available' THEN 1
ELSE CAST(denominator AS DECIMAL(5,0))
END AS weight
FROM readmissions
WHERE score NOT LIKE 'Not%';

DROP TABLE IF EXISTS my_survey;

CREATE TABLE my_survey AS
SELECT
	provider_number AS provider_id,
	hospital_name,
	CAST(hcahps_base_score AS DECIMAL(2,0)) AS base_score,
	CAST(hcahps_consistency_score AS DECIMAL(2,0)) AS consistency_score
FROM survey_responses
WHERE hcahps_base_score NOT LIKE 'Not%';

DROP TABLE my_ecare;

CREATE TABLE my_ecare AS
SELECT
	provider_id,
	hospital_name,
	condition,
	measure_id,
	measure_name,
	CAST(score AS DECIMAL(5,0)) AS numeric_score,
	CAST(sample AS DECIMAL(7,0)) AS weight
FROM effective_care
WHERE measure_id = 'EDV' OR score NOT LIKE 'Not%';
