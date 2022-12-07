use smqa;

CREATE TABLE EMPLOYEE (
    `empID` VARCHAR(255) PRIMARY KEY,
    `empName` VARCHAR(255) NOT NULL,
    `empType` VARCHAR(255) NOT NULL
);

CREATE TABLE MENU (
    `itemID` VARCHAR(255) PRIMARY KEY,
    `itemName` VARCHAR(255) NOT NULL,
    `itemPrice` INT NOT NULL,
    `itemType` VARCHAR(255) NOT NULL
);


CREATE TABLE TABLES (
    `tableID` VARCHAR(255) PRIMARY KEY,
    `available` BOOLEAN DEFAULT TRUE,
    `empID` VARCHAR(255) NOT NULL,
    `quantity` INT NOT NULL DEFAULT 1,
    `seats` INT,
    FOREIGN KEY (empID) REFERENCES EMPLOYEE(empID)
);

CREATE TABLE WAITER (
    `waiterID` VARCHAR(255) PRIMARY KEY,
    `empID` VARCHAR(255) NOT NULL UNIQUE,
    FOREIGN KEY (empID) REFERENCES EMPLOYEE(empID)
);

CREATE TABLE CHEF (
    `chefID` VARCHAR(255) PRIMARY KEY,
    `empID` VARCHAR(255) NOT NULL UNIQUE,
    FOREIGN KEY (empID) REFERENCES EMPLOYEE(empID)
);

CREATE TABLE ORDERS (
    `orderID` VARCHAR(255) PRIMARY KEY,
    `itemID` VARCHAR(255) NOT NULL,
    `tableID` VARCHAR(255) NOT NULL,
    `waiterID` VARCHAR(255) NOT NULL,
    FOREIGN KEY (tableID) REFERENCES TABLES(tableID)
);

CREATE TABLE BILL (
    `billID` VARCHAR(255) PRIMARY KEY,
    `orderID` VARCHAR(255) NOT NULL,
    `tableID` VARCHAR(255) NOT NULL,
    FOREIGN KEY (tableID) REFERENCES TABLES(tableID),
    FOREIGN KEY (orderID) REFERENCES ORDERS(orderID)
);


alter table smqa.orders drop constraint orders_ibfk_1;
alter table smqa.orders 
drop column tableID;

alter table smqa.orders 
add constraint fk_itemID
foreign key(itemID) references menu(itemID);

alter table orders drop column waiterID;

alter table orders add column empID varchar(255), add constraint fk_constraint2 foreign key(empID) references employee(empID);

alter table orders add column quantity int;

alter table bill
add column custID varchar(255),
add constraint fk_custID
foreign key(custID) references customer(custID);
alter table bill drop constraint bill_ibfk_2;
alter table bill drop column orderID;
alter table bill add column total int;
alter table bill drop constraint bill_ibfk_1;
alter table bill  drop column tableID;
alter table tables drop column quantity;
alter table tables drop column seats;
alter table tables add column customer varchar(255),
add constraint fk_customer 
foreign key(custID) references customer(custID);

