# DDL : data definition language
# type
create table tb_type(
	# 정수형
	# t_tinyint 1byte
    t_tinyint tinyint,
    # smallint 2byte
    t_smallint smallint,
    # mediumint 3byte
    t_mediumint mediumint,
    # int 4byte
    t_int int,
    # bigint 8byte
    t_bigint bigint,
    
    # 실수형
    # float 4byte
    t_float float,
    # double 8byte
    t_double double,
    # decimal 타입 + 1byte
    t_decimal decimal(5, 3),
    
    # 논리형 1byte, tinyint
    t_bool bool,
    
    # 문자형
    # char : 고정길이데이터, 255byte
    t_char char(10), # 10글자형태의 데이터이다. 5글자를 채우더라도 뒤에 공백을 채워서 10글자로 맞춰버림
    # varchar : 가변길이데이터, 65535byte
    t_varchar varchar(100), # 최대 길이가 100글자까지
    # text : 대량의 텍스트를 '저장'하는 용도, 탐색 속도가 많이 느림
    # tinytext(255), text(65535), mediumtext(16,777,215), longtext(4,294,967,295)
    t_mediumtext mediumtext,
    
    # 날짜
    # date : 연월일
    # time : 시분초
    # datetime : 연월일시분초
    # timestamp : 연월일시분초
    t_date date,
    t_time time,
    t_datetime datetime,
    t_timestamp timestamp
);