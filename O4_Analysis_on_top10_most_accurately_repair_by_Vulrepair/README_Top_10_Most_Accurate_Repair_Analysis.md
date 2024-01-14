
<h3>
    <b>
        <div align="center">
            Top-10 Most Accurately Repaired CWE Types of VulRepair (NIST Verification)
        </div>
    </b>
</h3>

<div align="center">
  
|    Sample        | CWE Type |                      Name                         |    NIST       |
|:----------------:|:--------:|:-------------------------------------------------:|:-------------:|
|    CWE755-220    |  CWE-755 |    Improper Handling of Exceptional Conditions    |    Yes        | 
|    CWE706-839    |  CWE-706 |    Use of Incorrectly-Resolved Name or Reference  |    CWE-863    |  
|    CWE326-104    |  CWE-326 |    Inadequate Encryption Strength                 |    Yes        |
|    CWE326-489    |  CWE-326 |    Inadequate Encryption Strength                 |    Yes        |  
|    CWE667-1597   |  CWE-667 |    Improper Locking                               |    Yes        |   
|    CWE369-218    |  CWE-369 |    Divide By Zero                                 |    Yes        |
|    CWE369-358    |  CWE-369 |    Divide By Zero                                 |    Yes        |
|    CWE369-407    |  CWE-369 |    Divide By Zero                                 |    Yes        |
|    CWE369-628    |  CWE-369 |    Divide By Zero                                 |    Yes        |
|    CWE369-768    |  CWE-369 |    Divide By Zero                                 |    Yes        |
|    CWE77-126     |  CWE-77  |    Command Injection                              |    CWE-78     |
|    CWE77-1608    |  CWE-77  |    Command Injection                              |    Yes        |
|    CWE388-1702   |  CWE-388 |    Error Handling                                 |    Yes        |
|    CWE436-592    |  CWE-436 |    Interpretation Conflict                        |    Yes        |
|    CWE191-410    |  CWE-191 |    Integer Underflow                              |    Yes        |
|    CWE191-685    |  CWE-191 |    Integer Underflow                              |    Yes        |
|    CWE285-128    |  CWE-285 |    Improper Access Control                        |    Yes        |
|    CWE285-288    |  CWE-285 |    Improper Access Control                        |    Yes        |
|    CWE285-465    |  CWE-285 |    Improper Access Control                        |    Yes        |
|    CWE285-706    |  CWE-285 |    Improper Access Control                        |    Yes        |
|    CWE285-881    |  CWE-285 |    Improper Access Control                        |    Yes        |
|    CWE285-1098   |  CWE-285 |    Improper Access Control                        |    Yes        |
| CWE285-1389 (D: CWE285-465) |  CWE-285 |    Improper Access Control             |    Yes        |
|    CWE285-1500   |  CWE-285 |    Improper Access Control                        |    Yes        |
|                  |          |    TOTAL                                          |    2/24       |

</div> 

<br>
<br>
<br>

<h3>
    <b>
        <div align="center">
            Top-10 Most Accurately Repaired CWE Types of VulRepair (Training and Validation Samples Verification)
        </div>
    </b>
</h3>

<div align="center">
  
|    Sample        | CWE Type |        Name        |    VulRepair Correctly Predicted       | Present in Train Dataset| Number of Sample Present | CWE Type of Sample |
|:----------------:|:--------:|:------------------:|:--------------------------------------:|:-----------------------:|:-------------------------:|:--------------------|
|    CWE755-220    |  CWE-755 |    Improper Handling of Exceptional Conditions    |    Yes        |    Yes        |
|    CWE706-839    |  CWE-706 |    Use of Incorrectly-Resolved Name or Reference  |    Yes        |    No         |  
|    CWE326-104    |  CWE-326 |    Inadequate Encryption Strength                 |    Yes        |    Yes        |
|    CWE326-489    |  CWE-326 |    Inadequate Encryption Strength                 |    Yes        |    Yes        |  
|    CWE667-1597   |  CWE-667 |    Improper Locking                               |    Yes        |    Yes        |   
|    CWE369-218    |  CWE-369 |    Divide By Zero                                 |    Yes        |    Yes        |
|    CWE369-358    |  CWE-369 |    Divide By Zero                                 |    Yes        |    Yes        |
|    CWE369-407    |  CWE-369 |    Divide By Zero                                 |    Yes        |    Yes        |
|    CWE369-628    |  CWE-369 |    Divide By Zero                                 |    Yes        |    Yes        |
|    CWE369-768    |  CWE-369 |    Divide By Zero                                 |    Yes        |    Yes        |
|    CWE77-126     |  CWE-77  |    Command Injection                              |    Yes        |    Yes        |
|    CWE77-1608    |  CWE-77  |    Command Injection                              |    Yes        |    Yes        |
|    CWE388-1702   |  CWE-388 |    Error Handling                                 |    Yes        |    No         | 
|    CWE436-592    |  CWE-436 |    Interpretation Conflict                        |    Yes        |    Yes        |
|    CWE191-410    |  CWE-191 |    Integer Underflow                              |    Yes        |    Yes        |
|    CWE191-685    |  CWE-191 |    Integer Underflow                              |    Yes        |    Yes        |
|    CWE285-128    |  CWE-285 |    Improper Access Control                        |    Yes        |    Yes        |
|    CWE285-288    |  CWE-285 |    Improper Access Control                        |    Yes        |    Yes        |
|    CWE285-465    |  CWE-285 |    Improper Access Control                        |    No         |    Yes        |
|    CWE285-706    |  CWE-285 |    Improper Access Control                        |    Yes        |    No         |
|    CWE285-881    |  CWE-285 |    Improper Access Control                        |    Yes        |    Yes        |
|    CWE285-1098   |  CWE-285 |    Improper Access Control                        |    Yes        |    No         |
| CWE285-1389 (D: CWE285-465) |  CWE-285 |    Improper Access Control             |    No         |    Yes        |
|    CWE285-1500   |  CWE-285 |    Improper Access Control                        |    Yes        |    Yes        |
|                  |          |    TOTAL                                          |    22/24      |

</div> 

<br>
<br>

<div align="center">
  
| No   | CWE Type |                      Name                           |  %PP | Proportion | Present in Validation  |  Number of Samples| CWEtype |
|:----:|:--------:|:---------------------------------------------------:|:----:|:----------:|:-----------------:|:--------:|:----------------:|
|   7  |  CWE-388 |                 Error Handling                      | 100% |     1/1    | Yes (Validation)   | 2   | CWE-388   |
|  10  | CWE-285-1098 |            Improper Access Control              | 100% |     1/1    | Yes (Validation)   | 1   | CWE-285 |

</div>


