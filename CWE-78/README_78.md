<p align="center">
  </a>
  <h3 align="center">CWE-78</a></h3>
  <p align="center">
    <b>Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection')</b><br><br><br> **Note:** :warning: - Unverifiable CWE Samples, :x: - misclassified CWE samples, :recycle: correct CWE for misclassified, :heavy_plus_sign: - Duplicate CWE samples <br><br><br>
  </p>
</p>
<div align="center">

## Real-World Software Vulnerabilities

</div>

<details>
<summary>Detection Performance of gpt-4-1106-preview in three different settings.</summary>
  
<div align="center">

|  Sample   |  gpt-4-1106 (No explanation) | gpt-4-1106-CWEtype  | gpt-4-1106 (with explanation)  | gpt-4-1106-CWEtype  | gpt-4-1106 (with explanation and highlighted code segment) | gpt-4-1106-CWEtype |
|-----------|------------------------|---------------------|-----------------------------|---------------------------|-----------------------------------|-------------------|
|  :warning: CWE78-1012  |  Yes  |  CWE-319 (90%), CWE-20 (80%), CWE-476 (70%), CWE-787 (60%), CWE-400 (50%), CWE-613 (40%), CWE-918 (30%) |  Yes  |  CWE-20 (90%), CWE-120 (80%), CWE-170 (70%), CWE-798 (60%), CWE-209 (75%), CWE-319 (90%), CWE-404 (70%), CWE-391 (80%)  |  Yes  |  CWE-319 (90%), CWE-20 (80%), CWE-400 (70%), CWE-79 (60%), CWE-770 (70%); code: No  |
|   CWE78-1149  |  Yes  |  CWE-120 (80%), CWE-787 (60%), CWE-476 (70%), CWE-416 (70%), CWE-674 (50%), CWE-665 (60%), CWE-754 (70%), CWE-20 (80%)  |  Yes  |  CWE-120 (70%), CWE-416 (60%), CWE-170 (60%), CWE-20 (70%), CWE-772 (65%), CWE-77 (50%), CWE-190 (60%), CWE-391 (60%)  |  Yes  |  **CWE-78 (80%)**, CWE-676 (80%), CWE-119 (80%), CWE-754 (80%), CWE-416 (80%), CWE-722 (80%), CWE-665 (80%); **code: Yes (1/1)**  |
|  CWE78-1502  |  Yes  |  CWE-131 (90%)  |  Yes  |  CWE-131 (90%)  |  Yes  |  **CWE-78 (90%); code: Yes (1/1)**  |
|  Total                                      |  2/3  |  0/3  |  2/3  |  0/3  |  2/3  |  2/3  |

</div>
</details>
<details>
  <summary>Detection Performance of text-davinvi-003 in three different settings.</summary>
  
<div align="center">

|  Sample   |  text-davinvi-003 (No explanation) | text-davinvi-003-CWEtype  | text-davinvi-003 (with explanation)  | text-davinvi-003-CWEtype  | text-davinvi-003 (with explanation and highlighted code segment) | text-davinvi-003-CWEtype |
|-----------|------------------------|---------------------|-----------------------------|---------------------------|-----------------------------------|-------------------|
|  :warning: CWE78-1012  |  No   |  -              |  Yes  |  CWE-119 (90%)     |  Yes  |  CWE-120 (90%); code: No      |
|  CWE78-1149            |  Yes  |  CWE-843 (90%)  |  Yes  |  CWE-120 (95%)     |  Yes  |  CWE-120 (100%); code: No      |
|  CWE78-1502            |  No   |  -              |  Yes  |  **CWE-78 (95%)**  |  Yes  |  **CWE-78 (100%); code: Yes**  |
|  Total                 |  2/3  |  0/3            |  2/3  |  1/3               |  2/3  |  1/3                           |

</div>
</details>
