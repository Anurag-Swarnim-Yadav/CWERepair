<p align="center">
  </a>
  <h3 align="center">CWE-732</a></h3>
  <p align="center">
    Incorrect Permission Assignment for Critical Resource
  </p>
</p>
<div align="center">

## Real-World Software Vulnerabilities

</div>

<details open="open">
<summary>CWE-732: Incorrect Permission Assignment for Critical Resource</summary>

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
|  CWE732-276  |  Yes  |  **CWE-22 (90%)**     |  Yes  |  **CWE-22 (90%)**  |  Yes  |  **CWE-22 (90%); code: Yes (4/4)**  |
|  :mag: :heavy_exclamation_mark: CWE732-1575  |  Yes  | CWE-120 (90%)  | Yes  |  CWE-476 ((90%)  | Yes  |  CWE-476 (90%); **code: Yes (2/2)**  |
|  Total      |  8/8  |  4/8  |  8/8  |  5/8  |  8/8  |  5/8  |

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
