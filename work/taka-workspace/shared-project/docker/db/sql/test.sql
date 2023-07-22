DROP schema public cascade;create schema public;
CREATE TABLE test (
    id VARCHAR(50) PRIMARY KEY,
    name VARCHAR(50),
    password VARCHAR(50)
);
INSERT INTO test (id, name, password) VALUES
    ('1', 'testA', 'test1'),
    ('2', 'testB', 'test2'),
    ('3', 'testC', 'test3');
select * from test;