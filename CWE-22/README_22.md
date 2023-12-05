<p align="center">
  </a>
  <h3 align="center">CWE-22</a></h3>
  <p align="center">
    Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal')
  </p>
</p>
<div align="center">

## Real-World Software Vulnerabilities

</div>

<details open="open">
<summary>CWE-22: Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal')</summary>

<h3>
    <b>
        <div align="center">
            Detection Performance on all the samples of CWE-22
        </div>
    </b>
</h3>
  
<div align="center"> Detection Performance of gpt-4-preview in three different settings. Here, W or Y as a prefix for the CWEtype column determines if the model classifies the CWE wrong or correctly. 

|  Sample   |  gpt-4-1106 (No explanation) | gpt-4-1106-CWEtype  | gpt-4-1106 (with explanation)  | gpt-4-1106-CWEtype  | gpt-4-1106 (with explanation and highlighted code segment) | gpt-4-1106-CWEtype |
|-----------|------------------------|---------------------|-----------------------------|---------------------------|-----------------------------------|-------------------|
|  CWE22-212  |  Yes  |  CWE-120 (90%), CWE-126 (80%), CWE-170 (75%), CWE-131 (70%) CWE-190 (80%)  |  Yes  |  **CWE-22 (90%)**  |  Yes  |  **CWE-22 (80%);  code: Yes** |

|  CWE22-402  |  -  |  -  |  -  |  -  |  -  |  -  |  
|  CWE22-512  |  Yes  |  CWE-22 (90%)  |  Yes  |  CWE-22 (90%)  |  Yes  |  **CWE-22 (90%); code: Yes**  |
|  CWE22-692  |  Yes  | CWE-476 ((90%)  | Yes  |  CWE-476 ((90%)  | Yes  | CWE-476 (90%); **code: Yes**  |
|  CWE22-964  |  
|  CWE22-1027 | 
|  CWE22-1436 |  
|  CWE22-1656 | 
|  Total      |

</div>

<div align="center"> Detection Performance of text-davinvi-003 in three different settings. Here, W or Y as a prefix for the CWEtype column determines if the model classifies the CWE wrong or correctly.

|  Sample   |  text-davinvi-003 (No explanation) | text-davinvi-003-CWEtype  | text-davinvi-003 (with explanation)  | text-davinvi-003-CWEtype  | text-davinvi-003 (with explanation and highlighted code segment) | text-davinvi-003-CWEtype |
|-----------|------------------------|---------------------|-----------------------------|---------------------------|-----------------------------------|-------------------|
|  CWE22-212  |  No  |  -  | No  |  -  |  Yes  |  CWE-119;  **code: Maybe**  |
|  CWE22-402  |  -  |  -  |  -  |  -  |  -  |  -|
| CWE22-512 |  Yes  |  CWE-284 (95%),  CWE-78 (90%)  | Yes  |  CWE-22 (90%)  | Yes  | **CWE-22 (90%);  code: Yes**  |
| CWE22-692 |  Yes  | CWE-732 (90%)  |  Yes  | CWE-476 (100%)  | CWE-476 (95%); **code: yes**  |
| CWE22-964 |
| CWE22-1027|
| CWE22-1436|
| CWE22-1656|
| Total     |
</div>
</details>
