# TOTAL SECONDS, JOIN, GROUP BY, SUM, ASTYPE
import pandas as pd


# Get the duration of the project
n = 365*24*3600 # Number of seconds in one year (365 days)
linkedin_projects["project_duration"] = (
    (
    linkedin_projects["end_date"] 
    - linkedin_projects["start_date"]
    ).dt.total_seconds() 
    / n
)


# Count total salaries of the employees by project
project_total_salaries = linkedin_emp_projects.merge(
    linkedin_employees,
    left_on="emp_id",
    right_on="id"
    ).groupby("project_id")["salary"] \
    .sum() \
    .rename("total_salaries") \
    .reset_index()


# Calculate the spent money over a specific project
budget_vs_cost = linkedin_projects.merge(
    project_total_salaries,
    left_on="id",
    right_on="project_id"
)
budget_vs_cost["prorated_expense"] = budget_vs_cost["project_duration"] * budget_vs_cost["total_salaries"]
budget_vs_cost["prorated_expense"] = budget_vs_cost["prorated_expense"].astype("int64") + 1


# Get the projects whose total employee expense exceeds the budget
output = budget_vs_cost[["title", "budget", "prorated_expense"]] \
    .query("`budget` < `prorated_expense`")


# Start writing code
output