
with t as (
  select
    year_no,
    calendar_dt,
    count(day_of_year_no) over (PARTITION BY year_no) * 0.5 holiday_count_med,
    count(day_of_year_no) over (PARTITION BY year_no ORDER BY day_of_year_no) holiday_num
  from public.calendar
  where holiday_flg = 1
)

select year_no,
min(calendar_dt) as calendar_dt
from t
where holiday_num >= holiday_count_med
group by year_no
order by year_no;


select
  ic.customer_rk
  coalesce(avg(ca_usd.account_opening_amt) over (PARTITION BY ca_usd.customer_rk),0) avg_usd,
  coalesce(avg(ca_eur.account_opening_amt) over (PARTITION BY ca_eur.customer_rk),0) avg_eur,
from public.individual_customer ic
  left join public.core_account ca_eur on ic.customer_rk = ca_eur.customer_rk
    and ca_eur.currency_cd = 'EUR'
    and ca_eur.account_renewal_cnt = 1
  left join public.core_account ca_usd on ic.customer_rk = ca_usd.customer_rk
    and ca_usd.currency_cd = 'USD'
    and ca_usd.account_renewal_cnt = 1
where extract(year from age(birth_dt)) <= 21
  and ic.valid_to_dttm = '5999-01-01 00:00:00'
  and ic.monthly_income_amt > 300000;
