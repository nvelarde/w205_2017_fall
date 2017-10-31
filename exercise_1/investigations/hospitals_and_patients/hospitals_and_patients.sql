DROP VIEW IF EXISTS my_results;

CREATE VIEW my_results AS
SELECT
	provider_id,
	base_score + consistency_score AS total_score
FROM my_survey;

SELECT
	(AVG(my_hospitals.rating * my_results.total_score) - AVG(my_hospitals.rating) * AVG(my_results.total_score)) / (STDDEV(my_hospitals.rating) * STDDEV(my_results.total_score)) AS correlation
FROM my_hospitals
JOIN my_results
ON my_hospitals.provider_id = my_results.provider_id;
