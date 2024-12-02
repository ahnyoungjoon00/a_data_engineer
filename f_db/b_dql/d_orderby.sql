# order by
# result set을 정렬하기 위해 사용
# select문의 가장 마지막에 작성되고, 실행순서도 가장 마지막
# from -> where -> group by -> having -> select -> order by

# asc 오름차순(default), desc 내림차순
# 사원들의 이름, 급여, 보너스, 연봉 레벨, 부서코드 조회
select emp_name, salary, bonus, sal_level, dept_code
from employee
order by dept_code;

select emp_name, salary, bonus, sal_level, dept_code
from employee
order by dept_code desc;

# 연봉 레벨로 오름차순 정렬, 연봉 레벨이 같다면 연봉으로 내림차순
select emp_name, salary, bonus, sal_level, dept_code
from employee
order by sal_level, salary desc;


select emp_name, salary, bonus, sal_level, dept_code
from employee
order by bonus is null asc, bonus asc;
# is null로 하면 true/false값으로 주어지는데 이걸로 먼저 정렬하고 bonus 값으로 정렬해서 null = true = 1이라 아래로 밀리고 시작

# Top N 구문
# limit 시작인덱스, 출력 개수
# limit 0, 5 => 0번 인덱스부터 5개 출력
select emp_name, salary
from employee
order by salary desc
limit 3, 5;

# employee 테이블에서 가장 퇴근에 입사한 사원 5명
select emp_name, hire_date
from employee
order by hire_date desc
limit 5;