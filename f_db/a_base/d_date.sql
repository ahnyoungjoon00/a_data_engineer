# 날짜
insert into tb_type(t_datetime, t_timestamp)
values('24-12-02 13:08:01', '24-12-02 13:08:01');
select * from tb_type;

# datetime과 timestamp의 차이
# timestamp는 dbms의 timezone을 참조한다. 
# 나중에 배포를 위해서는 timestamp를 쓰는게 옳다
set @@session.time_zone = '+01:00';
commit;
