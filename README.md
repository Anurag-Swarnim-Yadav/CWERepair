<p align="center">
  </a>
  <h3 align="center">CWERepair</a></h3>
  <p align="center">
    Revisiting Zero-Shot For Real-World Software Vulnerability Repair
  </p>
</p>

<div align="center">
Abstract—A record number of security vulnerabilities have
been reported to the Common Vulnerability Enumeration (CVE)
database in the last couple of years. These security vulnerabilities
are of different types that vary in complexity. The record number
of security vulnerabilities and complexity is in dire need of
automation to help developers reduce the time lag between re-
porting and fixing the vulnerabilities. Researchers have designed
and applied multiple machine learning-based systems to help
security developers fix vulnerabilities. However, these models
face various problems, such as reliance on large confirmed
vulnerability datasets, limited input, and output window size,
generalization on unknown and complicated bugs, and need
considerable time to generate plausible patches for a single bug.
This makes them impractical to be used in real life. On top of
that, we are still unclear if these tools work best for certain
types of security bugs. One solution is directly leveraging large
code language models (LLMs) trained on billions of text/code
tokes. LLMs have been applied on small programs related to
general software bugs and have shown promising results, but
security bugs are different as they are notoriously complicated.
In this work, we are interested in evaluating recently developed
Codex LLMs and comparing them with state-of-the-art fine-
tuned LLMs and DL-based models. This paper is the first to
study and compare the fixing capabilities of newly developed
LLMs on real-world vulnerabilities and assess the practicality of
these models.
</div>


<div align="center">
  
  ## Papers In Question
  
</div>

![](Papers-In-Question.png)

- **CVEfixes:** automated collection of vulnerabilities and their fixes from open-source software; Year: Aug.19, 2021; Conference: 17th International Conference on Predictive Models and Data Analytics in Software Engineering (PROMISE)
- **VRepair:** Neural Transfer Learning for Repairing Security Vulnerabilities in C Code; Year: Feb. 1, 2022; Conference: IEEE Transactions on Software Engineering
- **VulRepair:** A T5-Based Automated Software Vulnerability Repair; Year: Nov 7, 2022; Conference: 30th ACM Joint European Software Engineering Conference and Symposium on the Foundations of Software Engineering (ESEC/FSE)
- **Pre-trained Model-based Automated Software Vulnerability Repair: How Far are We?:** Year: Aug. 28, 2023; Conference: IEEE Transactions on Dependable and Secure Computing
- **DiverseVul:** A New Vulnerable Source Code Dataset for Deep Learning Based Vulnerability Detection; Year: Oct. 16, 2023; Conference: 26th International Symposium on Research in Attacks, Intrusions and Defenses (RAID)

<div align="center">

## Real-World Software Vulnerabilities

</div>


<details>
<summary>text-davinvi-003: without-buggy-line</summary>

<h3>
    <b>
        <div align="center">
            Performance on Top- 10 Most Dangerous CWEs in 2021
        </div>
    </b>
</h3>
  
<div align="center">

| Rank | CWE Type | Name                                                                                       | Count | VRepair | VulRepair | CWERepair |
|------|----------|--------------------------------------------------------------------------------------------|-------|---------|-----------|-----------|
| 1    | CWE-787  | Out-of-bounds Write                                                                        | 53    |         | 16        |           |
| 2    | CWE-79   | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')       | 1     |         | 0         |  0        |
| 3    | CWE-125  | Out-of-bounds Read                                                                         | 170   |         | 54        |           |
| 4    | CWE-20   | Improper Input Validation                                                                  | 152   |         | 68        |           |
| 5    | CWE-78   | Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection') | 3     |         | 1         |           |
| 6    | CWE-89   | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')       | 5     |         | 1         |  0        |
| 7    | CWE-416  | Use After Free                                                                             | 55    |         | 29        |           |
| 8    | CWE-22   | Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal')             | 8     |         | 2         |           |
| 9    | CWE-352  | Cross-Site Request Forgery (CSRF)                                                          | 2     |         | 0         |           |
| 10   | CWE-434  | Unrestricted Upload of File with Dangerous Type                                            | -     | -       | -         |           |

</div>
</details>

<details>
<summary>text-davinvi-003: with-buggy-line</summary>

<h3>
    <b>
        <div align="center">
            Performance on Top- 10 Most Dangerous CWEs in 2021
        </div>
    </b>
</h3>
  
<div align="center">

| Rank | CWE Type | Name                                                                                       | Count | VRepair | VulRepair | CWERepair |
|------|----------|--------------------------------------------------------------------------------------------|-------|---------|-----------|-----------|
| 1    | CWE-787  | Out-of-bounds Write                                                                        | 53    |         | 16        |           |
| 2    | CWE-79   | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')       | 1     |         | 0         |  0        |
| 3    | CWE-125  | Out-of-bounds Read                                                                         | 170   |         | 54        |           |
| 4    | CWE-20   | Improper Input Validation                                                                  | 152   |         | 68        |           |
| 5    | CWE-78   | Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection') | 3     |         | 1         |           |
| 6    | CWE-89   | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')       | 5     |         | 1         |  1        |
| 7    | CWE-416  | Use After Free                                                                             | 55    |         | 29        |           |
| 8    | CWE-22   | Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal')             | 8     |         | 2         |           |
| 9    | CWE-352  | Cross-Site Request Forgery (CSRF)                                                          | 2     |         | 0         |           |
| 10   | CWE-434  | Unrestricted Upload of File with Dangerous Type                                            | -     | -       | -         |           |

</div>
</details>



<details>
<summary>Analysis on Top-10 Most Accurately Repaired CWE Types of VulRepair</summary>

<h3>
    <b>
        <div align="center">
            Top-10 Most Accurately Repaired CWE Types of VulRepair  
        </div>
    </b>
</h3>

<div align="center">
  
| No   | CWE Type |                      Name                           |  %PP | Proportion | Present in Train  |  Number of Samples| CWEtype |
|:----:|:--------:|:---------------------------------------------------:|:----:|:----------:|:-----------------:|:--------:|:----------------:|
|   1  |  CWE-755 |  Improper Handling of Exceptional Conditions        | 100% |     1/1    | Yes  | 1   | CWE-755  |
|   2  |  CWE-706 | Use of Incorrectly-Resolved Name or Reference       | 100% |     1/1    | No   |  -  |  -  |
|   3  |  CWE-326 - 104 |         Inadequate Encryption Strength        | 100% |     1/1    | Yes  |  1  |  CWE-200  |
|   3  |  CWE-326 - 489 |         Inadequate Encryption Strength        | 100% |     1/1    | Yes  |  2  | CWE-326, CWE-310  |
|   4  |  CWE-667 |                Improper Locking                     | 100% |     1/1    | Yes  | 2   | CWE-362, CWE-667 |
|   5  |  CWE-369 - 218 |                 Divide By Zero                | 100% |     1/1    | Yes  | 2   | CWE-369, CWE-369  |
|   5  |  CWE-369 - 358 |                 Divide By Zero                | 100% |     1/1    | Yes  | 1   | CWE-369 |
|   5  |  CWE-369 - 407 |                 Divide By Zero                | 100% |     1/1    | Yes  | 1   | CWE-369 |
|   5  |  CWE-369 - 628 |                 Divide By Zero                | 100% |     1/1    | Yes  | 2   | CWE-369, CWE-369 |
|   5  |  CWE-369 - 768 |                 Divide By Zero                | 100% |     1/1    | Yes  | 1   | CWE-369 |
|   6  |  CWE-77  |               Command Injection                     | 100% |     2/2    |  -   | -   |  -  | 
|   7  |  CWE-388 |                 Error Handling                      | 100% |     1/1    | No   | -   | -   |
|   8  |  CWE-436 |            Interpretation Conflict                  | 100% |     1/1    | Yes  | 1   | CWE-436 | 
|   9  |  CWE-191-410 |               Integer Underflow                 | 100% |     1/1    | Yes  | 2   | CWE-191 |
|   9  |  CWE-191-685 |               Integer Underflow                 | 100% |     1/1    | Yes  | 1   | CWE-191 |
|  10  |  CWE-285-128 |            Improper Access Control              | 100% |     1/1    | Yes  | 1 | CWE-285 |
|  10  |  CWE-285-288 |            Improper Access Control              | 100% |     1/1    | Yes  | 2 | CWE-285 |
|  10  |  CWE-285-465 |            Improper Access Control              | 100% |     0/1    | Yes  | 2  | CWE-285 |
|  10  |  CWE-285-706 |            Improper Access Control              | 100% |     1/1    | No | - | - |
|  10  |  CWE-285-881 |            Improper Access Control              | 100% |     1/1    | Yes | 2 | CWE-285 |
|  10  | CWE-285-1098 |            Improper Access Control              | 100% |     1/1    | No | - | - |
|  10  | CWE-285-1389 (Duplicate: 465) |            Improper Access Control              | 100% |     0/1    | Yes | 2 | CWE-285 |
|  10  | CWE-285-1500 |            Improper Access Control              | 100% |     1/1    | Yes  | 2 | CWE-285 |
|      |          |                     TOTAL                           |  92% |    22/24   |
 
</div>
</details>





