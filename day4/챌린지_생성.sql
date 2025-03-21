-- 1. 생성 (CREATE) - 25 문제(필수 : 초급 10문제 / 도전 : 중급 + 고급 15문제)

-- (1) **`customers`** 테이블에 새 고객을 추가하세요.
INSERT INTO customers(customerName, phone, address, country, email) VALUES ('세연', '010-1234-5678', '서울시', '대한민국', 'ert@gmail.com');

-- (2) **`products`** 테이블에 새 제품을 추가하세요.
INSERT INTO products(productName, productLine, productVendor, buyPrice) VALUES ('자동차장난감', '트럭', '토이', 20000);

-- (3) **`employees`** 테이블에 새 직원을 추가하세요.
INSERT INTO employees(employeesName, phone, address, country, position) VALUES ('윤지', '010-1235-1234', '서울시', '대한민국', 'PM');

-- (4) **`offices`** 테이블에 새 사무실을 추가하세요.
INSERT INTO offices(officesName, phone, address, country) VALUES ('대박부동산', '02-1234-5678', '서울시', '대한민국');

-- (5) **`orders`** 테이블에 새 주문을 추가하세요.
INSERT INTO orders(orderDate, shippedDate_status, customerNumber, productName) VALUES (NOW(), '상품준비중', 1, '자동차장난감');

-- (6) **`orderdetails`** 테이블에 주문 상세 정보를 추가하세요.
INSERT INTO orderdetails(orderNumber, productCode, quantityOrdered) VALUES (1, 'P001', 1);

-- (7) **`payments`** 테이블에 지불 정보를 추가하세요.
INSERT INTO payments(productName, checkNumber, paymentDate, amount) VALUES ('자동차장난감', '123456', NOW(), 10000);

-- (8) **`productlines`** 테이블에 제품 라인을 추가하세요.
INSERT INTO productlines(productLine,textDescription,htmlDescription,image) VALUES ('자동차장난감', '트럭 장난감', '<p>이 제품은 고급 자동차 장난감입니다.</p>', '/images/toy_car.jpg');

-- (9) **`customers`** 테이블에 다른 지역의 고객을 추가하세요.
INSERT INTO customers(customerName, phone, address, country) VALUES ('가연 ', '010-1234-5678', '인천시', '대한민국'); 

-- (10) **`products`** 테이블에 다른 카테고리의 제품을 추가하세요.
INSERT INTO products(productName, productLine, productVendor, buyPrice) VALUES ('캐릭터장난감', '하츄', '토이나라', 30000);