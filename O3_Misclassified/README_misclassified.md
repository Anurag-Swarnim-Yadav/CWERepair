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
            VulRepair Test Samples (Misclassified).
        </div>
    </b>
</h3>
  
<div align="center">

|  CWE Sample    | VulRepair Classified As  | Correct CWE       |  Reason  |
|----------------|--------------------------|-------------------|----------|
|  CWE352-1540   | CWE-352                  | CWE-352; CWE-79   | 1. CWE-352 is very difficult to understand, adding a security token in code  <br>2. Input is appended directed   |
|  CWE352-1580   | CWE-352                  | CWE-352; CWE-319  | 1. Add the CSRF token to the Post method in HTTP <br>2. Does not use HTTPS method (SSL protocol, can lead to clear text)  |
|  CWE78-1012    | CWE-78                   | Might represent additional flags or options for the connection  | 1. Before fix - The function r_socket_http_post concludes with a call to r_socket_http_answer(s, code, rlen). This suggests that it is designed to read the HTTP response from the server, with s being the socket, and code and rlen being pointers to store the status code and response length, respectively.<br>2. After fix- The last line is return socket_http_answer(s, code, rlen, 0). The additional parameter (0 in this case) could indicate an extra configuration or behavior modification for the socket_http_answer function. Without the definition of this function, it's hard to determine the exact purpose of this parameter.  |
|  CWE22-692     | CWE-22                   | CWE-476           |  1. The main changes the program deals with are focusing solely on logging and calling percpu_ref_put on top ->remote_lun_ref.<br> 2. It removes the variable remote_dev and the associated conditional assignments and operations.<br> 3. The purpose of the function has shifted from manipulating an item related to remote_dev to simply decrementing a reference counter (percpu_ref_put) and logging the operation.<br>4. The function dereferences the pointer xop multiple times (xop->op_origin, xop->dst_dev, xop->src_dev, xop->remote_lun_ref).<br>5. The code does not explicitly check if xop or the fields within xop (like dst_dev, src_dev, remote_lun_ref) are null before accessing them.  |
|  CWE22-1436   |  CWE-22                  | CWE-120, CWE-367  | 1. The name string has no information. It does not say what it is and how it is used.<br> 2. There are vulnerabilities related to "iface" variable  and "access" function that can lead to CWE-120 or CWE-787, and CWE-367. See the explanation in the detection folder.  |
|  CWE-89-1484  | CWE-89  |  CWE-120  |  1. Changing strindex from an int to a size_t is a significant improvement. size_t is an unsigned type that is specifically designed for measuring the size of objects and is commonly used for array indexing and loop counting in C.<br> 2. This change prevents potential issues with negative indices and aligns with best practices for array indexing.  |
| CWE89-1671/1691  | CWE-89  |  CWE-89, CWE-120  |1. Uses int for alloc and strindex. It needs to be size_t for alloc and strindex. This change is significant as size_t is an unsigned type and typically more suitable for sizes and indices.  |
|  CWE287-287   |  CWE-287  | No  CWE  | 1. oidc_scrub_headers is declared as static void. The static keyword in this context means it cannot be called from other source files, even if the function declaration is included in those files.<br> 2. The change is without the static keyword, meaning it has an external linkage. It has nothing to do with Improper Authentication.  |
|  CWE287-975   |  CWE-287  |  Missing the code  | 1. The required change is the addition of a boolean to the line err = scm_send(sock, msg, siocb->scm);. The correct change is err = scm_send(sock, msg, siocb->scm, false);<br> 2. We are missing the definition of the function; without the definition, it does not make sense but when the function is added. It makes sense that it has improper authentication. (ASK DR. WILSON)  |
|  CWE522-21    | CWE-522  |  CWE-755; CWE-287  | Check the NVD page: https://nvd.nist.gov/vuln/detail/CVE-2020-28896  |
|  CWE522-773    | CWE-522  |  Missing code | 1. tpm_kdfa function is part of CWE522-370 sample. This sample needs to be added to the other sample. Otherwise, This sample has no meaning.<br>2. Since in the other sample, an argument to the function is removed. |
|  CWE522-1655    | CWE-522  | CWE-20  | Based on the given code. Also, Check the NVD page: https://nvd.nist.gov/vuln/detail/CVE-2020-11008  |
|  CWE732-276   | CWE-732  | Code Duplicate  | There is no code change. I think they deleted some code changes. So they wrote back.  |
|  CWE732-1575  | CWE-732  |  CWE-459; CWE-909  | Check the NVD page: https://nvd.nist.gov/vuln/detail/CVE-2019-25016 |
|  CWE611-351   | CWE-611  | Garbage Sample  | The required change is "ModSecurity: Invalid value for SecRuleEngine: %s" to "ModSecurity: Invalid value for SexHasEngine: %s". It has nothing to do with CWE611  |
|  CWE918-806  |  CWE-918  |  CWE-20  | 1. Vulnerable Before - Uses atoi to convert the port number from a string to an integer. Lacks comprehensive error handling if the port number conversion fails or if the string contains invalid characters after the port number. Only returns an error message if there is no colon in the string.<br> 2. Fixed code -  Uses strtol for port number conversion and includes error checking. This is a significant improvement as strtol provides error handling capabilities, which atoi lacks. It checks if the entire string has been correctly converted into a number and handles any trailing characters that are not part of the number. Adds a check (if (e && *e)) after converting the port number to ensure that the entire string segment is a valid number. This additional error handling can prevent potential bugs or undefined behaviors when dealing with malformed input. Includes error handling for cases where the port number parsing fails in the IPv4 or general cases (i.e., if e is not NULL or *e is not the string terminator).<br> 3. Use of atoi: The atoi function used in the before code for converting the port number from a string does not gracefully handle numeric overflows or invalid input. atoi converts the initial portion of the string to an int and does not provide any mechanism for error checking. If the string contains a number that exceeds the range of an int, it could cause an integer overflow.<br> 4. SSRF vulnerabilities typically occur when a server makes a network request based on user-controlled input. Vulnerable code does not itself make network requests or handle URLs or endpoints for such requests, it does not directly pertain to the typical context of SSRF vulnerabilities.<br> 5. Also check Github: https://github.com/php/php-src/commit/bab0b99f376dac9170ac81382a5ed526938d595a comments |
|  CWE77-126  | CWE-77  |CWE-78; The give vulnerable program is incomplete | 1. See NVD website: https://nvd.nist.gov/vuln/detail/CVE-2018-14357<br> 2. The program itself is incomplete. |
|  CWE77-1602 | CWE-77  |  Incomplete program, change in argument can't define the vulnerability | 1. Vulnerable Program: run_cmd(tty_fd, xfr_cmd, fname, NULL); Fixed Program: run_cmd(tty_fd, xfr_cmd, fname);<br> 2. rub_cmd() function definition is missing  |
                                                                     
                                                                      
</div>
</details>
