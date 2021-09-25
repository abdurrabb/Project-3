# Final Storyboard

https://public.tableau.com/app/profile/john.k1575/viz/Project3-EducateFinalStoryboard/DBDMStory?publish=yes


# Project-3-EDUCATE

STAGE 1: DEFINING THE PROBLEM
In the second annual report of Breaking the Link, released May 2019 by Charlotte-Mecklenburg Schools, it states,
"
The CMS Board of Education defined equity as 'providing the opportunities, support, environment, high expectations, and resources that every student needs to achieve
educational success, feel valued, and contribute to a thriving community.'
"


Project 3 - Educate - README


SEP 14

# IDENTIFIED SCHOOL PERFORMANCE KPIs
- Academic KPIs
	- 4-Year Cohort Graduation Rate Percent
	- ACT Percent 
		- or ACT WorkKeys Assessments Indicator["The ACT/ACT WorkKeys Indicator is the percentage of 12th graders who met either the UNC System Minimum 17 composite on ACT or Silver or better on the ACT WorkKeys assessment."]

- Community Climate KPIs
	- Chronic Absenteeism
	- Suspensions & Expulsions

- Groupby Demographics
	- Male vs Female
	- Black vs White vs Hispanic
	- Economically Disadvantaged vs Not Economically Disadvantaged


# DEFINED SCOPE OF PROJECT
- High Schools
- Charlotte-Mecklenburg School District in NC
- If time and data allows, expand to all school districts in NC
- Using data from 2015-2019 
	- (Avoiding 2020 due to COVID anamolies)
	- Why 2015; In 2017 Char-Meck District launched Opportunity Task Force with the following expressed purpose: "A major focus of the CMS strategic plan is breaking the link between poverty and academic achievement in order to close gaps and reach educational equity in our community." Showing data from 2015 through 2019 offers a before-after snapshot of the programs' effectiveness. 
	- Further context: "A 2013 study conducted by Harvard University and the University of California, Berkeley, examined economic mobility in the largest 50 cities in the United States. Charlotte was 50th, a finding that confirmed what many have observed anecdotally: If you are born poor in Charlotte, you are likely to stay that way. The economic-mobility study's findings sparked alarm and resulted in the formation of an Opportunity Task Force which issued a report in March 2017." -
	- "A major focus of the CMS strategic plan is breaking the link between poverty and academic achievement in order to close gaps and reach educational equity in our community."
- Compare CMS vs NC schools to measure impact of initiative?


# IDENTIFIED DATA SOURCE:
Academic KPI Data
- https://www.dpi.nc.gov/districts-schools/testing-and-school-accountability/school-accountability-and-reporting/accountability-data-sets-and-reports#2018–19-reports
- #Year-Reports
	- 2018-19 School Assessment and Other Indicator Data
	- 2017-18 School Assessment and Other Indicator Data
	- 2016-17 State, District, and School Level Other Indicators Report 
	- 2015-16 State, District, and School Level Other Indicators Report   
- DrillDown Data
	- missing drill down for 2019
	- missing drill down for 2018
	- ACCdrilldwn17
	- ACCdrilldwn16
	- ACCdrilldwn15

- Executive Summary Data [satisfies query by Scott regarding raw numbers of students within each subgroup]
	- 

Community KPI Data
	-missing 
	
	
# STRUCTURING DATA:
Considering best database format (SQL vs Mongo)
	- Free trial access to AWS (SQL) through Dec may place project behind paywall limit future availability during job search
	- With SQL, may have to structure each KPI into its own table with school/district code keys
	- With SQL, how do we make disparate data table relational
	- John/Josh/Alex have experience with SQLs frustrating limitation when structuring data for export
	- With Mongo, easier initial set up
	- With Mongo, geoJSON more fluid and allows easier map visualizations



# PRESENTATION:
Story
- focus on CMS performance, community, demographic 2015-2017
- highlight report/task force goal
- present performance, commmunity, demographic 2017-2019
- prescribe call to action to CMS
- zoom out to compare CMS vs all districts

Visualizations
- Map of CMS district with overlays for academic performance, community climate, and demographic groups - user selectable
- Interactive pivot tables?


# FOLLOW-UP TASKS BY MEMBER:
AB
	- research Tableau for story-telling best practices applicable to project (ie interactive charts, maps, etc.)
	- compile and post notes from meeting
	- collect remaining data for school KPIs (2015-2019)

ALEX
	- attempt to upload school data onto database (Mongo or AWS)
	- draft data to Jupyter format so team may trial transform data

JOHN
	- practice transforming sample data in Jupyter
	- develop project timeline projection tracker

JOSH
	- attempt to upload school data onto database (Mongo or AWS)

SCOTT
	- find map coordinates for CMS schools for geoJSON applications
