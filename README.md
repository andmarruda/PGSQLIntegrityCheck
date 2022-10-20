## PGSQLIntegrityCheck

I'm building this library in Python because i needed to migrate a huge database with more than 50Gb and i have to check if missing any information.
This is the basic version, in the future i want to improve this.

Is quitly easy to use as you can see in almost examples.
Today has these functionalties:

| Function Name | Description |
| ------------- | ----------- |
| missingView | Check if missing view in any side, left or right |
| missingMaterializedView | Check if missing materialized view in any side, left or right |
| missingTables | Check if missing ordinary table, toast table, partitioned table or foreign table in any size, left or right |
| searchNotMatchRows | Check if ordinary table or materiazlied view has the same number of rows. More detailed return |

You can see all examples in example directory.

Thanks everyone to see and share this.
See you all soon.
