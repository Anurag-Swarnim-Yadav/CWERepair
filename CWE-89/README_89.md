<p align="center">
  </a>
  <h3 align="center">CWE-89</a></h3>
  <p align="center">
    Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')<br><br><br> **Note:** :warning: - Unverifiable CWE Samples, :x: - misclassified CWE samples, :recycle: correct CWE for misclassified, :heavy_plus_sign: - Duplicate CWE samples <br><br><br>
  </p>
</p>
<div align="center">

## Real-World Software Vulnerabilities

</div>

<details open="open">
<summary>CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')</summary>

<h3>
    <b>
        <div align="center">
            Detection Performance of gpt-4-1106-preview in three different settings.
        </div>
    </b>
</h3>
  
<div align="center">

|  Sample   |  gpt-4-1106 (No explanation) | gpt-4-1106-CWEtype  | gpt-4-1106 (with explanation)  | gpt-4-1106-CWEtype  | gpt-4-1106 (with explanation and highlighted code segment) | gpt-4-1106-CWEtype |
|-----------|------------------------|---------------------|-----------------------------|---------------------------|-----------------------------------|-------------------|
|   CWE89-57                                    |  Yes  |  CWE-120 (80%)  |  Yes  |  CWE-120 (90%)  |  Yes  |  CWE-20 (80%)  **code: Yes (1/1)** |
|   CWE89-1063                                  |  Yes  |  CWE-20 (80%)   |  Yes  |  CWE-20 (90%)   |  Yes  |  CWE-20 (80%)  **code: Yes (1/1)** |
|  :x: CWE89-1484    |  Yes  |  **CWE-120 (80%)**  |  Yes  |  **CWE-120 (90%)**  |  Yes  |  **CWE-120 (90%)**  code: No    |
|  :x: CWE89-1671    |  Yes  |  **CWE-120 (80%)**  |  Yes  |  **CWE-120 (90%)**, CWE-170 (80%), CWE-391 (70%)  |  Yes  |  **CWE-120 (90%)**  code: No    |
|  :heavy_plus_sign: CWE89-1691                 |  Yes  |  CWE-120 (80%)  |  Yes  |  CWE-120 (90%), CWE-170 (80%), CWE-391 (70%)  |  Yes  |  CWE-120 (90%)  code: No    |
|  Total                                        |  5/5  |  1/5            |  5/5  |  1/5            |  5/5  |  1/5                        |

</div>

<h3>
    <b>
        <div align="center">
            Detection Performance of text-davinvi-003 in three different settings.
        </div>
    </b>
</h3>

<div align="center">

|  Sample   |  text-davinvi-003 (No explanation) | text-davinvi-003-CWEtype  | text-davinvi-003 (with explanation)  | text-davinvi-003-CWEtype  | text-davinvi-003 (with explanation and highlighted code segment) | text-davinvi-003-CWEtype |
|-----------|------------------------|---------------------|-----------------------------|---------------------------|-----------------------------------|-------------------|
|   CWE89-57                     |  No   |  -                                                              |  Yes  |  CWE-119 (100%)      |  No   |  -   |
|   CWE89-1063                   |  No   |  -                                                              |  No   |  -                   |  No   |  -   |
|  :x: CWE89-1484                |  Yes  |  **CWE-120 (90%)**, CWE-457 (90%), CWE-20 (90%), CWE-676 (90%)  |  Yes  |  **CWE-120 (90%)**   |  Yes  |  CWE-119 (90%)  code: No    |
|  :x: CWE89-1671                |  Yes  |  **CWE-120 (90%)**                                              |  Yes  |  CWE-119 (95%)       |  Yes  |  CWE-119 (90%)  code: No    |
|  :heavy_plus_sign: CWE89-1691  |  Yes  |  CWE-120 (90%)                                                  |  Yes  |  CWE-119 (95%)       |  Yes  |  CWE-119 (90%)  code: No    |
|  Total                         |  3/5  |  1/5                                                            |  4/5  |  1/5                 |  3/5  |  0/5                        |
</div>
</details>
