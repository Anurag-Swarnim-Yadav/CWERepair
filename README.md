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






