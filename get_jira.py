#!/usr/bin/env python

import sys
import re
from jira import JIRA

jira = JIRA('http://jira.zeusis.com', basic_auth=('kobe.liu', 'l!19900528'))

obj_issue = jira.issue('ALPHA-101')

print obj_issue.fields.summary
issue_in_alpha = jira.search_issues('project=ALPHA')
print issue_in_alpha
