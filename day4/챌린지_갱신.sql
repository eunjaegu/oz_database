-- 3. 갱신 (UPDATE) - 25 문제(필수 : 초급 10문제 / 도전 : 중급 + 고급 15문제)

-- (1) **`customers`** 테이블에서 특정 고객의 주소를 갱신하세요.
UPDATE customers SET address = '인천시' WHERE customerID = 1;

-- (2) **`products`** 테이블에서 특정 제품의 가격을 갱신하세요.
UPDATE products SET buyPrice = 50000 WHERE productID = '자동차장난감';

-- (3) **`employees`** 테이블에서 특정 직원의 직급을 갱신하세요.
UPDATE employees SET position = 'Backend' WHERE employeesID = 1;

-- (4) **`offices`** 테이블에서 특정 사무실의 전화번호를 갱신하세요.
UPDATE offices SET phone = '02-9999-8888' WHERE officesID = 1;

-- (5) **`orders`** 테이블에서 특정 주문의 상태를 갱신하세요.
UPDATE orders SET shippedDate_status = '배송중' WHERE ordersID = 1;

-- (6) **`orderdetails`** 테이블에서 특정 주문 상세의 수량을 갱신하세요.
UPDATE orderdetails SET quantityOrdered = '5' WHERE orderdetailsID = 1;

-- (7) **`payments`** 테이블에서 특정 지불의 금액을 갱신하세요.
UPDATE payments SET amount = 50000 WHERE paymentsID = 1;

-- (8) **`productlines`** 테이블에서 특정 제품 라인의 설명을 갱신하세요.
UPDATE productlines SET textDescription = '소형트럭장난감' WHERE productlinesID = 1;

-- (9) **`customers`** 테이블에서 특정 고객의 이메일을 갱신하세요.
UPDATE customers SET email = 'qwe@gmail.com' WHERE customerID = 1;

-- (10) **`products`** 테이블에서 여러 제품의 가격을 한 번에 갱신하세요.
UPDATE products SET buyPrice = 50000;
