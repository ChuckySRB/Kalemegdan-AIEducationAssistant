import os
import random
from grazie.api.client.gateway import AuthType, GrazieApiGatewayClient,GrazieHeaders
from grazie.api.client.chat.prompt import ChatPrompt
from grazie.api.client.endpoints import GrazieApiGatewayUrls
from grazie.api.client.profiles import Profile


def parse_response(response):
    info = {}
    current_section = None
    for line in response.content.split('\n'):
        if line.startswith("<<"):
            current_section = line[2:-2]
            info[current_section] = []
        elif current_section:
            info[current_section].append(line.strip())
    return info

token ="eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJHcmF6aWUgQXV0aGVudGljYXRpb24iLCJ1aWQiOiJhYmQ1MDQxOS0xMjQ2LTQzMWUtYjI0ZC01N2I3ZTMxNzUwNDEiLCJ0eXBlIjoiY3VzdG9tIiwibGljZW5zZSI6ImN1c3RvbV9hcHA6YjNmNjEwODgtYjcxYy00MGY2LWE4MmYtNDY2MjM1YWE0ZTYyIiwibGljZW5zZV90eXBlIjoiamV0YnJhaW5zLWFpLmFwcGxpY2F0aW9uLnN0YW5kYXJkIiwiZXhwIjoxNzEwNDQ2MTAwfQ.lz482uMjAKcTXyggXiL-4g2W-03w-5DwQ4dN7WkHPB3oKeb1QH9RzOG0fzoU1u_f2yFiT7PG-DYWVIEVtcSm9UvoIKFVJHJYeuWnTfndZSCvfaiKvfd4jrteMa0ZNh6mdigfObeOcVTUd5TRE1nXKDBMs5R6lvYJt5JnISNsSa3ze8jQlHOTXDRgbCKJfkSxUpjkrx7es1Zzeq-KlvrsyJZssjv9djrr06yVNgr0BFYVGJYZXTKbzuzj75oyNOuQyGpzev9j-NytR9dwFf-19QkYwVEEoAUaGpfSu_zKGWG-mA9iygDSowfVMqAZDQXDr7GGKTRxGIBKleMnAEkesQ"
# In a real application, you would have to supply the client's IP address
client_ip = "{}.{}.{}.{}".format(*[str(random.randint(0, 255)) for octet
in range(4)])

get_time = lambda f: os.stat(f).st_ctime



#Zadavanje Problema
pre_setting="You are teaching an aspiring programmer with he is trying to finish this Programing Course Task(Give Answers in bullet points):"
setting=pre_setting+\
        " You are given two non-empty linked lists" \
        " representing two non-negative integers. The digits are stored in reverse order," \
        " and each of their nodes contains a single digit. Add the two numbers and return the" \
        " sum as a linked list.You may assume the two numbers do not contain any leading zero," \
        " except the number 0 itself."
context="None"
format="Format of you answer should be: " \
       "1) section <<HINTs>> with Independent Numbered Bullet points (that should all be independent from one another) " \
       "that should not spoil the asnwer to the coder " \
       "2) section <<QUESTIONS TO GET THE ANSWER EASIER>>  " \
       "3) section <<TIPS>> with Independent Numbered Bullet points (that should all be independent from one another) " \
       "4) section <<TIME COMPLEXITY>> Where you should ONLY give tips on how to decrease time complexity if possible" \
       "5) section <<SPACE COMPLEXITY>> Where you should ONLY give tips on how to decrease space complexity if possible" \
       "6) section <<CORRECT ANSWER:>> with corrected code. "
new_content="/** \
 * Definition for singly-linked list. \
 * struct ListNode { \
 *     int val; \
 *     ListNode *next; \
 *     ListNode() : val(0), next(nullptr) {} \
 *     ListNode(int x) : val(x), next(nullptr) {} \
 *     ListNode(int x, ListNode *next) : val(x), next(next) {} \
 * }; \
 */ \
class Solution { \
public: \
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) { \
        int sum; \
        int carry = 0; \
        ListNode* curr1 = l1; \
        ListNode* curr2 = l2; \
        while (curr1 != nullptr && curr2 != nullptr) { \
            sum = curr1->val + curr2->val + carry; \
            curr1->val = sum % 10; \
            carry = sum / 10; \
            curr1 = curr1->next; \
            curr2 = curr2->next; \
        }\
        return l1;\
    }\
};"
whole_prompt="Your setting: "+setting\
            +format\
             +"Your Context of pevious entries:"\
             +context+"Your content: "\
             +new_content
print(new_content)

client = GrazieApiGatewayClient(
    url=GrazieApiGatewayUrls.STAGING,
    grazie_jwt_token=token,
    auth_type=AuthType.APPLICATION,
)
response = client.chat(
    chat=(
        ChatPrompt().add_system("You are a helpful assistant.").add_user(whole_prompt)
    ),
    profile=Profile.OPENAI_GPT_4,
    headers={
        GrazieHeaders.ORIGINAL_USER_IP: client_ip,
    }
)
print("HELPFUL ASSISTANT---------------------------------------------------------------------")


# Parse response into dictionary

#Parse response into dictionary

print(parse_response(response))

print(response.content)

response = client.chat(
    chat=(
        ChatPrompt().add_system("You are a professional programmer.").add_user(whole_prompt)
    ),
    profile=Profile.OPENAI_GPT_4,
    headers={
        GrazieHeaders.ORIGINAL_USER_IP: client_ip,
    }
)
print("PROFESIONAL PROGRAMMER-----------------------------------------------------------------")
print(response.content)



response = client.chat(
    chat=(
        ChatPrompt().add_system("You give very light tips.").add_user(whole_prompt)
    ),
    profile=Profile.OPENAI_GPT_4,
    headers={
        GrazieHeaders.ORIGINAL_USER_IP: client_ip,
    }
)
print("Lil Tips-----------------------------------------------------------------")
print(response.content)

response = client.chat(
    chat=(
        ChatPrompt().add_system("You are a strict professor.").add_user(whole_prompt)
    ),
    profile=Profile.OPENAI_GPT_4,
    headers={
        GrazieHeaders.ORIGINAL_USER_IP: client_ip,
    }
)
print("Strict Professor-----------------------------------------------------------------")
print(response.content)