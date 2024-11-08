<p align="center">
  </a>
  <h3 align="center">CWE-22</a></h3>
  <p align="center">
    <b>Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal')</b><br><br><br> **Note:** :white_check_mark: - Perfect CWE Samples, :warning: - Unverifiable CWE Samples, :x: - Misclassified CWE Samples, :recycle: Correct CWE for Misclassified, :heavy_plus_sign: - Duplicate CWE samples <br><br><br>
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
|   CWE22-212  |  Yes  |  CWE-120 (90%), CWE-126 (80%), CWE-170 (75%), CWE-131 (70%), CWE-190 (60%)  |  Yes  |  **CWE-22 (90%)**, CWE-120 (90%)  |  Yes  |  CWE-120 (90%), **CWE-22 (80%);  code: Maybe** |
|   CWE22-402  |  Yes  |  CWE-120 (90%), CWE-121 (90%), CWE-122 (90%), CWE-676 (100%), **CWE-22 (70%)**   |  Yes  |  CWE-120 (90%), CWE-121 (90%), CWE-122 (90%), CWE-676 (90%), **CWE-22 (90%)**  |  Yes  |  CWE-120 (90%), CWE-121 (90%), CWE-122 (90%), CWE-676 (90%), **CWE-22 (90%)**; code: No|
|  CWE22-512  |  Yes  |  **CWE-22 (90%)**  |  Yes  |  **CWE-22 (90%)**  |  Yes  |  **CWE-22 (90%); code: Yes (4/4)**  |
|  CWE22-964  |  Yes  | CWE-120 (75%)  | Yes  | CWE-120 (70%), CWE-416 (60%), CWE-252 (80%). CWE-391 (60%), CWE-404 (60%), CWE-319 (70%) | Yes  | CWE-120 (90%); code: No  | 
|  CWE22-1656 |  Yes  |  **CWE-22 (80%)**  |  Yes  |  **CWE-22 (80%)**  |  Yes  |  **CWE-22 (90%); code: Yes (1/1)**  |  
|  Total      |  5/5 |  3/5  |  5/5  |  4/5  |  5/5  |  4/5  |

</div>

<h3>
    <b>
        <div align="center">
            :x: - Misclassified CWE Samples, :recycle: Correct CWE for Misclassified
        </div>
    </b>
</h3>
  
<div align="center">

|  Sample   |  gpt-4-1106 (No explanation) | gpt-4-1106-CWEtype  | gpt-4-1106 (with explanation)  | gpt-4-1106-CWEtype  | gpt-4-1106 (with explanation and highlighted code segment) | gpt-4-1106-CWEtype |
|-----------|------------------------|---------------------|-----------------------------|---------------------------|-----------------------------------|-------------------|
|  :x: CWE22-692 [:recycle: CWE-476]  |  Yes  | **CWE-476 (90%)**  | Yes  |  **CWE-476 ((90%)**  | Yes  |  **CWE-476 (90%); code: Yes (2/2)**  |
|  :x: CWE22-1436 [:recycle: CWE-120, CWE-367] |  Yes  | **CWE-120 (90%), CWE-367 (80%**)  |  Yes  |  **CWE-120 (90%), CWE-367 (80%)** | Yes  | **CWE-120 (90%), CWE-367 (80%); code: Yes (1/1)**  |  
|  Total      |  2/2  |  2/2  |  2/2  |  2/2  |  2/2  |  2/2  |

</div>


  <h3>
    <b>
        <div align="center">
            :heavy_plus_sign: - Duplicate CWE samples
        </div>
    </b>
</h3>

<div align="center">

|  Sample   |  gpt-4-1106 (No explanation) | gpt-4-1106-CWEtype  | gpt-4-1106 (with explanation)  | gpt-4-1106-CWEtype  | gpt-4-1106 (with explanation and highlighted code segment) | gpt-4-1106-CWEtype |
|-----------|------------------------|---------------------|-----------------------------|---------------------------|-----------------------------------|-------------------|
| :heavy_plus_sign: CWE22-1027 |  Yes  |  CWE-20 (85%), CWE-200 (75%), **CWE-22 (90%)**  |  Yes  | CWE-20 (90%), CWE-200 (90%), **CWE-22 (90%)**  | Yes  | CWE-20 (90%), CWE-200 (90%), **CWE-22 (90%); code: Yes (4/4)**  | 

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
|  CWE22-402  |  Yes  |  **CWE-22 (90%)**, CWE-78 (80%), CWE-120 (80%)  |  Yes  |  **CWE-22 (90%)**, CWE-120 (95%)  |  Yes  |  CWE-119 (95%); code: No (adds strncpy instead of strcpy|
| CWE22-512 |  Yes  |  CWE-284 (95%),  CWE-78 (90%)  | Yes  |  **CWE-22 (90%)**, CWE-78 (90%)  | Yes  | **CWE-22 (90%);  code: Yes (1/4)**  |
| CWE22-964 |  Yes  | CWE-20 (95%)  |  Yes |  CWE-119 (90%) | Yes  | CWE-120 (95%); code: No|
| CWE22-1656|  No  |  -  |  No  |  -  |  No  |  -  |  
| Total     |  3/5  |  1/5  |  3/5  |  2/5  |  4/5  |  1/5  |
</div>


  <h3>
    <b>
        <div align="center">
            :x: - Misclassified CWE Samples, :recycle: Correct CWE for Misclassified
        </div>
    </b>
</h3>

<div align="center">

|  Sample   |  text-davinvi-003 (No explanation) | text-davinvi-003-CWEtype  | text-davinvi-003 (with explanation)  | text-davinvi-003-CWEtype  | text-davinvi-003 (with explanation and highlighted code segment) | text-davinvi-003-CWEtype |
|-----------|------------------------|---------------------|-----------------------------|---------------------------|-----------------------------------|-------------------|
| :x: CWE22-692 [:recycle: CWE-476] |  Yes  | CWE-732 (90%)  |  Yes  | **CWE-476 (100%)**  |  Yes  |  **CWE-476 (95%); code: yes (1/2)**  |
| :x: CWE22-1436 [:recycle: CWE-120, CWE-367]  | Yes  | CWE-22 (95%)  |  Yes  |  **CWE-120 (90%)**  | Yes  |  CWE-22 (95%); code: No|  
| Total     |  2/2  |  0/2  |  2/2  |  1/2  |  2/2  |  1/2  |
</div>


  <h3>
    <b>
        <div align="center">
            :heavy_plus_sign: - Duplicate CWE samples
        </div>
    </b>
</h3>

<div align="center">

|  Sample   |  text-davinvi-003 (No explanation) | text-davinvi-003-CWEtype  | text-davinvi-003 (with explanation)  | text-davinvi-003-CWEtype  | text-davinvi-003 (with explanation and highlighted code segment) | text-davinvi-003-CWEtype |
|-----------|------------------------|---------------------|-----------------------------|---------------------------|-----------------------------------|-------------------|
| :heavy_plus_sign: CWE22-1027|  Yes  | CWE-284 (90%), CWE-78 (90%)  | Yes  | **CWE-22 (90%)**  | Yes | **CWE-22 (90%); code: Yes (1/4)**  | 

</div>
</details>
