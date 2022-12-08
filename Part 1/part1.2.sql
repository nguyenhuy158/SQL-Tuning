-- Truong hop 2
SELECT o.OrderID,
    c.LastName,
    p.ProductID,
    p.Description,
    sd.ActualShipDate,
    sd.ShipStatus,
    sd.ExpectedShipDate
FROM Orders o
    INNER JOIN Item i ON i.OrderID = o.OrderID
    INNER JOIN Customer c ON c.CustomerID = o.CustomerID
    INNER JOIN ShipmentDetails sd ON sd.ShipmentID = i.ShipmentID
    INNER JOIN Product p ON p.ProductID = i.ProductID
    INNER JOIN Address a ON a.AddressID = sd.AddressID
WHERE c.LastName LIKE ISNULL(@LastName, '') || '%'
    AND c.FirstName LIKE ISNULL(@FirstName, '') || '%'
    AND o.OrderDate >= DATEADD(day, -30, CURRENT_TIMESTAMP)
    AND o.OrderStatus <> 'C';
-- isnull(variable, default) if variable is null get default
-- dateaddd(interval, number, date) +number intervarl into date
-- final
SELECT o.OrderID,
    c.LastName,
    p.ProductID,
    p.Description,
    sd.ActualShipDate,
    sd.ShipStatus,
    sd.ExpectedShipDate
FROM (
        SELECT o.OrderID,
            o.CustomerID
        FROM Orders o
        WHERE o.OrderDate >= DATEADD(day, -30, CURRENT_TIMESTAMP)
            AND o.OrderStatus <> 'C'
    ) oo
    JOIN (
        SELECT i.OrderID,
            i.ShipmentID,
            i.ProductID
        FROM Item i
    ) ii on oo.OrderID == ii.OrderID (
        SELECT c.CustomerID,
            c.LastName
        FROM Customer c
        WHERE c.LastName LIKE ISNULL(@LastName, '') || '%'
            AND c.FirstName LIKE ISNULL(@FirstName, '') || '%'
    ) cc on cc.CustomerID == oo.CustomerID
    join (
        SELECT sd.ShipmentID,
            sd.ActualShipDate,
            sd.ShipStatus,
            sd.ExpectedShipDate,
            sd.AddressID
        FROM ShipmentDetails sd
    ) ssdd on ssdd.ShipmentID == ii.ShipmentID
    join (
        SELECT p.ProductID,
            p.Description
        FROM Product p
    ) pp on pp.ProductID == ii.ProductID
    join (
        SELECT a.AddressID
        FROM Address a
    ) aa on aa.AddressID == sd.AddressID;