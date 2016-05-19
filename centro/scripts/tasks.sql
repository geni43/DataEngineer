--Q1- List the Sales Team name, Gross Revenue and Net Revenue of the latest ordered campaigns by Sales Team.

SELECT Min(b.sales_team_name) as TeamName,SUM(a.gross_revenue) as GrossRevenue,SUM(a.net_revenue) as NetRevenue from sample_campaigns a
inner join sample_salesperson b on a.salesperson_id=b.salesperson_id 
where a.is_last_ordered_campaign='t' group by b.sales_team_name order by 1;


--Q2- List the Sales Team name, Gross Revenue, Net Revenue, and Margin Revenue of the latest ordered campaigns by Sales Team.


SELECT Min(b.sales_team_name) as TeamName,SUM(a.gross_revenue) as GrossRevenue,SUM(a.net_revenue) as NetRevenue ,SUM(a.gross_revenue/a.net_revenue) as MarginPercentage from sample_campaigns a
inner join sample_salesperson b on a.salesperson_id=b.salesperson_id 
where a.is_last_ordered_campaign='t' group by b.sales_team_name order by 1;

--Q3- List all Sales Person names from the salesperson table with his/her Gross Revenue, Net Revenue, and Margin Revenue of the latest ordered campaigns.

SELECT b.salesperson_name as SalesPersonName,a.gross_revenue as GrossRevenue,a.net_revenue as NetRevenue ,a.gross_revenue/a.net_revenue as Margin from sample_campaigns a
inner join sample_salesperson b on a.salesperson_id=b.salesperson_id 
where a.is_last_ordered_campaign='t' ;

--Q4- List the Sales Persons name who had more than 3 Campaigns assigned to them.


SELECT MIN(b.salesperson_name) as SalesPersonName from sample_campaigns a
inner join sample_salesperson b on a.salesperson_id=b.salesperson_id group by b.salesperson_name having count(b.salesperson_name) >3 

--Q5- List the top 5 sellers in 2015 based on the Net Revenue.

SELECT SalesPersonName from (
SELECT b.salesperson_name as SalesPersonName,SUM(COALESCE(a.net_revenue,0)) as NetRevenue  from sample_campaigns a
inner join sample_salesperson b on a.salesperson_id=b.salesperson_id where EXTRACT(YEAR from a.campaign_start_date)=2015 group by b.salesperson_name order by 2 DESC)S LIMIT 5

--Q6- List the Top Seller in each Sales Team who exceeded $100,000 Gross Revenue.

WITH topseller AS(
Select SalesPersonName,SalesTeamName,GrossRevenue, rank() OVER(PARTITION BY SalesTeamName order by GrossRevenue DESC ) AS rk from (

SELECT b.salesperson_name as SalesPersonName,b.sales_team_name as SalesTeamName,SUM(a.gross_revenue) as GrossRevenue
from sample_campaigns a inner join sample_salesperson b on a.salesperson_id=b.salesperson_id 
group by b.salesperson_name,b.sales_team_name) S  where GrossRevenue >100000.0 )

Select s.SalesPersonName,s.SalesTeamName from topseller s where s.rk=1


--Q7- List the Year, Quarter, Month, Sales team name, Sales Person name, Gross Revenue, Net Revenue and Margin Revenue of the latest ordered campaigns by Year, Quarter, Month, Sales Team, and Sales Person. The Year, Quarter and Month are based on the Plan Ordered At of the lasted ordered campaigns.

Select EXTRACT(YEAR from a.campaign_ordered_at) as CompaignYear,EXTRACT(QUARTER from a.campaign_ordered_at) as CompaignQuarter,
         EXTRACT(MONTH from a.campaign_ordered_at) as CompaignMonth,b.salesperson_name as SalesPersonName,b.sales_team_name as SalesTeamName,
         a.gross_revenue as GrossRevenue,a.net_revenue as NetRevenue ,a.gross_revenue/a.net_revenue as Margin 
         from sample_campaigns a inner join sample_salesperson b on a.salesperson_id=b.salesperson_id where a.is_last_ordered_campaign='t' 
         ORDER BY CompaignYear,CompaignQuarter,CompaignMonth,SalesTeamName,SalesPersonName ;


--Q8- List the Sales team name, Sales Manager name, Gross Revenue and Net Revenue of the latest ordered campaigns by Sales team and Sales Manager

 SELECT b.sales_team_name as SalesTeamName,b.sales_manager_name as SalesMgrName ,SUM(a.gross_revenue) as GrossRevenue,SUM(a.net_revenue) as NetRevenue
   from sample_campaigns a inner join sample_salesperson b on a.salesperson_id=b.salesperson_id where b.sales_manager_name IS NOT NULL group by b.sales_team_name, SalesMgrName order by 1


--Q9- List the Sales VP name, Sales VP Gross Revenue, Sales VP Net Revenue, Sales Director Name, Sales Director Gross Revenue, Sales Director Net Revenue, Sales Manager name, Sales Manager Gross Revenue, Sales Manager Net Revenue of the latest ordered campaigns. The Gross Revenue and Net revenue should include all the revenue numbers from all salespeople who report to them.


WITH VP AS(
SELECT MIN(b.sales_vp_name) as vpname,SUM(a.gross_revenue) as VPGrossRevenue,SUM(a.net_revenue) as VPNetRevenue  from sample_campaigns a
inner join sample_salesperson b on a.salesperson_id=b.salesperson_id 
group by b.sales_vp_name order by 1),


director AS(

SELECT MIN(b.sales_director_name) as sales_director_name ,SUM(a.gross_revenue) as GrossRevenue,SUM(a.net_revenue) as NetRevenue ,
MIN(b.sales_vp_name) as vpname from sample_campaigns a
inner join sample_salesperson b on a.salesperson_id=b.salesperson_id 
where a.is_last_ordered_campaign='t' group by b.sales_director_name order by 1),

manager AS(
SELECT b.sales_manager_name as sales_manager_name,SUM(a.gross_revenue) as GrossRevenue,SUM(a.net_revenue) as NetRevenue 
,b.sales_director_name as sales_director_name ,b.sales_vp_name AS sales_vp_name
from sample_campaigns a inner join sample_salesperson b on a.salesperson_id=b.salesperson_id 
where a.is_last_ordered_campaign='t' group by sales_manager_name,sales_director_name,sales_vp_name)

 Select VP.vpname,VP.VPGrossRevenue,VP.VPNetRevenue,director.sales_director_name,director.GrossRevenue,director.NetRevenue,
        manager.sales_manager_name,manager.GrossRevenue,manager.NetRevenue from VP inner join director on VP.vpname=director.vpname 
        Inner Join manager 
        on manager.sales_director_name=director.sales_director_name ;
