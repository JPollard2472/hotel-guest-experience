WITH tagged AS (
    SELECT rating, 'Friendly staff' AS theme FROM reviews
        WHERE review LIKE '%friendly%' OR review LIKE '%helpful%'
    UNION ALL
    SELECT rating, 'Rude staff' FROM reviews
        WHERE review LIKE '%rude%' OR review LIKE '%unhelpful%'
    UNION ALL
    SELECT rating, 'Feeling welcome' FROM reviews
        WHERE review LIKE '%welcom%'
    UNION ALL
    SELECT rating, 'Clean' FROM reviews
        WHERE review LIKE '%clean%'
    UNION ALL
    SELECT rating, 'Dirty' FROM reviews
        WHERE review LIKE '%dirty%' OR review LIKE '%stain%'
    UNION ALL
    SELECT rating, 'Noise' FROM reviews
        WHERE review LIKE '%noise%' OR review LIKE '%noisy%'
    UNION ALL
    SELECT rating, 'Comfortable bed' FROM reviews
        WHERE review LIKE '%comfortable bed%' OR review LIKE '%comfy%'
    UNION ALL
    SELECT rating, 'Value for money' FROM reviews
        WHERE review LIKE '%value%' OR review LIKE '%worth%'
    UNION ALL
    SELECT rating, 'Expensive' FROM reviews
        WHERE review LIKE '%expensive%' OR review LIKE '%overpriced%'
)
SELECT theme,
       COUNT(*) AS reviews_mentioning,
       ROUND(AVG(rating), 2) AS avg_rating,
       ROUND(AVG(rating) - (SELECT AVG(rating) FROM reviews), 2) AS vs_overall
FROM tagged
GROUP BY theme
ORDER BY avg_rating DESC;