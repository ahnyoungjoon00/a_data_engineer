# function 사용
# 1. 문자열관련함수
# length, char_length, substr, trim, lpad, rpad, ...
select length('멀티캠퍼스');
select char_length('멀티캠퍼스');
select length('multicampus');
select char_length('multicampus');

SELECT substr('multicampus',2);
SELECT substr('multicampus',2, 4); # 2번부터 4개
SELECT substr('multicampus' from 2 for 4); # 2번부터 4개
SELECT substr('multicampus',-3);
SELECT substr('multicampus' from -6 for 4); 

# employee 테이블에서 남자인 직원 조회
select *
from employee
where substr(emp_no, -7, 1) in (1,3);

# instr
SELECT INSTR('foobarbar', 'bar');

# employee 테이블에서 사원 이름, 이메일, 이메일 아이디 조회
select emp_name, email, substr(email,1, instr(email, '@')-1) as email_id
from employee;

# concat
select concat('mult', 'camp','us');
select concat('mult', 'camp', null);

SELECT concat_ws('', 'mult', 'camp', NULL);
select concat_ws('!!','mult', 'camp', 'us');

# replace
SELECT replace(email, '@', '$$')
from employee;

# trim

SELECT TRIM('  bar   ');
SELECT TRIM(LEADING 'x' FROM 'x    barxxx');
SELECT TRIM(BOTH 'x' FROM 'xxxbarxxx');
SELECT TRIM('y' FROM 'yyybaryyy');
SELECT TRIM(TRAILING 'xyz' FROM 'barxxyz');

# ucase
select ucase('xxxmulticampusxxx');

#rpad
select rpad('multicampus', 20, '*');

#lpad
select lpad('multicampus', 20, '*');

#lpad
select lpad('1', 3, '0');

# employee 테이블에서 사원명과 주민번호를 조회하시오
# 단, 주민번호의 뒤 8자리는 *로 마스킹처리
# 1) replace
select emp_name, emp_no, replace(emp_no, substr(emp_no, instr(emp_no, '-')+1), '*******')as na_code
from employee;
# 2) concat
select emp_name, emp_no, concat(substr(emp_no, 1, 7), '*******') as na_code
from employee;
# 3) rpad
select emp_name, emp_no, rpad(substr(emp_no, 1, 7), 14, '*') as na_code
from employee;

# 숫자 관련 함수
# abs, mod(나머지), floor, ceil, round, truncate(floor와 같이 버림인데 어느자리에서 버릴지 선택 가능)
select abs(-100);
select mod(100, 3);
select floor(10.555);
select ceil(10.555);
select round(10.555,2);
select truncate(100.555, 2);
select truncate(100.555, -2);

# 날짜 관련 함수
# now, datediff(두 날의 차이), date_add(더하기), date_sub(빼기), year, month, date, ...
select now();

# datediff
# employee테이블에서 사원들의 근무일자 조회
select emp_name, datediff(now(), hire_date) as '근무일자'
from employee
where ent_yn = 'N';

# date_add, date_sub (date, interval expr unit)
SELECT DATE_ADD(now(), INTERVAL 31 DAY);
SELECT DATE_ADD(now(), INTERVAL '5:10.0001' minute_microsecond);
SELECT DATE_sub(now(), INTERVAL 12 month);

select now(), year(now()), month(now()), day(now()), dayofweek(now()),
	hour(now()), minute(now()), second(now());
    
# 형변환 함수
# cast, convert
select cast('2024-12-04' as date);
select cast('2024-12-04' as datetime);
select cast('100' as double) + 0.2;
select cast('57년' as year);

# case-when-then
# case ... when 조건식 then 표현식
# else ...
select emp_name, salary,
case 
when salary >= 6000000 and salary <= 10000000 then 'S1'
when salary >= 5000000 and salary < 6000000 then 'S2'
when salary >= 4000000 and salary < 5000000 then 'S3'
when salary >= 3000000 and salary < 4000000 then 'S4'
when salary >= 2000000 and salary < 3000000 then 'S5'
else 'S6'
end as sal_level
from employee;