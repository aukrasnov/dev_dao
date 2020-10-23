-- 1.
with t as (
 select 
  customer_rk 
  ,monthly_income_amt
 from public.individual_customer
 where monthly_income_amt in (60000)
)

select extract('year' from birth_dt) birth_year
 ,count(distinct ic.customer_rk) count_customers
from public.individual_customer ic
 inner join t on ic.customer_rk = t.customer_rk
where ic.monthly_income_amt in (50000)
group by birth_year
order by count_customers desc

-- 2.
select customer_rk
 ,max(monthly_income_amt) max_zp
 from public.individual_customer ic
 where middle_nm not like '%А'
 group by customer_rk
 having max(monthly_income_amt)/min(monthly_income_amt) >= 2;

-- 3.
with t as (
 select customer_rk
  ,extract('year' from birth_dt) birth_year
  ,round(avg(monthly_income_amt),2) avg_zp
 from public.individual_customer ic
 where monthly_income_amt is not null
 group by customer_rk, birth_dt
)

select birth_year
 ,max(avg_zp) max_zp
from t
where birth_year >= 2001
group by birth_year
order by birth_year;
