# DML (data manipulate language) : 데이터 조작어
# C U D

# 인턴 직급을 추가해보자
insert into job(job_code, job_name) values('J8', '인턴');

create table emp_dept(
	emp_id varchar(3),
    emp_name varchar(50),
    dept_title varchar(50)
);

# 퇴사하지 않은 사원의 사번, 이름, 부서명을 emp_dept 테이블에 추가
insert into emp_dept(
	select emp_id, emp_name, dept_title
    from employee e
    join department d on(e.dept_code=d.dept_id)
    where ent_yn ='N');
    
create view emp_hiredate as
	(select emp_id, emp_name, hire_date
	from employee);
    
select *
from emp_hiredate;

insert into emp_dept(emp_id, emp_name, dept_title)
values('900', 'kjy', '개발팀'),
('901', 'ljo', '개발팀');

# update
# where절이 없으면 테이블의 모든행이 수정
# 반드시 where절을 작성해서 수정하고자 하는 범위의 데이터만 수정해야한다.
SET SQL_SAFE_UPDATES = 0;
update emp_dept
set dept_title = concat('멋진', dept_title)
where emp_id = '900';
SET SQL_SAFE_UPDATES = 1;

delete from emp_dept 
where emp_id = '900';

# delete 보다 빠름
# rollback이 안된다
truncate emp_dept;


select *
from emp_dept;

##############################################################################################
# TCL (transaction control languate)
# transaction : 논리적 최소작업단위
# ex) a계좌 -> b계좌로 5만원입금
#	  a계좌에서 balance 컬럼 5만원 차감 update
#	  b계좌에서 balance 컬럼 5만원 증가 update

# 계좌이체 전 상태 (이전 commit 상태)
# a잔고만 차감된 상태
# b잔고만 증가된 상태
commit;

# DML로 테이블 상태로 변경
update emp_dept
set dept_title = ''
where emp_id = '900';

select * from emp_dept where emp_id = '900';

# rollback을 통해 예전에 기억해둔 테이블 상태로 되돌림
rollback;