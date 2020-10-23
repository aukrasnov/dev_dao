-- Узнать средний чек по клиенту в 2018 году
SELECT
  p. client_id
  ,avg(purchase_amt*coalesce(cc. coefficient,1)) avg_purchase_amt
FROM purchase AS p
  LEFT JOIN currency_change cc ON cc. from_currency_id = p. currency_id
    AND cc. to_currency_id = 0
    AND cc.calendar_dt = p.purchase_dt
WHERE p. purchase_dt >= ‘2018-01-01’
  AND p. purchase_dt < ‘2019-01-01’
GROUP BY p. client_id;

-- Узнать объёмы продаж по месяцам в разрезе интернет/(страна + город)
SELECT
  concat(year(p. purchase_dt), ‘_’, month(p. purchase_dt)) purchase_month,
  CASE
    WHEN s.shop_id THEN ‘интернет’
    ELSE concat(s.country_nm, ’_’, s. city_nm)
    END AS purchase_city,
  sum(purchase_amt*coalesce(cc. coefficient,1)) sum_purchase_amt,
  count(purchase_id) count_purchases
FROM purchase AS p
  LEFT JOIN currency_change cc ON cc. from_currency_id = p. currency_id
    AND cc. to_currency_id = 0
    AND cc.calendar_dt = p.purchase_dt
  LEFT JOIN shop s ON p.shop_id = s.shop_id
WHERE p. purchase_dt >= ‘2018-01-01’
  AND p. purchase_dt < ‘2019-01-01’
GROUP BY purchase_month, purchase_city;

-- Оценить продаваемость товаров по кол-ву по месяцам.
SELECT
  concat(year(p. purchase_dt), ‘_’, month(p. purchase_dt)) purchase_month,
  pi. item_desc,
  sum(purchase_item_count) count_purchase_items
FROM purchase AS p
  JOIN purchase_item pi ON p.id = pi. purchase_id
GROUP BY purchase_month, purchase_item_id
ORDER BY purchase_month, count_purchase_items DESC;

-- Оценить продаваемость товаров по цене по кварталам
SELECT
  concat(year(p. purchase_dt), ‘_’, quarter(p. purchase_dt)) purchase_quarter,
  pi.item_desc,
  sum(purchase_item_count * item_price*coalesce(cc. coefficient,1)) sum_items_price,
FROM purchase AS p
  JOIN purchase_item pi ON p.id = pi. purchase_id
  LEFT JOIN currency_change cc ON cc. from_currency_id = p. currency_id
    AND cc. to_currency_id = 0
    AND cc.calendar_dt = p.purchase_dt
GROUP BY purchase_quarter, purchase_item_id
ORDER BY purchase_quarter, sum_items_price DESC;
