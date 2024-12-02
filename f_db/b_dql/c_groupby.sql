# group by 
# 특정 컬럼을 기준으로 그룸핑
# group by 컬럼명
# having 조건절
# having 조건절에는 집계함수를 사용 가능하다
# sum, count, avg, max, min

select sum(salary), count(salary), avg(salary), max(salary), min(salary)
from employee
where ent_yn = 'N';

# 부서별 급여, 총합, 개수, 평균, 최대, 최소 급여 출력
select dept_code, sum(salary), count(salary), avg(salary), max(salary), min(salary)
from employee
group by dept_code;

# dept_code로 그룹핑이 안되는 emp_id를 조회하는것은 에러이다.
select dept_code, emp_id, sum(salary), count(salary), avg(salary), max(salary), min(salary)
from employee
group by dept_code;

# 부서별, 직급별 급여, 총합, 개수, 평균, 최대, 최소 급여 출력
select dept_code, job_code, sum(salary), count(salary), avg(salary), max(salary), min(salary)
from employee
group by dept_code, job_code;

# having절
# group by에 의해 생성된 그룹들에 대한 조건절
select dept_code, job_code, sum(salary), count(salary), avg(salary), max(salary), min(salary)
from employee
group by dept_code, job_code
having sum(salary) <= 3000000;

# rollup
# 그룹별 중간 집계와 총 집계를 계산하기 위해 사용
select dept_code, job_code, sal_level, sum(salary), count(salary)
from employee
group by dept_code, job_code, sal_level with rollup;

# grouping
# 집계값의 연산에 포함된 컬럼이면 0 아니면 1
select dept_code, job_code, sal_level
, grouping(dept_code)
, grouping(job_code)
, grouping(sal_level)
, sum(salary), count(salary)
from employee
group by dept_code, job_code, sal_level with rollup
order by 
dept_code is null asc
, job_code is null asc
, sal_level is null asc
, dept_code asc
, job_code asc
, sal_level asc;