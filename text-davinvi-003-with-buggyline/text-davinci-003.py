import os
import openai

openai.api_key = "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"
print("We are going to query the model now!!")

prefix="The Original Code is vulnerable to CWE-416: Use After Free. Fix the vulnerability."
code="void inet6_destroy_sock ( struct sock * sk ) { struct ipv6_pinfo * np = inet6_sk ( sk ) ; struct sk_buff * skb ; struct ipv6_txoptions * opt ; skb = xchg ( & np -> pktoptions , NULL ) ; if ( skb ) kfree_skb ( skb ) ; skb = xchg ( & np -> rxpmtu , NULL ) ; if ( skb ) kfree_skb ( skb ) ; fl6_free_socklist ( sk ) ; opt = xchg ( & np -> opt , NULL ) ; if ( opt ) sock_kfree_s ( sk , opt , opt -> tot_len ) ; }"
suffix="Fixed code:"
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
with open("Top_10_Most_Dangerous/CWE416/without_buggyline/CWE416-744.csv", "w", newline="") as csvfile:
    writer= csv.writer(csvfile)
    writer.writerow(["Original code","Plausible Program","Total Tokens","Sum Entropy","Mean Entropy"])
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

        writer.writerow([f"{prefix}\nOriginal Code:\n{code}\n{suffix}",response.choices[i]["text"],count,num,average])
        #print(response.choices[i]["logprobs"]["token_logprobs"])
    print("\n\nThe response is done!!!!\n\n")