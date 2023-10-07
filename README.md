# Mini Porject 6 Design a complex SQL query for a MySQL database and explain the results.

# Project Description
I used AWS SDK and AWS CLI to operate in AWS Dynamodb
 
Create a table recording user info in AWS Dynamodb

<img width="1000" alt="image" src="https://github.com/nogibjj/IDS706_miniproject6_Mutian/assets/108935314/4a7ab4a5-04bb-43eb-8214-1bb13fc437fc">

Randomly generate 15 users info data and insert the data into the table

<img width="628" alt="image" src="https://github.com/nogibjj/IDS706_miniproject6_Mutian/assets/108935314/b33fbe04-e486-45ab-baa0-14bec06c6a7b">

The table structure

<img width="1877" alt="image" src="https://github.com/nogibjj/IDS706_miniproject6_Mutian/assets/108935314/e49ef2a7-5ced-4c5a-9009-64774c404138">

Complex Query. Because Aws Dynamodb is a NoSql database, it doesn't support complex query. I do the query in a python script to get the average age from users aged 30 or older.

<img width="772" alt="image" src="https://github.com/nogibjj/IDS706_miniproject6_Mutian/assets/108935314/f92df03b-1817-4ba8-a2cd-439e423c6e48">

Expected result: 44.5

<img width="328" alt="image" src="https://github.com/nogibjj/IDS706_miniproject6_Mutian/assets/108935314/d69fd51c-2063-4493-bb44-c02d2cdfe94e">

# Run
Makefile commands:

`make install`

`make format`

`make lint`

`make test`

`make createtable`

`make deletetable`

`make all`
