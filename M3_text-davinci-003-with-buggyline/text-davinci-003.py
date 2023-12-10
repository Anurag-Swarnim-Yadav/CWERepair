import os
import openai

openai.api_key = "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"
print("We are going to query the model now!!")

prefix="The Original Code is vulnerable to CWE-416: Use After Free. Fix the code between <StartBug> and <EndBug> to fix the vulnerability."
code="int sctp_do_peeloff ( struct sock * sk , sctp_assoc_t id , struct socket * * sockp ) { struct sctp_association * asoc = sctp_id2assoc ( sk , id ) ; struct sctp_sock * sp = sctp_sk ( sk ) ; struct socket * sock ; <StartBug> int err = 0 ; <EndBug> if ( ! asoc ) return - EINVAL ; if ( waitqueue_active ( & asoc -> wait ) ) return - EBUSY ; if ( ! sctp_style ( sk , UDP ) ) return - EINVAL ; err = sock_create ( sk -> sk_family , SOCK_SEQPACKET , IPPROTO_SCTP , & sock ) ; if ( err < 0 ) return err ; sctp_copy_sock ( sock -> sk , sk , asoc ) ; sp -> pf -> to_sk_daddr ( & asoc -> peer . primary_addr , sk ) ; sctp_sock_migrate ( sk , sock -> sk , asoc , SCTP_SOCKET_UDP_HIGH_BANDWIDTH ) ; * sockp = sock ; return err ; }"
suffix="Fixed code:"
Number_of_bugs_present=1
#suffix="Fixed code: Lets think step-by-step"

response = openai.Completion.create(
  model="text-davinci-003",
  #prompt=prompt,
  prompt=f"{prefix}\nOriginal Code:\n{code}\n{suffix}",
  temperature=0.8,
  max_tokens=1000,
  top_p=1,
  n=50,
  #best_of=5,
  frequency_penalty=0,
  logprobs=2,
  presence_penalty=0,
  #echo=True
)

# print(response)

import csv
#os.mkdir("CWE-22")
with open("Top_10_Most_Dangerous/CWE416/with_buggyline/CWE416-1663.csv", "w", newline="") as csvfile:
    writer= csv.writer(csvfile)
    writer.writerow(["Original code","Plausible Program","Number of Bugs Present","Total Tokens","Sum Entropy","Mean Entropy"])
    print("we are writing in the file now")
    for i in range(0,50):
        print(f'The {i+1}st response is done')
        #print(response.choices[i]["text"])
        
        num=0
        count=0
        token_list=response.choices[i]["logprobs"]["token_logprobs"]
        for item in token_list:
            if item is not None:
                num=num+(item)
                count=count+1

        average=num/count

        #print(num)
        #print(count)

        writer.writerow([f"{prefix}\nOriginal Code:\n{code}\n{suffix}",response.choices[i]["text"],Number_of_bugs_present,count,num,average])
        #print(response.choices[i]["logprobs"]["token_logprobs"])
    print("\n\nThe response is done!!!!\n\n")