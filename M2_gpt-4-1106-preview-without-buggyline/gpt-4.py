import openai

openai.api_key = "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"
print("We are going to query the model now!!")

prefix="The Original Code is vulnerable to CWE-79: Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting'). Fix the vulnerability."
code="static int oidc_handle_session_management_iframe_rp ( request_rec * r , oidc_cfg * c , oidc_session_t * session , const char * client_id , const char * check_session_iframe ) { oidc_debug ( r , \"enter\" ) ; const char * java_script = \"<script type=\\\\\"text/javascript\\\\\">\\\\n\" \" var targetOrigin  = \\'%s\\';\\\\n\" \" var message = \\'%s\\' + \\' \\' + \\'%s\\';\\\\n\" \"\\t   var timerID;\\\\n\" \"\\\\n\" \"function checkSession() {\\\\n\" \" console.debug(\\'checkSession: posting \\' + message + \\' to \\' + targetOrigin);\\\\n\" \"var win = window.parent.document.getElementById(\\'%s\\').contentWindow;\\\\n\" \"win.postMessage( message, targetOrigin);\\\\n\" \"}\\\\n\" \"\\\\n\" \" function setTimer() {\\\\n\" \"checkSession();\\\\n\" \"timerID = setInterval(\\'checkSession()\\', %s);\\\\n\" \"}\\\\n\" \"\\\\n\" \"function receiveMessage(e) {\\\\n\" \"console.debug(\\'receiveMessage: \\' + e.data + \\' from \\' + e.origin);\\\\n\" \"if (e.origin !== targetOrigin ) {\\\\n\" \"console.debug(\\'receiveMessage: cross-site scripting attack?\\');\\\\n\" \"return;\\\\n\" \"}\\\\n\" \"if (e.data != \\'unchanged\\') {\\\\n\" \"clearInterval(timerID);\\\\n\" \"if (e.data == \\'changed\\') {\\\\n\" \"\\t\\t  window.location.href = \\'%s?session=check\\';\\\\n\" \"} else {\\\\n\" \"\\t\\t  window.location.href = \\'%s?session=logout\\';\\\\n\" \"}\\\\n\" \"}\\\\n\" \"}\\\\n\" \"\\\\n\" \"window.addEventListener(\\'message\\', receiveMessage, false);\\\\n\" \"\\\\n\" \"</script>\\\\n\" ; char * origin = apr_pstrdup ( r -> pool , check_session_iframe ) ; apr_uri_t uri ; apr_uri_parse ( r -> pool , check_session_iframe , & uri ) ; char * p = strstr ( origin , uri . path ) ; * p = '\\\\0' ; const char * op_iframe_id = \"openidc-op\" ; const char * session_state = oidc_session_get_session_state ( r , session ) ; if ( session_state == NULL ) { oidc_warn ( r , \"no session_state found in the session; the OP does probably not support session management!?\" ) ; return DONE ; } char * s_poll_interval = NULL ; oidc_util_get_request_parameter ( r , \"poll\" , & s_poll_interval ) ; if ( s_poll_interval == NULL ) s_poll_interval = \"3000\" ; const char * redirect_uri = oidc_get_redirect_uri ( r , c ) ; java_script = apr_psprintf ( r -> pool , java_script , origin , client_id , session_state , op_iframe_id , s_poll_interval , redirect_uri , redirect_uri ) ; return oidc_util_html_send ( r , NULL , java_script , \"setTimer\" , NULL , DONE ) ; }"
suffix="Fixed code:"
#suffix="Fixed code: Lets think step-by-step"

response = openai.ChatCompletion.create(
  model="gpt-4",
  messages=[
    {
      "role": "system",
      "content": "Assistant is an intelligent code repair system designed to help users fix vulnerabilities related to CWE-79: Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting'). Just fix the code. Don't provide any reasoning."
    },
    {
      "role": "user",
      "content": f"{prefix}\nOriginal code:\n{code}\n\n{suffix}"
    }
  ],
  temperature=0.8,
  max_tokens=1000,
  top_p=1,
  n=50,
  frequency_penalty=0,
  presence_penalty=0
)

print(response)
# print("<------------This is first----------->")
# print(response.choices[0]["message"])
# print("<------------This is second----------->")
# print(response.choices[1]["message"]["content"])
# # print("<------------This is third----------->")
# # print(response.choices[2]["message"]["content"])

import csv
#os.mkdir("CWE-22")
with open("Top_10_Most_Dangerous/CWE79/without_buggyline/CWE79-856.csv", "w", newline="") as csvfile:
    writer= csv.writer(csvfile)
    writer.writerow(["Original code","Plausible Program"])
    print("we are writing in the file now")
    for i in range(0,50):
        print(f'The {i+1}st response is done')
        writer.writerow([f"{prefix}\nOriginal Code:\n{code}\n{suffix}",response.choices[i]["message"]])
    print("\n\nThe response is done!!!!\n\n")
