<p align="center">
  </a>
  <h3 align="center">CWE-352</a></h3>
  <p align="center">
    Cross-Site Request Forgery (CSRF)<br><br><br> **Note:** :warning: - Unverifiable CWE Samples, :x: - misclassified CWE samples, :recycle: correct CWE for misclassified, :heavy_plus_sign: - Duplicate CWE samples <br><br><br>
  </p>
</p>
<div align="center">

## Real-World Software Vulnerabilities

</div>

<details open="open">
<summary>CWE-352: Cross-Site Request Forgery (CSRF)</summary>

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
|  :x: CWE352-1540 [:recycle: CWE-352, CWE-79]  |  Yes  |  **CWE-79 (80%)**   |  Yes  |  **CWE-79 (90%)**, CWE-200 (80%), CWE-120 (60%), CWE-306 (70%)                              |  Yes  |  **CWE-79 (90%)**; code:Don't Know  |
|  :x: CWE352-1580 [:recycle: CWE-352, CWE-319]  |  Yes  |  **CWE-319 (90%)**  |  Yes  |  CWE-120 (70%), CWE-20 (80%), **CWE-319(90%)**, CWE-259(50%), CWE-401 (70%), CWE-755 (60%)  |  Yes  |  **CWE-319 (90%)**; **code:1/2**  | 
|  Total                                       |  2/2  |  0/2            |  2/2  |  0/2                                                                                    |  2/2  |  0/2                          |

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
| :x: CWE352-1540 [:recycle: CWE-352, CWE-79]  |  No  |  -             |  Yes  |  CWE-120 (95%)  |  Yes  |  CWE-120 (90%); code: Don't Know  |
| :x: CWE352-1580 [:recycle: CWE-352, CWE-319]  |  Yes |  CWE-20 (90%)  |  Yes  |  CWE-20 (90%)   |  Yes  |  CWE-20 (90%); code: No  |
|  Total        |  1/2 |  0/2           |  2/2  |  0/2            |  2/2  |  0/2                     |
</div>
</details>
