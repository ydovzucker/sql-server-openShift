PS C:\Users\ydovz> oc new-app docker.io/library/mysql:8.0 -e MYSQL_ROOT_PASSWORD=123456 -e MYSQL_DATABASE=mydb
oc get pods
oc rsh mysql-1-mphgp
CREATE TABLE table_name (id INT,first_name VARCHAR(100),last_name VARCHAR(100));
INSERT INTO table_name (id,first_name, last_name) VALUES  (101, 'Alice', 'Johnson'), (102, 'Charlie', 'Brown'), (103,'Dave','White') ,(104,'Callum','Scot');
docker build -t my-web-app:1.0 .