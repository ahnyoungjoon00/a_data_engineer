# 테이블 수정

# 테이블 이름 변경
alter table ddl_emp rename to ddl_employee;

alter table ddl_employee rename to ddl_emp;

# 테이블 컬럼명 변경
# alter table 테이블명 add | modify | drop 컬럼명;

# 테이블 컬럼 추가
alter table ddl_emp add(job_code char(3));

# 테이블 컬럼 수정
# 테이블 수정할때는, 데이터와 충돌하지 않는 방향으로만 변경 가능하다.

# 1. 데이터가 존재한다면 컬럼의 타입은 변경할 수 없다. 데이터 없으면 가능
# alter table ddl_emp modify emp_name int;

# 2. 데이터가 존재한다면 컬럼의 크기는 기존보다 큰값으로만 변경 가능하다.
# Error Code: 1265. Data truncated for column 'emp_name' at row 1
alter table ddl_emp modify emp_name VARCHAR(100);

# 3. 컬럼에 이미 null인 데이터가 존재한다면, not null은 걸 수 없다.
# Error Code: 1138. Invalid use of NULL value
alter table ddl_emp modify job_code char(3) not null;

# 컬럼에 중복값이 하나라도 존재한다면 unique 제약조건을 걸 수 없다.
alter table ddl_emp modify age int unique;

# 컬럼에 새롭게 설정할 check제약조건을 어기는 데이터가 하나라도 있다면 제약조건 불가
alter table ddl_emp modify age int check(age <3);

# 테이블 컬럼 이름 변경
# alter table ddl_emp add job_code char(3);
alter table ddl_emp rename column job_code to job;
# 테이블 컬럼 삭제
alter table ddl_emp drop job;

# 제약조건 추가 및 삭제
# 기본키 추가
alter table tb_type add primary key(t_tinyint);
alter table tb_type drop primary key;

# 제약조건 변경
# alter table 테이블명 add | drop 제약조건명
# 	on delete|update restrict: default, 부모테이블에서 자식테이블이 참조하고 잇는 행을 수정|삭제 불가
# 	on delete|update cascade: 자식테이블이 참조하고 잇는 행을 수정|삭제할 경우, 자식테이블의 행도 함께 삭제
#	on delete|update set null: 자식테이블이 참조하고 있는 행을 수정|삭제할 경우, 자식테이블의 외래키에 NULL을 넣어준다.
alter table ddl_emp drop constraint ddl_emp_ibfk_1;
alter table ddl_emp add constraint fk_ddl_emp
foreign key(dept_code) references ddl_dept(dept_code) on delete set null;


delete from ddl_dept where dept_code ='D01';
select * from ddl_dept;
select * from ddl_emp;
rollback;