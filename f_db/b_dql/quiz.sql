#1. 급여가 200만원 이상인 대리 직급 직원을 조회하세요
select emp_name, salary
from employee
where job_code = (select job_code 
	from job
    where job_name = '대리')
and salary >= 2000000;

select emp_name, salary, job_name
from employee e
join job j on (e.job_code = j.job_code)
where job_name = '대리';

#2. 직급별 급여 평균과 같은 직급, 급여를 가진 직원 조회하세요
select emp_name, job_code, salary
from employee
where (job_code, salary) in
	(select job_code, avg(salary)
	from employee
	group by job_code);
    
#3. 부서명과 부서별 평균급여를 구하시오
# 평균 급여는 소수점에서 내림처리하여 정수로 표현하세요
# 부서에 사원이 존재하지 않아 평균급여가 null일경우는 0원으로 표시하세요
select d.dept_title, floor(avg(salary))
from employee e
join department d on (e.DEPT_CODE = d.DEPT_ID)
group by e.DEPT_CODE;

#4. 각 부서별 급여의 합계들을 구하여, 
#부서 급여합이 1000만을 초과하는 부서명과 부서별 급여합계를 조회하는
#SELECT 문을 작성하시오.
select d.dept_title, sum(salary) as sum_sal
from employee e
join department d on (e.DEPT_CODE = d.DEPT_ID)
group by e.DEPT_CODE
having sum_sal > 10000000;

#5. 직원 테이블에서 보너스 포함한 연봉이 높은 5명의
# 사번, 이름, 부서명, 직급명, 입사일을 조회하세요
select emp_id, emp_name, d.dept_title, j.job_name, hire_date
from employee e
join department d on (e.DEPT_CODE = d.DEPT_ID)
join job j on (e.job_code = j.job_code)
order by (salary*12 + salary*ifnull(bonus, 0)) desc
limit 5;

#6.70년대 생이면서 성별이 여성이고 성이 전씨인 사원의
#이름, 주민등록번호, 부서명, 직급명을 출력하세요.
select emp_name, emp_no, dept_title, job_name 
from employee e
join department d on (e.DEPT_CODE = d.DEPT_ID)
join job j on (e.job_code = j.job_code)
where substr(emp_no, 1, 1) in (6, 7)
and substr(emp_no, 8, 1) = 2
and substr(emp_name, 1, 1) = '전';

#7. 이름에 '형'이 들어가는 사원의 사원ID, 사원이름, 직업명을 출력하세요 
select emp_id, emp_name, job_name
from employee e
join job j on (e.job_code= j.job_code)
where emp_name like '%형%';

#8. 부서코드가 D5, D6 인 사원의 이름, 직급명, 부서코드, 부서명을 출력하세요
select emp_name, job_name, dept_code, dept_title
from employee e
join job j on (e.job_code=j.job_code)
join department d on (e.dept_code=d.dept_id)
where dept_code in ('D5', 'D6');

#9. 사번, 사원명, 급여
#급여가 500만원 이상이면 '고급'
#급여가 300~500만원이면 '중급'
#그 이하는 '초급'으로 출력처리 하고 별칭은 '구분' 으로 한다.
select emp_id, emp_name, salary, 
case 
when salary >= 5000000 then '고급'
when salary >= 3000000 and salary < 5000000 then '중급'
else '초급'
end as '구분'
from employee;

#10. 보너스를 받은 사원의 사원명, 보너스, 부서명, 지역명을 출력하세요
select emp_name, bonus, salary*bonus as bonus_m ,dept_title, local_name 
from employee e
join department d on (e.dept_code=d.dept_id)
join location l on (d.location_id=l.local_code)
where bonus is not null;

#11. 부서가 위치한 국가가 한국이나 일본인 사원의
#이름, 부서명, 지역명, 국가명을 출력하시오
select e.emp_name, d.dept_title, l.local_name, n.national_name
from employee e
join department d on (e.dept_code=d.dept_id)
join location l on (d.location_id=l.local_code)
join national n on (l.national_code=n.national_code)
where national_name in ('한국', '일본');

#12. job_code가 'J4', 'J7'이면서 보너스를 받지 못한 사원의 
#이름, 직급명, 급여, 보너스금액(0원으로) 출력하세요
select emp_name, job_name, salary, ifnull(bonus*salary, 0) as 보너스금액 
from employee e
join job j on (e.job_code=j.job_code)
where e.job_code in ('J4', 'J7')
and bonus is null;