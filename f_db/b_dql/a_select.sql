# dql : 테이블에서 데이터를 조회하기 위한 구문
# 테이블에서 원하는 데이터를 조회한 결과집합을 result set이라 한다.

# [작성법]
# select 컬럼명...
# from 테이블명...
# where 조건절...

# job테이블의 모든 데이터를 조회
select *
from job;
select job_code
from job;

# job테이블에서 직급명이 '대표'인 직급코드를 조회해보자
select job_code
from job
where JOB_NAME = '대표';

# employee 테이블에서 급여가 3,000,000이상인 사원들의 이름과 급여를 조회
select EMP_NAME, SALARY
from employee
where SALARY >= 3000000;

# employee 테이블에서 직원의 이름과 연봉 (급여*12)을 조회하시오
# result set의 컬럼에 별칭 붙이기 as
select EMP_NAME, SALARY*12 as '연봉' 
from employee;

select emp_name, salary > 3000000
from employee;

# distinct : 중복제거
select distinct dept_code, ent_yn
from employee;

# 실습 quiz
# 1. employee 테이블에서 부터코드가 D9 또는 D5이고,
# 급여를 400이상 받는 모든 사원 조회 
# 의도 : not and or 논리연산자 우선순위에 따라 select됨
select * 
from employee
where (dept_code = 'D9' or dept_code = 'D5')
and SALARY > 4000000;

select * 
from employee
where (dept_code = 'D9' or dept_code = 'D5');

select * 
from employee
where (dept_code = 'D9' or 'D5');
