
															 /* Data Cleaning
															    By Purvarth Raj Chaudhary
															    IIT Guwahati */
															   



SELECT * FROM Project..Sheet1$




--Standardize date fromat

SELECT SaleDate, CONVERT(Date, SaleDate)
FROM Project..Sheet1$


ALTER TABLE Sheet1$
ADD SaleDateConverted Date;


UPDATE Sheet1$ SET SaleDateConverted = CONVERT(Date,SaleDate)

/*SELECT SaleDateConverted 
FROM Project..Sheet1$*/





--Populate Property Address data

SELECT PropertyAddress
FROM Project..Sheet1$


SELECT a.ParcelID, a.PropertyAddress, b.ParcelID, b.PropertyAddress 
, ISNULL(a.PropertyAddress, b.PropertyAddress)
FROM Project..Sheet1$ a
JOIN Project..Sheet1$ b
on a.ParcelID = b.ParcelID
and a.[UniqueID] <> b.[UniqueID]
WHERE a.PropertyAddress is NULL


UPDATE a
SET PropertyAddress = ISNULL(a.PropertyAddress, b.PropertyAddress)
FROM Project..Sheet1$ a
JOIN Project..Sheet1$ b
on a.ParcelID = b.ParcelID
and a.[UniqueID] <> b.[UniqueID]
WHERE a.PropertyAddress IS NULL


/*SELECT PropertyAddress from Sheet1$*/




--Breaking Address into Adress, City, State

SELECT PropertyAddress, 
SUBSTRING(PropertyAddress, 1, CHARINDEX(',', PropertyAddress)-1 ) as Address,
SUBSTRING(PropertyAddress, CHARINDEX(',', PropertyAddress)+1, LEN(PropertyAddress)) as City 
FROM Project..Sheet1$


--Address
ALTER TABLE Sheet1$
ADD PropertySplitAddress Nvarchar(255);

UPDATE Sheet1$
SET PropertySplitAddress = SUBSTRING(PropertyAddress, 1, CHARINDEX(',', PropertyAddress)-1 )


--City
ALTER TABLE Sheet1$
ADD PropertySplitCity Nvarchar(255);

UPDATE Sheet1$
SET PropertySplitCity = SUBSTRING(PropertyAddress, CHARINDEX(',', PropertyAddress)+1, LEN(PropertyAddress) )


SELECT * FROM Project..Sheet1$

/*ALTER TABLE Sheet1$
DROP column LocalAddress*/

--Select OwnerAddress FROM Project..Sheet1$


SELECT
OwnerAddress,
PARSENAME (REPLACE(OwnerAddress, ',','.'), 3),
PARSENAME (REPLACE(OwnerAddress, ',','.'), 2),
PARSENAME (REPLACE(OwnerAddress, ',','.'), 1)
FROM Project..Sheet1$


--Owner Address
ALTER TABLE Project..Sheet1$
ADD OwnerSplitAddress Nvarchar(255);

UPDATE Project..Sheet1$
SET OwnerSplitAddress = PARSENAME (REPLACE(OwnerAddress, ',','.'), 3)


--Owner City
ALTER TABLE Project..Sheet1$
ADD OwnerSplitCity Nvarchar(255);

UPDATE Project..Sheet1$
SET OwnerSplitCity = PARSENAME (REPLACE(OwnerAddress, ',','.'), 2)


--Owner State
ALTER TABLE Project..Sheet1$
ADD OwnerSplitState Nvarchar(255);

UPDATE Project..Sheet1$
SET OwnerSplitState = PARSENAME (REPLACE(OwnerAddress, ',','.'), 1)

SELECT * FROM Project..Sheet1$




-- Chnaging Y and N to Yes and No in SoldasVacant column

SELECT DISTINCT(SoldasVacant), COUNT(SoldasVacant) 
FROM Project..Sheet1$
GROUP BY SoldAsVacant


SELECT SoldasVacant,
CASE when SoldasVacant = 'Y' then 'Yes'
	 when SoldasVacant = 'N' then 'No'
	 ELSE SoldasVacant
	 END as SoldasVacant1
FROM Project..Sheet1$


UPDATE Project..Sheet1$
SET SoldasVacant = CASE when SoldasVacant = 'Y' then 'Yes'
				   when SoldasVacant = 'N' then 'No'
				   ELSE SoldasVacant
			       END 


SELECT SoldasVacant FROM Project..Sheet1$




--Removing Duplicates

WITH RowNumCTE AS(
SELECT *, ROW_NUMBER() OVER (
		 PARTITION by ParcelID,
					  PropertyAddress,
					  SaleDate,				--For identifying Duplicates
					  LegalReference
					  ORDER BY
						UniqueID
						) row_num
FROM Project..Sheet1$
--order by ParcelID
)
SELECT * FROM RowNumCTE
WHERE row_num > 1
ORDER by PropertyAddress




--Deleting unused columns

SELECT * FROM Project..Sheet1$

ALTER TABLE Project..Sheet1$
DROP column SaleDate, OwnerAddress, TaxDistrict, PropertyAddress