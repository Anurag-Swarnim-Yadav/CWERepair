<p align="center">
  <h3 align="center"> Misclassified CWEs with sample</h3>
</p>
<div align="center">

## Real-World Software Vulnerabilities

</div>

<details open="open">
<summary>List of misclassified samples in Vulrepair Dataset</summary>

<h3>
    <b>
        <div align="center">
            Detection Performance of gpt-4-1106-preview in three different settings.
        </div>
    </b>
</h3>
  
<div align="center">

|  CWE Sample    | VulRepair Classified As  | Correct CWE       |  Reason  |
|----------------|--------------------------|-------------------|----------|
|  CWE352-1540   | CWE-352                  | CWE-352; CWE-79   | 1. CWE-352 is very difficult to understand, adding a security token in code  <br>2. Input is appended directed   |
|  CWE352-1580   | CWE-352                  | CWE-352; CWE-319  | 1. Add the CSRF token to the Post method in HTTP <br>2. Does not use HTTPS method (SSL protocol, can lead to clear text)  |
|  CWE78-1012    | CWE-78                   | Might represent additional flags or options for the connection  | Definitely not command injection for the given program and vulnerable line.  |
|  CWE22-692     | CWE-22                   | CWE-476           |  1. The main changes the program deals with are focusing solely on logging and calling percpu_ref_put on top ->remote_lun_ref.<br> 2. It removes                                                                         the variable remote_dev and the associated conditional assignments and operations.<br> 3. The purpose of the function has shifted from manipulating an item related to remote_dev to simply decrementing a reference counter (percpu_ref_put) and logging the operation.<br>4.The function dereferences the pointer xop multiple times (xop->op_origin, xop->dst_dev, xop->src_dev, xop->remote_lun_ref).<br>5. The code does not explicitly check if xop or the fields within xop (like dst_dev, src_dev, remote_lun_ref) are null before accessing them.  |
|  CWE22-1436    |  CWE-22                  | CWE-120, CWE-367  | 1) The name string has no information. It does not say what exact it is and where it is being used.<br> 2. There is vulnerabilities related to 
                                                                     "iface" variable  and "access" function that can lead CWE120 or CWE-787 and CWE-367. See if the explanation in the detection folder.  |
                                                                     
                                                                      
</div>
</details>
