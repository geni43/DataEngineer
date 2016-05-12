# Database Management Exercise

Centro’s core business is the planning and management of display advertisements on the web.
This exercise uses examples from our day-to-day business to exercise your data management skills.

## Instructions

You should have received this problem as a `git-bundle`.
Please do your work on a separate branch (as shown below):

```
git checkout -b candidate/<your-name-here>
```

Please `git-bundle` up your work
(make sure your branch is included!)
and email it to the address you received this repository from.
Include a `DESIGN.md` document in your solution
if you feel you need to state any assumptions
or would like to describe your approach.

Our team will review your work and get back to you ASAP!

## Vocabulary

### Description of the sample_campaigns data:

**campaign_id:** A unique identifier for campaigns

**campaign_status:** Pending, Live, or Completed.
    This describes where the campaign is in its lifetime. When a
    salesperson creates a campaign, it must be approved. Before approval, it is in
    'Pending' status. Once it is approved, it becomes 'Live.' Upon
    completion, it becomes 'Completed.'

**campaign_ordered_at:** Date when the campaign was created.

**revision_number:** When a campaign is created, it may be revised and
    resubmitted. The first version gets a revision_number of 0, incrementing with
    each new revision.

**next_revision_ordered_at:** If the campaign has multiple revisions, this field
    marks the date of the next revision.

**is_last_ordered_campaign:** Because campaigns can have multiple revision
    versions, we are often only interested in looking at the most recent revision
    version. is_last_ordered_campaign is a boolean displaying whether the
    revision_number is the most recent one. For example:

```
campaign_id revision_version	is_last_ordered_version
A	0	f
B	1	f
C	2	t
```

**campaign_start_date:** Start date of the campaign.

**campaign_end_date:** End date of the campaign.

**salesperson_id:** Foreign key. An ID marking which salesperson created the
    campaign.

**gross_revenue:** The total gross revenue that the campaign made, not
    accounting for any costs, "margins," or other expenses. This is the actual
    dollar amount that a client gets charged for a campaign.

**net_revenue:** Gross revenue minus all costs, margins, and expenses.

### Other relevant vocabulary:

**Margin (percent):** When a campaign is ordered, margin is the percentage of the
    gross_revenue which Centro is paid. Margin percent may be calculated as
    net_revenue / gross_revenue

**Margin (dollar amount):** If a campaign has a 20% margin, and makes $100,000
    gross_revenue, the margin (in dollars) would be $20,000.

### Gross revenue allocation by month:

For the purposes of this problem, if you need to break out gross or net
revenue numbers by month, you can assume a uniform distribution by month.
That means that if a campaign has a start date of 3/1/2016, and an end date
of 4/20/2016, then each month gets an equal amount of gross revenue. So, if
the total gross_revenue for the campaign is $30,000, then each month would
have $15,000 gross_revenue.

## The Challenge

In the `data/` directory, you have been provided with CSV files
containing a small set of data similar to what we work with on a regular basis.
For all of your answers, please provide the code and any explanation behind your execution in a `DESIGN.md` file.
Using this data set, please proceed with the following:

1. Provide a script in a `scripts/` directory to load the CSV data into database table(s) of your own design.
2. Provide SQL scripts in a `scripts/` directory to achieve the following:
    - List the Sales Team name, Gross Revenue and Net Revenue of the latest ordered campaigns by Sales Team.
    - List the Sales Team name, Gross Revenue, Net Revenue, and Margin Revenue of the latest ordered campaigns by Sales Team.
    - List all Sales Person names from the salesperson table with his/her Gross Revenue, Net Revenue, and Margin Revenue of the latest ordered campaigns.
    - List the Sales Persons name who had more than 3 Campaigns assigned to them.
    - List the top 5 sellers in 2015 based on the Net Revenue.
    - List the Top Seller in each Sales Team who exceeded $100,000 Gross Revenue.
    - List the Year, Quarter, Month, Sales team name, Sales Person name, Gross Revenue, Net Revenue and Margin Revenue of the latest ordered campaigns by Year, Quarter, Month, Sales Team, and Sales Person. The Year, Quarter and Month are based on the Plan Ordered At of the lasted ordered campaigns.
    - List the Sales team name, Sales Manager name, Gross Revenue and Net Revenue of the latest ordered campaigns by Sales team and Sales Manager.
    - List the Sales VP name, Sales VP Gross Revenue, Sales VP Net Revenue, Sales Director Name, Sales Director Gross Revenue, Sales Director Net Revenue, Sales Manager name, Sales Manager Gross Revenue, Sales Manager Net Revenue of the latest ordered campaigns. The Gross Revenue and Net revenue should include all the revenue numbers from all salespeople who report to them.
3. (BONUS ARCHITECTURE QUESTION) Provide a prose answer (on the order of a few paragraphs) in your `DESIGN.md` file for the following:
    - Imagine this problem scaled up to a large business working with terabytes to petabytes of information.  Would your solution be different?  What kinds of performance issues would you consider?  What overall architectural concerns would you have?  How might you structure a team around this kind of work?  Be creative!
