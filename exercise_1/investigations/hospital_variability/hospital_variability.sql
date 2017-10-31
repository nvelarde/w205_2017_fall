DROP VIEW IF EXISTS my_procedures;

CREATE VIEW my_procedures AS
SELECT
	measure_id,
	measure_name,
	numeric_score
FROM my_readmissions
UNION ALL
SELECT
	measure_id,
	measure_name,
	numeric_score
FROM my_ecare;

SELECT
	measure_id,
	measure_name,
	CAST((STDDEV(numeric_score)/AVG(numeric_score)) AS DECIMAL(5,2)) AS coeff_var
FROM my_procedures
GROUP BY measure_id, measure_name
ORDER BY coeff_var DESC
LIMIT 10;
