import openai

openai.api_key = "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"
prefix="#C Language\nThe Original Code is vulnerable to CWE-119: Improper Restriction of Operations within the Bounds of a Memory Buffer. Fix the vulnerability."
code="void * H264SwDecMalloc ( u32 size, u32 num) { return malloc (size) ;}"
suffix="Fixed code:"
#suffix="Fixed code: Lets think step-by-step"

response = openai.ChatCompletion.create(
  model="gpt-4",
#   messages=[
#     {
#       "role": "user",
#       "content": "# C Language\nThe Original Code is vulnerable to CWE-119: Improper Restriction of Operations within the Bounds of a Memory Buffer. Fix the vulnerability.\nOriginal code: void * H264SwDecMalloc ( u32 size, u32 num) { return malloc (size) ;}\nFixed code: Lets think step-by-step"
#     }
#   ],
  messages=[
    {
      "role": "user",
      "content": f"{prefix}\nOriginal code:\n{code}\n\n{suffix}"
    }
  ],
  temperature=0.8,
  max_tokens=500,
  top_p=1,
  n=10,
  frequency_penalty=0,
  presence_penalty=0
)

# print(response)



import csv
with open("gpt-4.csv", "w", newline="") as csvfile:
    writer= csv.writer(csvfile)
    writer.writerow(["Original Code", "Patched Program"])
    print("we are writing in the file now")
    for i in range(0,10):
        print(f'This is the {i+1} response')
        writer.writerow([f"{prefix}\nOriginal code:\n{code}\n\n{suffix}",response.choices[i]["message"]["content"]])
        #print(response.choices[i]["logprobs"]["token_logprobs"])
    print("\n\nThe response is done!!!!\n\n")