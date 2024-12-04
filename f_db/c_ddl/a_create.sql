# 테이블 생성구문
# create
# create table 테이블명 (컬럼명 type [제약조건])

# 제약조건 : 데이터 무결성 보장을 위해 컬럼에 설정하는 조건
# 데이터 무결성 :
#	정확성 : 데이터가 중복되거나 누락되지 않은 상태
#	유효성 : 저장되는 데이터가 도메인의 범위에 포함되는 값인 상태
#   일관성 : 데이터가 수정되었을때, 그 수정이 연속적으로 보장

create table ddl_dept(
	dept_code char(3) primary key,
    dept_title varchar(50)
);
insert into ddl_dept(dept_code, dept_title) values('D01','개발팀');
insert into ddl_dept(dept_code, dept_title) values('D02','인사팀');
insert into ddl_dept(dept_code, dept_title) values('D03','기획팀');

select *
from ddl_dept;
commit;


# 조건
# primary key, foregin key
# unique값, check default, not null
create table ddl_emp(
	# primary key : 기본키
    # 테이블을 대표하고, 테이블의 각 행을 식별하기 위해 사용하는 키
    # 기본키로 지정된 컬럼은 중복값을 허용하지 않는다.
    # 기본키로 지정된 컬럼은 null을 허용하지 않는다.
	#	식별자로 사용할 수 있는 단일컬럼 또는 컬럼집합을 슈퍼키
    # 	슈퍼키 중에서 식별자로 사용할 수 있는 최소한의 컬럼집합을 후보키
    # 	후보키 중에서 테이블에 대한 대표성을 지닌 컬럼을 기본키로 지정
    # 모든 테이블에 반드시 기본키를 지정해야함
    # 만약에 식별할 수 있는 키도 없고, 대표성이 있는 키도 없다면 인위적으로 생성해서라도 지정해야함
	# 인위적인 키를 만들 때는 100부터 1씩 증가하는 코드번호, 문자열로 유니크값을 생성하는 uuid를 사용
	
    # auto_increment : 0부터 순차적으로 1씩 증가하는 값을 저장
    emp_id int auto_increment primary key,
    
    # not null : 컬럼에 null을 허용하지 않음
    emp_name varchar(50) not null,
    
    # check : 도메인 무결성 보장
    age int check(age >= 0),
    
    # unique : 중복값 허용하지 않음
    emp_no char(15) unique,
    
    # default : 컬럼값이 존재하지 않으면 default에 정의한 값 세팅
    hire_date timestamp default now(),
    
    # 참조무결성
    # 외래키는 부모테이블(ddl_dept)에서 유일성고 최소성(not null)을 만족하는 컬럼을 사용하는 것이 좋다.
    dept_code char(3),
    foreign key(dept_code) references ddl_dept(dept_code)
);

# 기본키에 null 넣기 == Error Code: 1364. Field 'emp_id' doesn't have a default value
-- insert into ddl_emp(emp_name, age, emp_no, dept_code)
-- values('ayj', 12, '000000-1111111', 'D01');

insert into ddl_emp(emp_id, emp_name, age, emp_no, dept_code)
values(0, 'ayj', 12, '000000-1111111', 'D01');

# 기본키에 중복된 0값을 넣기 == Error Code: 1062. Duplicate entry '0' for key 'ddl_emp.PRIMARY'
insert into ddl_emp(emp_id, emp_name, age, emp_no, dept_code)
values(0, 'chj', 15, '000000-2222222', 'D02');

# 중복되지 않은 값 넣기 or idx역할로 만들어놓은 것이라면 table생성시 auto_increment 설정
insert into ddl_emp(emp_id, emp_name, age, emp_no, dept_code)
values(1, 'chj', 15, '000000-2222222', 'D02');
insert into ddl_emp(emp_name, age, emp_no, dept_code)
values('csh', 18, '000000-3333333', 'D01');

# null 제약조건 == Error Code: 1048. Column 'emp_name' cannot be null
-- insert into ddl_emp(emp_name, age, emp_no, dept_code)
-- values(null, 18, '000000-3333333', 'D01');

# check 제약조건 == Error Code: 3819. Check constraint 'ddl_emp_chk_1' is violated. (이걸로는 문제가 뭔지 모르니까 table inspect가서 봐야함)
# check에 지정한 조건식이 false가 되는 값을 넣을 수 없다.
insert into ddl_emp(emp_name, age, emp_no, dept_code)
values('매니저', 22, '000000-4444444', 'D01');

# unique 제약조건 == Error Code: 1062. Duplicate entry '000000-4444444' for key 'ddl_emp.emp_no'
insert into ddl_emp(emp_name, age, emp_no, dept_code)
values('sch', 24, '000000-5555555', 'D01');

# 외래키 제약조건1
# 주 키인 컬럼에 존재하지 않는 값을 자식 테이블의 외래키 컬럼에 넣을 수 없다.
# == Error Code: 1452. Cannot add or update a child row: a foreign key constraint fails 
# (`study`.`ddl_emp`, CONSTRAINT `ddl_emp_ibfk_1` FOREIGN KEY (`dept_code`) REFERENCES `ddl_dept` (`dept_code`))
insert into ddl_emp(emp_name, age, emp_no, dept_code)
values('scl', 28, '000000-6666666', 'D11');

insert into ddl_emp(emp_name, age, emp_no, dept_code)
values('scl', 28, '000000-6666666', 'D01'); 

# 외래키 제약조건2
# 자식테이블에서 참조하고 잇는 행을 삭제할 수 없다.
# == Error Code: 1451. Cannot delete or update a parent row: 
# a foreign key constraint fails (`study`.`ddl_emp`, CONSTRAINT `ddl_emp_ibfk_1` FOREIGN KEY (`dept_code`) REFERENCES `ddl_dept` (`dept_code`))

# 만약 자식테이블이 참조하고 잇는 부모테이블의 행을 삭제, 수정할 경우, 자식테이블 외래키컬럼값이 무의미해진다.
delete from ddl_dept where dept_code= 'D01';
update ddl_dept set dept_code= 'D12' where dept_code = 'D01';

update ddl_dept set dept_title= '데이터분석팀' where dept_code = 'D01';

select *
from ddl_dept;


