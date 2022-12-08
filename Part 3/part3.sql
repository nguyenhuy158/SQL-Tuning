--yêu cầu 
--tên của sản phẩm, 
--nhà sản xuất,
--id đơn hàng
--tên của nhân viên,
--các đơn đặc hàng nằm trong ngày bao nhiêu tới bao nhiêu 
--và giảm giá > 0.15
--ProductName, s.CompanyName, o.OrderID, LastName + ' ' + FirstName
--ProductName, s.CompanyName, o.OrderID, LastName + ' ' + FirstName
--ProductName, s.CompanyName, o.OrderID, LastName + ' ' + FirstName
SELECT *
FROM Orders o
	FULL JOIN [Order Details] od ON o.OrderID = od.OrderID
	FULL JOIN Products p ON od.ProductID = p.ProductID
	FULL JOIN Employees e ON o.EmployeeID = e.EmployeeID
	FULL JOIN Customers c ON o.CustomerID = c.CustomerID
	FULL JOIN Suppliers s ON s.SupplierID = p.SupplierID
WHERE DATEDIFF(yy, OrderDate, getdate()) >= 26
	AND Discount >= 0.15
	AND (
		UPPER(s.CompanyName) LIKE '%H%'
		OR UPPER(s.CompanyName) LIKE '%U%'
		OR UPPER(s.CompanyName) LIKE '%Y%'
	);
-- 
-- UNION ALL
SELECT p.ProductName,
	s.CompanyName,
	o.OrderID,
	e.LastName + ' ' + e.FirstName
FROM (
		SELECT OrderID,
			EmployeeID,
			CustomerID
		FROM Orders
		WHERE OrderDate <= DATEADD(yy, -26, GETDATE())
	) o
	INNER JOIN (
		SELECT OrderID,
			ProductID
		FROM [Order Details]
		WHERE Discount >= 0.15
	) od ON o.OrderID = od.OrderID
	INNER JOIN (
		SELECT ProductName,
			ProductID,
			SupplierID
		FROM Products
	) p ON od.ProductID = p.ProductID
	INNER JOIN (
		SELECT EmployeeID,
			LastName,
			FirstName
		FROM Employees
	) e ON o.EmployeeID = e.EmployeeID
	INNER JOIN (
		SELECT CustomerID
		FROM Customers
	) c ON o.CustomerID = c.CustomerID
	INNER JOIN (
		SELECT CompanyName,
			SupplierID
		FROM Suppliers
		WHERE UPPER(CompanyName) LIKE '%H%'
			OR UPPER(CompanyName) LIKE '%U%'
			OR UPPER(CompanyName) LIKE '%Y%'
	) s ON s.SupplierID = p.SupplierID