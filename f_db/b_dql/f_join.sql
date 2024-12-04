# join
# 0. 관계형 데이터베이스에서 데이터 중복을 최소화하고 이상현상을 방지하기 위해 
# 	 연관된 데이터들을 분리하여 저장하도록 설계
#	 분리되어 저장된 테이블의 데이터를 다시 결합하여 조회하도록 해주는 기능
# 1. 서브쿼리와 동일한 동작을 하는 sql을 작성하면서, 성능상의 문제를 최소화할 수 있다.

# 모든 직원이름, 부서명 조회
select emp_name, (select dept_title 
				from department 
                where e.dept_code = dept_id) as dept
from employee e;

select *
from employee e
join department d 
on(e.dept_code = d.dept_id);
# e의행 X d의 행만큼 비교연산을 하게 된다.

# join
# cross join, 
# inner join, 
# outer join(left join, right join, full outer join-공식지원 X)

# cross join : 사용하면 안됨
# 조인조건절이 무조건 참인 조인, 모든 경우의 수를 모두 출력해주는
# ex) 30만개 상품과 300만개 주문 cross join시,
#	  9천억개의 행을 가진 result set이 나와버림
select *
from employee
cross join department;

# 2. inner join(equals join, 등가조인)
# 	 = join으로 줄여서 사용
# 조인조건절을 등위비교로 작성한 join, 한쪽은 unique한 값을 갖는 상태여야함

# 사번, 이름, 직급명 출력
select emp_id, emp_name, e.job_code, j.job_name
from employee e
join job j on (e.job_code = j.job_code);

# using
# inner 조건절에서 사용할 두 컬럼 이름이 같다면 using 사용
select emp_id, emp_name, job_code, job_name
from employee e
join job j using(job_code);

# 여러 테이블 join하기
# 모든 사원들의 사번 이름 부서명 근무지 조회
select emp_id, emp_name, dept_title, local_name
from employee e
join department d on (e.dept_code = d.dept_id)
join location l on (d.location_id = l.local_code);

# ASIA(1, 2, 3)지역에서 근무하는 급여 500만원 미만의 모든 사원을 조회
select emp_id, emp_name, salary, local_name
from employee e
join department d on (e.dept_code = d.dept_id)
join location l on (d.location_id = l.local_code)
where (salary < 5000000) 
and local_name like 'ASIA%';

select emp_id, emp_name, salary, local_name
from 
(select emp_id, emp_name, salary, dept_code
from employee
where salary < 5000000) e
join department d on (e.dept_code = d.dept_id)
join 
(select local_code, local_name
from location
where local_name like 'ASIA%') l on (d.location_id = l.local_code);

# outer join - inner join과 개념적 차이를 설명할줄 알아야
# join조건절이 false를 반환하더라도, 특정 테이블을 기준으로 result set에 행을 포함시키는 join
# 부서별 사원수를 조회
select dept_title, count(*)
from employee e
left join department d on (e.DEPT_CODE = d.dept_id)
group by dept_title
order by dept_title;

select dept_title, count(*)
from employee e
right join department d on (e.DEPT_CODE = d.dept_id)
group by dept_title
order by dept_title;

# full outer join - 공식지원 X
# 동일한 결과를 내는 방법
select *
from employee e
left join department d on (e.DEPT_CODE = d.dept_id)
union
select *
from employee e
right join department d on (e.DEPT_CODE = d.dept_id)
order by dept_title;

# self join
# employee 테이블에서 이름, 매니저사번 매니저 이름을 조회하는 쿼리
select emp_name, manager_id,
		(select emp_name
		from employee
		where emp_id = e.manager_id) as manager_name
from employee e;

select e.emp_name, e.manager_id, f.emp_name as manager_name
from employee e
join employee f on (e.manager_id = f.emp_id);

select e.emp_name, e.manager_id, f.emp_name as manager_name
from employee e
left join employee f on (e.manager_id = f.emp_id);