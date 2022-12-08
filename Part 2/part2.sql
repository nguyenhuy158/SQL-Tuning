-- method 1 is Compatibility Views
SELECT *
FROM sys.sysdatabases;
SELECT *
FROM dbo.sysdatabases;
-- method 2 is Catalog Views
SELECT *
FROM sys.databases;
-- 
SELECT COUNT(*)
FROM INFORMATION_SCHEMA.COLUMNS
WHERE table_catalog = 'database_name'
    AND table_name = 'table_name';
--
sys.sysobjects trong compatibility view thành sys.objects trong catalog view sys.sysindexes trong compatibility view thành sys.indexes trong catalog view …;
-- 
-- 
-- 
SELECT wait_type,
    SUM(wait_time_ms / 1000) AS [wait_time_s]
FROM sys.dm_os_wait_stats DOWS
WHERE wait_type NOT IN (
        'SLEEP_TASK',
        'BROKER_TASK_STOP',
        'SQLTRACE_BUFFER_FLUSH',
        'CLR_AUTO_EVENT',
        'CLR_MANUAL_EVENT',
        'LAZYWRITER_SLEEP'
    )
GROUP BY wait_type
ORDER BY SUM(wait_time_ms) DESC -- 
    -- 
    -- 
SELECT DB_NAME(mf.database_id) AS databaseName,
    mf.physical_name,
    divfs.num_of_reads,
    --other columns removed in this section. See Listing 6.14 for complete code
    GETDATE() AS baselineDate INTO #baseline
FROM sys.dm_io_virtual_file_stats(NULL, NULL) AS divfs
    JOIN sys.master_files AS mf ON mf.database_id = divfs.database_id
    AND mf.file_id = divfs.file_id;
-- 
-- 
--
WITH currentLine AS (
    SELECT DB_NAME(mf.database_id) AS databaseName,
        mf.physical_name,
        num_of_reads,
        --other columms removed
        GETDATE() AS currentlineDate
    FROM sys.dm_io_virtual_file_stats(NULL, NULL) AS divfs
        JOIN sys.master_files AS mf ON mf.database_id = divfs.database_id
        AND mf.file_id = divfs.file_id
)
SELECT currentLine.databaseName,
    currentLine.physical_name,
    --gets the time difference in milliseconds since the baseline was taken
    DATEDIFF(millisecond, baseLineDate, currentLineDate) AS elapsed_ms,
    --gets the change in time since the baseline was taken
    currentLine.num_of_reads - #baseline.num_of_reads AS num_of_reads
    --other columns removed
FROM currentLine
    INNER JOIN #baseline ON #baseLine.databaseName = currentLine.databaseName
    AND #baseLine.physical_name = currentLine.physical_name