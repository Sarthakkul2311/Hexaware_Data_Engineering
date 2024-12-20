use pet_adoption;

CREATE TABLE SalesList
(SalesMonth NVARCHAR(20), SalesQuartes VARCHAR(5), SalesYear SMALLINT, SalesTotal MONEY);

INSERT INTO SalesList(SalesMonth,SalesQuartes,SalesYear,SalesTotal) VALUES (N'March','Q1',2019,60);
INSERT INTO SalesList(SalesMonth,SalesQuartes,SalesYear,SalesTotal) VALUES (N'March','Q1',2020,50);
INSERT INTO SalesList(SalesMonth,SalesQuartes,SalesYear,SalesTotal) VALUES (N'May','Q2',2019,30);
INSERT INTO SalesList(SalesMonth,SalesQuartes,SalesYear,SalesTotal) VALUES (N'July','Q3',2020,10);
INSERT INTO SalesList(SalesMonth,SalesQuartes,SalesYear,SalesTotal) VALUES (N'November','Q4',2019,120);
INSERT INTO SalesList(SalesMonth,SalesQuartes,SalesYear,SalesTotal) VALUES (N'October','Q4',2019,150);
INSERT INTO SalesList(SalesMonth,SalesQuartes,SalesYear,SalesTotal) VALUES (N'November','Q4',2019,180);
INSERT INTO SalesList(SalesMonth,SalesQuartes,SalesYear,SalesTotal) VALUES (N'November','Q4',2020,120);
INSERT INTO SalesList(SalesMonth,SalesQuartes,SalesYear,SalesTotal) VALUES (N'July','Q3',2019,160);
INSERT INTO SalesList(SalesMonth,SalesQuartes,SalesYear,SalesTotal) VALUES (N'March','Q1',2020,170);

select * from SalesList;

SELECT SalesYear, SUM(SalesTotal) AS SalesTotal FROM SalesList
GROUP BY ROLLUP(SalesYear);

SELECT SalesYear,SalesQuartes, SUM(SalesTotal) AS SalesTotal
FROM SalesList GROUP BY ROLLUP(SalesYear, SalesQuartes);

SELECT SalesYear,SalesQuartes,SalesMonth ,SUM(SalesTotal) AS SalesTotal
FROM SalesList GROUP BY ROLLUP(SalesYear, SalesQuartes, SalesMonth);

SELECT SalesYear,
SalesQuartes,
SUM(SalesTotal) AS SalesTotal ,
GROUPING(SalesQuartes) AS SalesQuarterGrp,
GROUPING(SalesYear) AS SYearGrp
FROM SalesList
GROUP BY ROLLUP(SalesYear, SalesQuartes);

SELECT CASE
WHEN GROUPING(SalesQuartes)=1 AND GROUPING(SalesYear)=0
THEN 'SubTotal'
WHEN GROUPING(SalesQuartes)=1 AND GROUPING(SalesYear)=1
THEN 'Grand Total'
ELSE CAST(SalesYear AS varchar(10))
END AS SalesYear,
SalesQuartes,
SUM(SalesTotal) AS SalesTotal
FROM SalesList
GROUP BY ROLLUP(SalesYear,SalesQuartes);

SELECT SalesMonth,SalesTotal ,
ROW_NUMBER() OVER(ORDER BY NEWID()) AS RowNumber FROM SalesList;

WITH CTE AS (
SELECT SalesMonth,SalesTotal ,
ROW_NUMBER() OVER(ORDER BY NEWID())
AS RowNumber FROM SalesList
)
SELECT RowNumber ,SalesMonth,SUM(SalesTotal) AS SalesTotal
FROM CTE
GROUP BY ROLLUP(SalesMonth, RowNumber);

WITH CTE AS (
SELECT SalesMonth,SalesTotal ,
ROW_NUMBER() OVER(ORDER BY NEWID())
AS RowNumber FROM SalesList
)
SELECT CASE WHEN GROUPING(RowNumber) =1 THEN 'SubTotal'
ELSE SalesMonth
END AS SalesMonth,SUM(SalesTotal) AS SalesTotal
FROM CTE
GROUP BY ROLLUP(SalesMonth, RowNumber);

WITH CTE AS (
    SELECT SalesMonth, SalesTotal,
           ROW_NUMBER() OVER(ORDER BY NEWID()) AS RowNumber
    FROM SalesList
)
SELECT SalesMonth,
    SUM(SalesTotal) AS SalesTotal
FROM CTE
GROUP BY SalesMonth;

SELECT NULL AS SalesQuarter, SalesMonth,
SUM(SalesTotal) AS SalesTotal
FROM SalesList
GROUP BY SalesMonth
UNION ALL
SELECT SalesQuartes, NULL AS SalesMonth,
SUM(SalesTotal) AS SalesTotal
FROM SalesList
GROUP BY SalesQuartes;

SELECT
SalesQuartes,SalesMonth ,
SUM(SalesTotal) AS SalesTotal
FROM SalesList
GROUP BY GROUPING SETS(SalesQuartes,SalesMonth);

SELECT CASE
WHEN GROUPING(SalesQuartes)=1 AND GROUPING(SalesYear)=0
THEN 'SubTotal'
WHEN GROUPING(SalesQuartes)=1 AND GROUPING(SalesYear)=1
THEN 'Grand Total'
ELSE CAST(SalesYear AS varchar(10))
END AS SalesYear,
SalesQuartes,
SUM(SalesTotal) AS SalesTotal
FROM SalesList
GROUP BY GROUPING SETS(SalesYear,(SalesYear,SalesQuartes),());