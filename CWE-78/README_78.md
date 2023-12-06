<p align="center">
  </a>
  <h3 align="center">CWE-78</a></h3>
  <p align="center">
    Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection')
  </p>
</p>
<div align="center">

## Real-World Software Vulnerabilities

</div>

<details open="open">
<summary>CWE-78: Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection')</summary>

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
|  :warning: :triangular_flag_on_post: CWE78-1012  |  
|  :mag: :heavy_exclamation_mark: CWE78-1149  |  
|  :mag: :heavy_exclamation_mark: CWE78-1502  |
|  Total                                      |

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
|  :warning: :triangular_flag_on_post: CWE78-1012  |  No   |  -              |  Yes  |  CWE-119 (90%)     |  Yes  |  CWE-120 (90%); code: No      |
|  CWE78-1149  |  Yes  |  CWE-843 (90%)  |  Yes  |  CWE-120 (90%)     |  Yes  |  CWE-120 (95%); code: No      |
|  CWE78-1502  |  No   |  -              |  Yes  |  **CWE-78 (95%)**  |  Yes  |  **CWE-78 (100%)**; code: No  |
|  Total       |  1/3  |  0/3            |  3/3  |  1/3               |  3/3  |  1/3                          |
</div>
</details>
