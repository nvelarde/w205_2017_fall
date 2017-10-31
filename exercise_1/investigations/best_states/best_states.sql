SELECT
	sub.state,
	CAST(AVG(sub.quality_score) AS DECIMAL(5,2)) AS avg_q_score
FROM (
	SELECT
		my_hospitals.provider_id,
		my_hospitals.state AS state,
		my_hospitals.rating,
		AVG(my_readmissions.relative_score),
		STDDEV(my_readmissions.relative_score),
		AVG(my_readmissions.relative_score) / STDDEV(my_readmissions.relative_score),
		(my_hospitals.rating + (AVG(my_readmissions.relative_score) / STDDEV(my_readmissions.relative_score))) AS quality_score
	FROM my_hospitals
	JOIN my_readmissions
	ON my_hospitals.provider_id = my_readmissions.provider_id
	GROUP BY my_hospitals.provider_id, my_hospitals.state, my_hospitals.rating
	) AS sub
GROUP BY sub.state
ORDER BY avg_q_score DESC
LIMIT 10;
