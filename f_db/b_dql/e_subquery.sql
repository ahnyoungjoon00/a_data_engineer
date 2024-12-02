# sub query
# 쿼리 안에 쿼리

# 노옹철사원과 같은 부서인 직원 명단을 조회하시오
# 조건 : 쿼리 2개 작성
select emp_id, emp_name, dept_code
from employee
where dept_code = 
	(select dept_code
	from employee
	where emp_name = '노옹철');
    
# 서브쿼리 분류
# 1. 사용 위치에 따른 분류
# select절 : 스칼라(단일값) 서브쿼리
# from절 : 인라인뷰 서브쿼리
# where, having절 : 서브쿼리 

# 2. 서브쿼리의 result set 형태에 따라 분류
# 단일행, 단일열, 다중행, 다중열, ... 
select emp_id, emp_name, dept_code
from employee
where dept_code = 
	(select dept_code
	from employee
	where emp_name = '노옹철');
    
select emp_name, (select dept_code
	from employee
	where emp_name = '노옹철')
from employee
where dept_code = 
	(select dept_code
	from employee
	where emp_name = '노옹철');
    
# 단일열, 다중행 서브쿼리
# in, any, all, exits

# IN
# 급여가 4,999,999이하인 급여등급을 가지고 있는 모든 직원을 조회
select emp_name, sal_level
from employee
where sal_level in
	(select sal_level
	from sal_grade
	where max_sal < 4999999)
order by sal_level;

# ALL
# 단일열 다중행 서브쿼리가 반환하는 result set과 컬럼값을 비교연산하였을 때, 모두가 true면 참, and
# where 1 < ALL(100, 200, 300, 400, 0.9) => (t, t, t, t, f) 결과는 false
# where 1 < ALL(100, 200, 300, 400, 9) => (t, t, t, t, t) 결과는 true

# 박나라가 속한 부서의 사람들 중에서 가장 많은 연봉을 받는 사람보다
# 더 많은 연봉을 받는 사람을 구해보자. 단, group by는 사용할 수 없다.
select emp_name, salary
from employee
where salary > all
	(select salary
	from employee
	where dept_code =
		(select dept_code
		from employee
		where emp_name = '박나라'));
        
# EXITS
# 서브쿼리의 결과가 있으면 true
# 존재 하냐마냐에 따라 D9는 다른 데이터까지 전체 출력, D3은 없으니까 아무것도 출력 X
select emp_id, dept_code
from employee
-- where exists(select dept_code from employee where dept_code = 'D9');
where exists(select dept_code from employee where dept_code = 'D3');

# 상관쿼리(상호연관쿼리)
# 메인쿼리에서 사용하는 컬럼값을 서브쿼리에서도 사용하는 것
# 메인쿼리 테이블을 참조하는 래퍼런스를 서브쿼리에서 사용하는 것
# 매니저인 사원을 조회
select emp_id, emp_name, manager_id
from employee e
where exists(select emp_id 
			from employee 
			where manager_id = e.emp_id);

# quiz. in을 사용해서 위와 같은 결과를 반환하는 쿼리를 작성하시오.
select emp_id, emp_name, manager_id
from employee
where emp_id in(select manager_id
					from employee);

# 다중열 서브쿼리
# 퇴사한 직원이 존재하는 부서의 사원 중
# 퇴사한 사원과 같은 직급인 사원의 이름, 직급, 부서를 조회
select emp_name, job_code, dept_code
from employee
where dept_code in 
	(select dept_code 
	from employee
	where ent_yn = 'Y')
and job_code in
	(select job_code
    from employee
    where ent_yn = 'Y');
    
select emp_name, job_code, dept_code
from employee
where (dept_code, job_code) in 
	(select dept_code, job_code
    from employee
    where ent_yn = 'Y');
    
# 인라인 뷰 : from 절에서 사용하는 서브쿼리
# mysql에서는 인라인뷰에 반드시 별칭이 있어야한다.
# 성능이슈가 없음
select *
from (
	select emp_id, emp_name, job_code
    from employee
    where job_code = 'J6'
    ) e
where e.emp_name like '전%';