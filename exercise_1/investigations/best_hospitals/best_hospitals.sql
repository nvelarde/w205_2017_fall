SELECT
	my_hospitals.provider_id,
	my_hospitals.hospital_name,
	my_hospitals.ownership,
	my_hospitals.rating,
	CAST(AVG(my_readmissions.relative_score) AS DECIMAL(5,2)) AS avg_rel_pscore,
	CAST(STDDEV(my_readmissions.relative_score) AS DECIMAL(5,2)) AS stdev_rel_pscore,
	CAST(AVG(my_readmissions.relative_score) / STDDEV(my_readmissions.relative_score) AS DECIMAL(5,2)) AS scaled_pscore,
	CAST((my_hospitals.rating + (AVG(my_readmissions.relative_score) / STDDEV(my_readmissions.relative_score))) AS DECIMAL(5,2)) AS quality_score
FROM my_hospitals
JOIN my_readmissions
ON my_hospitals.provider_id = my_readmissions.provider_id
GROUP BY
	my_hospitals.provider_id,
	my_hospitals.hospital_name,
	my_hospitals.ownership,
	my_hospitals.rating
ORDER BY quality_score DESC
LIMIT 10;
