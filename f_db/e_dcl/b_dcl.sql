# dcl
# 1. 계정 생성
create user dcl identified by '123qwe!@#';
create user dcl_dev identified by '123qwe!@#';

show grants for dcl;

# 2. 계정 삭제
drop user 'dcl_dev';

# 3. 권한 부여
# grant 권한 [권한, ... ] on db명.table명(*) to 사용자명 [with grant option]
grant select, insert on study.* to 'dcl';
# 4. 권한 회수
revoke select, insert on study.* from 'dcl';

# 5. role : 역할에 필요한 권한을 하나의 이름으로 묶음
create role 'role_dev';
show grants for 'role_dev';

grant select, insert, update, delete on study.* to 'role_dev';

# role에ㅐ 저장한 권한을 사용자에게 부여
grant 'role_dev' to 'dcl';
set default role 'role_dev' to 'dcl';

revoke 'role_dev' from 'dcl';