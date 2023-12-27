<p align="center">
  </a>
  <h3 align="center">CWE-611</a></h3>
  <p align="center">
    <b>Improper Restriction of XML External Entity Reference</b><br><br><br> **Note:** :white_check_mark: - Perfect CWE Samples, :warning: - Unverifiable CWE Samples, :x: - Misclassified CWE Samples, :recycle: Correct CWE for Misclassified, :heavy_plus_sign: - Duplicate CWE samples <br><br><br>
  </p>
</p>
<div align="center">

## Real-World Software Vulnerabilities

</div>
<details>
<summary>Detection Performance of gpt-4-1106-preview in three different settings.</summary><br>


<h3>
    <b>
        <div align="center">
            :white_check_mark: - Perfect CWE Samples
        </div>
    </b>
</h3>

<div align="center">

|  Sample   |  gpt-4-1106 (No explanation) | gpt-4-1106-CWEtype  | gpt-4-1106 (with explanation)  | gpt-4-1106-CWEtype  | gpt-4-1106 (with explanation and highlighted code segment) | gpt-4-1106-CWEtype |
|-----------|------------------------|---------------------|-----------------------------|---------------------------|-----------------------------------|-------------------|
|  CWE611-7                                        |  Yes  | CWE-20 (70%)  | Yes  |  CWE-776 (70%), CWE-190 (60%)  | Yes  |  **CWE-611 (90%); code: Yes (1/1)**  |
|  CWE611-1274                                     |  Yes  | CWE-476 (60%), CWE-787 (60%), CWE-665 (60%), CWE-200 (60%), CWE-404 (60%)  |  Yes  |  CWE-215 (80%), CWE-476 (80%), CWE-20 (80%), CWE-532 (80%), CWE-665 (80%), CWE-404 (80%) | Yes  | CWE-20 (70%); code: No  |  
|  Total                                           |  2/2  |  0/2  |  2/2  |  0/2  |  2/2  |  1/2  |

</div>


<h3>
    <b>
        <div align="center">
            :warning: - Unverifiable CWE Samples
        </div>
    </b>
</h3>

<div align="center">

|  Sample   |  gpt-4-1106 (No explanation) | gpt-4-1106-CWEtype  | gpt-4-1106 (with explanation)  | gpt-4-1106-CWEtype  | gpt-4-1106 (with explanation and highlighted code segment) | gpt-4-1106-CWEtype |
|-----------|------------------------|---------------------|-----------------------------|---------------------------|-----------------------------------|-------------------|
|  :warning: CWE611-351  |  No   | -     | No   | -      | No    | -     |
|  Total                 |  1/1  |  1/1  |  1/1  |  1/1  |  1/1  |  1/1  |

</div>
</details>


<details>
  <summary>Detection Performance of text-davinvi-003 in three different settings.</summary><br>


  <h3>
    <b>
        <div align="center">
            :white_check_mark: - Perfect CWE Samples
        </div>
    </b>
</h3>

<div align="center">

|  Sample   |  text-davinvi-003 (No explanation) | text-davinvi-003-CWEtype  | text-davinvi-003 (with explanation)  | text-davinvi-003-CWEtype  | text-davinvi-003 (with explanation and highlighted code segment) | text-davinvi-003-CWEtype |
|-----------|------------------------|---------------------|-----------------------------|---------------------------|-----------------------------------|-------------------|
|  CWE22-212  |  No  |  -  | No  |  -  |  Yes  |  CWE-119 (90%);  code: No  |
|  CWE22-402  |  Yes  |  **CWE-22 (90%)**  |  Yes  |  **CWE-22 (90%)**  |  Yes  |  CWE-119; code: No (adds strncpy instead of strcpy|
| CWE22-512 |  Yes  |  CWE-284 (95%),  CWE-78 (90%)  | Yes  |  **CWE-22 (90%)**  | Yes  | **CWE-22 (90%);  code: Yes (1/4)**  |
| CWE22-692 |  Yes  | CWE-732 (90%)  |  Yes  | CWE-476 (100%)  |  Yes  |  CWE-476 (95%); **code: yes (1/2)**  |
| CWE22-964 |  Yes  | CWE-20  |  Yes |  CWE-119  | Yes  | CWE-120 (95%); code: No|
| CWE22-1027|  Yes  | CWE-284 (90%), CWE-78 (90%)  | Yes  | **CWE-22 (90%)**  | Yes | **CWE-22 (90%); code: Yes (1/4)**  | 
| CWE22-1436| Yes  | **CWE-22 (95%)**  |  Yes  |  CWE-120 (90%)  | Yes  |  **CWE-22 (95%); code: yes (1/1)**|  
| CWE22-1656|  No  |  -  |  No  |  -  |  No  |  -  |  
| Total     |  6/8  |  2/8  |  6/8  |  3/8  |  7/8  |  3/8  |
</div>
</details>
