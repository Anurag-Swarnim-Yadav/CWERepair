
<h3>
    <b>
        <div align="center">
            VulRepair Performance on Top-25 Most Dangerous CWEs (NIST Verification)
        </div>
    </b>
</h3>
  
<div align="center">
    
| Sample            | CWE Type |                     Name                     | NIST |
|:-----------------:|:--------:|:--------------------------------------------:|:----:|
|   CWE79-856       |  CWE-79  |             Cross-site Scripting             |  Yes |
|   CWE78-1012      |  CWE-78  |             OS Command Injection             |  Yes |
|   CWE78-1149      |  CWE-78  |             OS Command Injection             |  Yes |
|   CWE78-1502      |  CWE-78  |             OS Command Injection             |  Yes |
|   CWE89-57        |  CWE-89  |                 SQL Injection                |  Yes |
|   CWE89-1063      |  CWE-89  |                 SQL Injection                |  Yes |
|   CWE89-1484      |  CWE-89  |                 SQL Injection                |  Yes |
|   CWE89-1671      |  CWE-89  |                 SQL Injection                |  Yes |
|   CWE89-1691 (D: CWE89-1671) |  CWE-89  |      SQL Injection                |  Yes |
|   CWE22-212       |  CWE-22  |                Path Traversal                |  Yes |
|   CWE22-402       |  CWE-22  |                Path Traversal                |  Yes |
|   CWE22-512       |  CWE-22  |                Path Traversal                |  Yes |
|   CWE22-692       |  CWE-22  |                Path Traversal                |  Yes |
|   CWE22-964       |  CWE-22  |                Path Traversal                |  Yes |
|   CWE22-1027 (D: CWE22-512)  |  CWE-22  |     Path Traversal                |  Yes |
|   CWE22-1436      |  CWE-22  |                Path Traversal                |  Yes |
|   CWE22-1656      |  CWE-22  |                Path Traversal                |  Yes |
|   CWE352-1540     |  CWE-352 |          Cross-Site Request Forgery          |  Yes |
|   CWE352-1580     |  CWE-352 |          Cross-Site Request Forgery          |  Yes |
|  CWE287-231       |  CWE-287 |            Improper Authentication           |  Yes |
|  CWE287-287       |  CWE-287 |            Improper Authentication           |  Yes |
|  CWE287-413       |  CWE-287 |            Improper Authentication           |   -  |
|  CWE287-561(D: CWE287-231)   |  CWE-287 | Improper Authentication           |  Yes |
|  CWE287-975       |  CWE-287 |            Improper Authentication           |  Yes |
|  CWE287-1635      |  CWE-287 |            Improper Authentication           |  Yes |
|  CWE862-200       |  CWE-862 |             Missing Authorization            |  Yes |
|  CWE862-693(D: CWE862-200)   |  CWE-862 |  Missing Authorization            |  Yes |
|  CWE522-21        |  CWE-522 |     Insufficiently Protected Credentials     |  CWE-287, CWE-755 |
|  CWE522-370       |  CWE-522 |     Insufficiently Protected Credentials     |  Yes |
|  CWE522-773       |  CWE-522 |     Insufficiently Protected Credentials     |  Yes |
|  CWE522-1655      |  CWE-522 |     Insufficiently Protected Credentials     |  CWE-522, CWE-20 |
|  CWE732-276       |  CWE-732 |        Incorrect Permission Assignment       |  Yes |
|  CWE732-1575      |  CWE-732 |        Incorrect Permission Assignment       |  CWE-909, CWE-459 |
|  CWE611-7         |  CWE-611 |     Improper Restriction of XML Reference    |  Yes |
|  CWE611-351       |  CWE-611 |     Improper Restriction of XML Reference    |  Yes |
|  CWE611-1274      |  CWE-611 |     Improper Restriction of XML Reference    |  Yes |
|  CWE918-806       |  CWE-918 |      Server-Side Request Forgery (SSRF)      |  Yes |
|  CWE77-126        |  CWE-77  |               Command Injection              | CWE-78 |
|  CWE77-1608       |  CWE-77  |               Command Injection              | Yes  |
|                   |          |               TOTAL                          |  4/39 |

</div> 

<br>
<br>
<br>

<h3>
    <b>
        <div align="center">
            VulRepair Performance on Top-25 Most Dangerous CWEs (Training and Validation Samples Verification)
        </div>
    </b>
</h3>
  
<div align="center">
    
| Sample            | CWE Type |                     Name                     | VulRepair Correctly Predicted | Present in Train Dataset| Number of Sample Present | CWE Type of Sample |
|:-----------------:|:--------:|:--------------------------------------------:|:-----------------------------:|:-----------------------:|:-------------------------:|:--------------------|
|   CWE79-856       |  CWE-79  |             Cross-site Scripting             |  No |    Yes    |    2 | CWE-79    |
|   CWE78-1012      |  CWE-78  |             OS Command Injection             |  No |    Yes    |    1 | CWE-78    |
|   CWE78-1149      |  CWE-78  |             OS Command Injection             |  No |    Yes    |    1 | CWE-78    |
|   CWE78-1502      |  CWE-78  |             OS Command Injection             | Yes |    Yes	|    2 | CWE-78    |
|   CWE89-57        |  CWE-89  |                 SQL Injection                |  No |    Yes	|	1 | CWE-89    |
|   CWE89-1063      |  CWE-89  |                 SQL Injection                |  No |    Yes	|	1 | CWE-89    |
|   CWE89-1484      |  CWE-89  |                 SQL Injection                | Yes |    Validation Dataset     |	- |	-         |
|   CWE89-1671      |  CWE-89  |                 SQL Injection                |  No |    Yes	|	1 | CWE-89    |
|   CWE89-1691 (D: CWE89-1671) |  CWE-89  |      SQL Injection                |  No |    Yes    |	1 | CWE-89    |
|   CWE22-212       |  CWE-22  |                Path Traversal                |  No |    Yes    |	1 | CWE-22    |
|   CWE22-402       |  CWE-22  |                Path Traversal                |  No |    Yes    |	2 | CWE-22    |
|   CWE22-512       |  CWE-22  |                Path Traversal                |  No |    Yes    |	2 | CWE-22    |
|   CWE22-692       |  CWE-22  |                Path Traversal                |  No |    Yes    |	1 | CWE-22    |
|   CWE22-964       |  CWE-22  |                Path Traversal                |  No |    Yes    |	1 | CWE-22    |
|   CWE22-1027 (D: CWE22-512)  |  CWE-22  |     Path Traversal                |  No |    Yes    |	2 | CWE-22    |
|   CWE22-1436      |  CWE-22  |                Path Traversal                | Yes |    Yes    |	1 | CWE-22    |
|   CWE22-1656      |  CWE-22  |                Path Traversal                | Yes |    Yes    |	2 | CWE-22    |
|   CWE352-1540     |  CWE-352 |          Cross-Site Request Forgery          |  No |    Validation Dataset     |	- |	-         |
|   CWE352-1580     |  CWE-352 |          Cross-Site Request Forgery          |  No |    Yes    |	1 | CWE-352   |
|  CWE287-231       |  CWE-287 |            Improper Authentication           |  No |    Yes	|	1 | CWE-287    |
|  CWE287-287       |  CWE-287 |            Improper Authentication           | Yes |    Yes	|	1 | CWE-287    |
|  CWE287-413       |  CWE-287 |            Improper Authentication           |  No |    Yes	|	1 | CWE-287    |
|  CWE287-561(D: CWE287-231)   |  CWE-287 | Improper Authentication           |  No |    Yes	|	1 | CWE-287    |
|  CWE287-975       |  CWE-287 |            Improper Authentication           | Yes |    No     |	- |	-          |
|  CWE287-1635      |  CWE-287 |            Improper Authentication           | Yes |    Yes	|	2 | CWE-287    |
|  CWE862-200       |  CWE-862 |             Missing Authorization            |  No |    Yes	|	1 | CWE-862    |
|  CWE862-693(D: CWE862-200)   |  CWE-862 |  Missing Authorization            |  No |    Yes	|	1 | CWE-862    |
|  CWE522-21        |  CWE-522 |     Insufficiently Protected Credentials     |  No |    Yes	|	1 | CWE-522    |
|  CWE522-370       |  CWE-522 |     Insufficiently Protected Credentials     |  No |    Yes	|	2 | CWE-522    |
|  CWE522-773       |  CWE-522 |     Insufficiently Protected Credentials     |  No |    Yes	|	2 | CWE-522    |
|  CWE522-1655      |  CWE-522 |     Insufficiently Protected Credentials     |  No |    Yes	|	1 | CWE-522    |
|  CWE732-276       |  CWE-732 |        Incorrect Permission Assignment       | Yes |    Yes	|	1 | CWE-732    |
|  CWE732-1575      |  CWE-732 |        Incorrect Permission Assignment       |  No |    No     |	- |	-          |
|  CWE611-7         |  CWE-611 |     Improper Restriction of XML Reference    |  No |    Validation Dataset     |	- |	-          |
|  CWE611-351       |  CWE-611 |     Improper Restriction of XML Reference    |  No |    Yes	|	1 | CWE-611    |
|  CWE611-1274      |  CWE-611 |     Improper Restriction of XML Reference    |  No |    No     |	- |	-          |
|  CWE918-806       |  CWE-918 |      Server-Side Request Forgery (SSRF)      |  No |    Yes	|	2 | CWE-918    |
|  CWE77-126        |  CWE-77  |               Command Injection              | Yes |    Yes	|	2 | CWE-78, CWE-77 |
|  CWE77-1608       |  CWE-77  |               Command Injection              | Yes |    Yes    |	1 | CWE-77     |
|                    |         |               TOTAL                        | 10/39 |   36/39   |     |            |

</div> 

<br>
<br>

<div align="center">
    
| Sample            | CWE Type |                     Name                     | VulRepair Correctly Predicted | Present in Validation Dataset| Number of Sample Present | CWE Type of Sample |
|:-----------------:|:--------:|:--------------------------------------------:|:-----------------------------:|:-----------------------:|:-------------------------:|:--------------------|
|   CWE89-1484      |  CWE-89  |                 SQL Injection                | Yes |    Yes    |	 1 | CWE-89    |
|   CWE352-1540     |  CWE-352 |          Cross-Site Request Forgery          |  No |    Yes    |	 1 | CWE-352   |
|  CWE611-7         |  CWE-611 |     Improper Restriction of XML Reference    |  No |    Yes    |	 1 | CWE-611   |

</div>

<br>
<br>
<br>

<h3>
    <b>
        <div align="center">
            VulRepair Performance on Top-25 Most Dangerous CWEs (CWE Identification)
        </div>
    </b>
</h3>
  
<div align="center">
    
| Sample            | CWE Type |                     Name                     | NIST |
|:-----------------:|:--------:|:--------------------------------------------:|:----:|
|   CWE79-856       |  CWE-79  |             Cross-site Scripting             |  Yes |
|   CWE78-1012      |  CWE-78  |             OS Command Injection             |  Yes |
|   CWE78-1149      |  CWE-78  |             OS Command Injection             |  Yes |
|   CWE78-1502      |  CWE-78  |             OS Command Injection             |  Yes |
|   CWE89-57        |  CWE-89  |                 SQL Injection                |  Yes |
|   CWE89-1063      |  CWE-89  |                 SQL Injection                |  Yes |
|   CWE89-1484      |  CWE-89  |                 SQL Injection                |  Yes |
|   CWE89-1671      |  CWE-89  |                 SQL Injection                |  Yes |
|   CWE89-1691 (D: CWE89-1671) |  CWE-89  |      SQL Injection                |  Yes |
|   CWE22-212       |  CWE-22  |                Path Traversal                |  Yes |
|   CWE22-402       |  CWE-22  |                Path Traversal                |  Yes |
|   CWE22-512       |  CWE-22  |                Path Traversal                |  Yes |
|   CWE22-692       |  CWE-22  |                Path Traversal                |  Yes |
|   CWE22-964       |  CWE-22  |                Path Traversal                |  Yes |
|   CWE22-1027 (D: CWE22-512)  |  CWE-22  |     Path Traversal                |  Yes |
|   CWE22-1436      |  CWE-22  |                Path Traversal                |  Yes |
|   CWE22-1656      |  CWE-22  |                Path Traversal                |  Yes |
|   CWE352-1540     |  CWE-352 |          Cross-Site Request Forgery          |  Yes |
|   CWE352-1580     |  CWE-352 |          Cross-Site Request Forgery          |  Yes |
|  CWE287-231       |  CWE-287 |            Improper Authentication           |  Yes |
|  CWE287-287       |  CWE-287 |            Improper Authentication           |  Yes |
|  CWE287-413       |  CWE-287 |            Improper Authentication           |   -  |
|  CWE287-561(D: CWE287-231)   |  CWE-287 | Improper Authentication           |  Yes |
|  CWE287-975       |  CWE-287 |            Improper Authentication           |  Yes |
|  CWE287-1635      |  CWE-287 |            Improper Authentication           |  Yes |
|  CWE862-200       |  CWE-862 |             Missing Authorization            |  Yes |
|  CWE862-693(D: CWE862-200)   |  CWE-862 |  Missing Authorization            |  Yes |
|  CWE522-21        |  CWE-522 |     Insufficiently Protected Credentials     |  CWE-287, CWE-755 |
|  CWE522-370       |  CWE-522 |     Insufficiently Protected Credentials     |  Yes |
|  CWE522-773       |  CWE-522 |     Insufficiently Protected Credentials     |  Yes |
|  CWE522-1655      |  CWE-522 |     Insufficiently Protected Credentials     |  CWE-522, CWE-20 |
|  CWE732-276       |  CWE-732 |        Incorrect Permission Assignment       |  Yes |
|  CWE732-1575      |  CWE-732 |        Incorrect Permission Assignment       |  CWE-909, CWE-459 |
|  CWE611-7         |  CWE-611 |     Improper Restriction of XML Reference    |  Yes |
|  CWE611-351       |  CWE-611 |     Improper Restriction of XML Reference    |  Yes |
|  CWE611-1274      |  CWE-611 |     Improper Restriction of XML Reference    |  Yes |
|  CWE918-806       |  CWE-918 |      Server-Side Request Forgery (SSRF)      |  Yes |
|  CWE77-126        |  CWE-77  |               Command Injection              | CWE-78 |
|  CWE77-1608       |  CWE-77  |               Command Injection              | Yes  |
|                   |          |               TOTAL                          |  4/39 |

</div> 

