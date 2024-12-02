# 숫자타입
insert into tb_type(t_tinyint, t_smallint, t_mediumint, t_int, t_bigint)
values(100, 1000, 10000, 100000, 1000000);

select * from tb_type;

# 고정소수점, 부동소수점
# 고정소수점 : 정수부와 실수부의 자리수를 지정하는 방식 ex) 전체 자리수에서 소수점 자리수를 3자리로 고정 xxx.yyy
# 부동소수점 : float, double 실수연산 결과를 float과 double이 표현 가능한 실수부의 마지막 자리에서 올림처리하여 근사값으로 저장한다. xxx.yyyy, xxx.yy, ...
# decimal(precision, scale)
# precision : 전체 자리수, scale :  소수점 자리수

insert into tb_type(t_float, t_double) value(0.1, 112.0003);

# insert into tb_type(t_decimal) value(100.99); 는 에러다 
# decimal(5, 3)으로 전체 5자리, 소수점 3자리까지로 지정해놨는데 위에꺼는 넘는다.
insert into tb_type(t_decimal) value(90.99);