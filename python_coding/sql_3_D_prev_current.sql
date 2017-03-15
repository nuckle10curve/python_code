
select t1.actual - t2.actual as previous_minus_curremt 
from target_actual t1,target_actual t2 
where t1.id = t2.id - 1