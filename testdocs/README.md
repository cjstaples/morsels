Script to pregenerate the scrum test documentation files

input:  1 or more JIRA ticket numbers
            possible constrain input to valid JIRA number format
        base document format to sub data into boilerplate
        
- get input(s) of JIRA numbers from cmd line or file
- for each JIRA input
    create a base doc file with the appropriate name, e.g "CAM-1234_brief-summary_testing.txt"
    populate internal header lines for jira_number, jira_full-summary, jira_link, separator

--
Version History

1.0 -- Initial working version

