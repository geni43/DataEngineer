Queries below are tested using PostgreSQL


1. Provide a script in a `scripts/` directory to load the CSV data into database table(s) of your own design.
             Execute Scipts in 'Design and Load.SQL'  to load the CSV data into PostgreSQL database


2. Provide SQL scripts in a `scripts/` directory to achieve the following:

             Execute Scripts in the "tasks.sql" .Look for the tagname as Q* (*: tasknumber Q1,Q2,Q3...) to acheive the below tasks

    Q1- List the Sales Team name, Gross Revenue and Net Revenue of the latest ordered campaigns by Sales Team.
    Q2- List the Sales Team name, Gross Revenue, Net Revenue, and Margin Revenue of the latest ordered campaigns by Sales Team.
    Q3- List all Sales Person names from the salesperson table with his/her Gross Revenue, Net Revenue, and Margin Revenue of the latest ordered campaigns.
    Q4- List the Sales Persons name who had more than 3 Campaigns assigned to them.
    Q5- List the top 5 sellers in 2015 based on the Net Revenue.
    Q6- List the Top Seller in each Sales Team who exceeded $100,000 Gross Revenue.
    Q7- List the Year, Quarter, Month, Sales team name, Sales Person name, Gross Revenue, Net Revenue and Margin Revenue of the latest ordered campaigns by Year, Quarter, Month, Sales Team, and Sales Person. The Year, Quarter and Month are based on the Plan Ordered At of the lasted ordered campaigns.
    Q8- List the Sales team name, Sales Manager name, Gross Revenue and Net Revenue of the latest ordered campaigns by Sales team and Sales Manager.
    Q9- List the Sales VP name, Sales VP Gross Revenue, Sales VP Net Revenue, Sales Director Name, Sales Director Gross Revenue, Sales Director Net Revenue, Sales Manager name, Sales Manager Gross Revenue, Sales Manager Net Revenue of the latest ordered campaigns. The Gross Revenue and Net revenue should include all the revenue numbers from all salespeople who report to them.
	
	
	
3. (BONUS ARCHITECTURE QUESTION) Provide a prose answer (on the order of a few paragraphs) in your `DESIGN.md` file for the following:
    - Imagine this problem scaled up to a large business working with terabytes to petabytes of information.  Would your solution be different?  What kinds of performance issues would you consider?  What overall architectural concerns would you have?  How might you structure a team around this kind of work?  Be creative!
	
	         Answer :  Yes, I will reconsider my approaches if the problem is scaled up to terabytes to petabytes of information.
			           
					   If you observe the queries ,there are lot of joins between the two tables , Main thing we need to consider is the indexing. We should assign the proper clustered index and non clustered indexes for the table.
					   
					   Temp memory should be considered ,and it will be good if we clear the temp memeory when we step from one query to the other ,this is one of the concern which developer wont realize when the query is not responding after executing for hours.
			 
			           Another good approach to use the nosql databases and using the Hadoop processing for better peeformance.