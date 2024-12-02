# where절
# 1. employee테이블에서 월급이 350만원이상 600만원 이하에 속하는 사원정보
select *
from employee
where salary>=3500000 and salary<=6000000;

# between A and B
select *
from employee
where salary between 3500000 and 6000000;

# 2. employee테이브렝서 월급이 350만원 미만, 600만원 초과
select *
from employee
where salary not between 3500000 and 6000000;

# 3. 날짜 타입 데이터 연산에도 사용 가능
# 고용일이 90-01-01부터 01-01-01사이인 모든 사원 조회
select *
from employee
where HIRE_DATE >= '90-01-01' and HIRE_DATE <= '01-01-01';

select *
from employee
where HIRE_DATE between '90-01-01' and '01-01-01';

# Like절
# like절에 지정한 패턴을 만족하는 컬럼값이면 true
# 컬럼명 like 패턴
# 패턴문자 : %, _
# % : 'A%' : A로 시작하는
#	  '%A' : A로 끝나는
#	  '%A%' : A가 포함된

# q. employee테이블에서 성이 이씨인 사원을 조회
select *
from employee
where EMP_NAME like '이%';

# q. employee테이블에서 이름에 이가 포함되고, 입사일이 01-01-01 이후인 사원의 이름 사번, 고용일 조회
select *
from employee
where (EMP_NAME like '%이%') 
and HIRE_DATE >= '01-01-01';

# q. employee 테이블에서 이름이 '연'으로 끝나고, 퇴사하지 않은 사원
select *
from employee
where (EMP_NAME like '%연') 
and ENT_YN = 'N';

# like절의 와일드카드
# _ 문자의 자리수를 지정
# _ -> 한자리, __ -> 두자리

# employee테이블에서 전화번호 뒤에서 4번째 자리가 9인 사원 이름 전화번호 조회
select *
from employee
where PHONE like '%7___';

# 이메일이 '_' 앞에 3글자가 존재하는 패턴의 이메일을 가진 사원의 정보 조회
# ex) aaa_b@naver.com
# 와일드카드 문자를 작성할때 escape문자를 등록할 수 있다.
# like '___$_%' escape '$'
# 해석 : 앞에 ___는 아무 문자나 와도 되고,
# 내가 등록한 escape기호인 $문자 이후의 _는 "_"그대로 문자로 대우를 받음

select *
from employee
where email like '__$_%' escape '$';

# in
# 직급코드가 'J7' 또는 'J2'인 직원 중 급여가 200만원 이상인 직원의 이름, 급여, 직급코드 조회
select *
from employee
where (JOB_CODE = 'J7' or JOB_CODE = 'J2')
and salary >= 2000000;

select *
from employee
where (JOB_CODE in ('J7','J2'))
and salary >= 2000000;

# null
# null : 미정, 정해지지 않아서 값이 없는거
# 연산이 가능하고, 대신 모든 산술연산의 결과는 null
# 미지수 + 10 = null
# 모든 비교연산의 결과는 null, 크기비교가 안되니까

# 근데 논리연산자(true, false)는 다름
# null and true : null
# null and false : false
# null or true : null
# null or false : null
select null and false;

select emp_name, salary, bonus, salary*12*(1+ifnull(bonus, 0)) as '실수령연봉'
from employee;

select *
from employee
where BONUS is null;