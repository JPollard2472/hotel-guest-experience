WITH grouped AS (
    SELECT review,
           CASE
               WHEN rating = 5 THEN 'Delighted (5)'
               WHEN rating >= 3 THEN 'Satisfied (3-4)'
               ELSE 'Disappointed (1-2)'
           END AS guest_group
    FROM reviews
)
SELECT guest_group,
       COUNT(*) AS reviews,
       ROUND(AVG(CASE WHEN review LIKE '%friendly%' OR review LIKE '%helpful%' THEN 1.0 ELSE 0 END) * 100, 1) AS pct_friendly_staff,
       ROUND(AVG(CASE WHEN review LIKE '%rude%' OR review LIKE '%unhelpful%' THEN 1.0 ELSE 0 END) * 100, 1) AS pct_rude_staff,
       ROUND(AVG(CASE WHEN review LIKE '%dirty%' OR review LIKE '%stain%' THEN 1.0 ELSE 0 END) * 100, 1) AS pct_dirty,
       ROUND(AVG(CASE WHEN review LIKE '%noise%' OR review LIKE '%noisy%' THEN 1.0 ELSE 0 END) * 100, 1) AS pct_noise
FROM grouped
GROUP BY guest_group
ORDER BY reviews DESC;