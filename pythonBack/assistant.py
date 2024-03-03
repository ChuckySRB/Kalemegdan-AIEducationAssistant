import os
import random
from grazie.api.client.gateway import AuthType, GrazieApiGatewayClient,GrazieHeaders
from grazie.api.client.chat.prompt import ChatPrompt
from grazie.api.client.endpoints import GrazieApiGatewayUrls
from grazie.api.client.profiles import Profile


def parse_response(resp):
    info = {}
    current_section = None
    for line in resp.content.split('\n'):
        if line.startswith("<<"):
            current_section = line[2:-2]
            info[current_section] = []
        elif current_section:
            info[current_section].append(line.strip())
    return info


def grazie_assistant(client_ip, token, task_text, new_content, context):
    pre_setting = "You are teaching an aspiring programmer with he is trying to finish this Programming Course Task(Give Answers in bullet points):"
    setting = pre_setting + task_text

    format = "Format of your answer should be: " \
             "1) section <<HINTs>> with Independent Numbered Bullet points (that should all be independent from one another) " \
             "that should not spoil the answer to the coder " \
             "2) section <<QUESTIONS TO GET THE ANSWER EASIER>>  " \
             "3) section <<TIPS>> with Independent Numbered Bullet points (that should all be independent from one another) " \
             "4) section <<TIME COMPLEXITY>> Where you should ONLY(no need to tell me current complexity if its good) give tips on how to decrease time complexity if possible(with Independent Numbered Bullet points (that should all be independent from one another))" \
             "5) section <<SPACE COMPLEXITY>> Where you should ONLY(no need to tell me current complexity if its good) give tips on how to decrease space complexity if possible(with Independent Numbered Bullet points (that should all be independent from one another))" \
             "6) section <<CORRECT ANSWER:>> with corrected code. "

    whole_prompt = "Your setting: " + setting \
                   + format \
                   + "Your Context of previous entries:" \
                   + context + "Your content: " \
                   + new_content

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
    print(parse_response(response))
    print(response.content)


tokn ="eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJHcmF6aWUgQXV0aGVudGljYXRpb24iLCJ1aWQiOiJhYmQ1MDQxOS0xMjQ2LTQzMWUtYjI0ZC01N2I3ZTMxNzUwNDEiLCJ0eXBlIjoiY3VzdG9tIiwibGljZW5zZSI6ImN1c3RvbV9hcHA6YjNmNjEwODgtYjcxYy00MGY2LWE4MmYtNDY2MjM1YWE0ZTYyIiwibGljZW5zZV90eXBlIjoiamV0YnJhaW5zLWFpLmFwcGxpY2F0aW9uLnN0YW5kYXJkIiwiZXhwIjoxNzEwNDQ2MTAwfQ.lz482uMjAKcTXyggXiL-4g2W-03w-5DwQ4dN7WkHPB3oKeb1QH9RzOG0fzoU1u_f2yFiT7PG-DYWVIEVtcSm9UvoIKFVJHJYeuWnTfndZSCvfaiKvfd4jrteMa0ZNh6mdigfObeOcVTUd5TRE1nXKDBMs5R6lvYJt5JnISNsSa3ze8jQlHOTXDRgbCKJfkSxUpjkrx7es1Zzeq-KlvrsyJZssjv9djrr06yVNgr0BFYVGJYZXTKbzuzj75oyNOuQyGpzev9j-NytR9dwFf-19QkYwVEEoAUaGpfSu_zKGWG-mA9iygDSowfVMqAZDQXDr7GGKTRxGIBKleMnAEkesQ"
# In a real application, you would have to supply the client's IP address
cl_ip = "{}.{}.{}.{}".format(*[str(random.randint(0, 255)) for octet
in range(4)])

get_time = lambda f: os.stat(f).st_ctime

tekst_zadatka=" You are given two non-empty linked lists" \
              " representing two non-negative integers. The digits are stored in reverse order," \
              " and each of their nodes contains a single digit. Add the two numbers and return the" \
              " sum as a linked list.You may assume the two numbers do not contain any leading zero," \
              " except the number 0 itself."

pokusaj_resenja = "/** \
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

grazie_assistant(cl_ip, tokn, tekst_zadatka, pokusaj_resenja, "None")


tekst_zadatka="Write a function to find the longest common prefix string amongst an array of strings.\
If there is no common prefix, return an empty string ""."

pokusaj_resenja='''#include <bits/stdc++.h>
using namespace std;

string findPrefix(string x, string y)
{
    //base case checking
    if (x == "" || y == "")
        return "";

    string result = "";

    //if string x is smaller than y
    if (x.length() < y.length()) {
        //check up for common prefix part
        for (int i = 0; i < x.length(); i++) {
            if (x[i] == y[i])
                result += x[i];
        }
    }
    else {
        //if string y is smaller than x
        for (int i = 0; i < y.length(); i++) {
            //check up for common prefix part
            if (y[i] == x[i])
                result += y[i];
            else
                return result;
        }
    }
    return result;
}

string longestCommonPrefix(vector<string>& strs)
{
    //base cases
    if (strs.size() == 0)
        return "";
    //if only one string exists
    if (strs.size() == 1)
        return strs[0];
    string prefix = strs[0];
    //follow the associative property for checking
    //take two strings each time & pass output prefix
    //as one string for further processings
    for (int i = 1; i < strs.size(); i++) {
        prefix = findPrefix(prefix, strs[i]);
        if (prefix == "")
            return prefix;
    }
    return prefix;
}

int main()
{
    int n;
    cout << "enter no of strings you want to add\n";
    cin >> n;

    string s;
    vector<string> v;
    cout << "enter " << n << " strings\n";

    //collect input
    while (n--) {
        cin >> s;
        v.push_back(s);
    }
    //print longest common prefix
    if (longestCommonPrefix(v) == "")
        cout << "no common prefix between the strings\n";
    else
        cout << "longest common prefix: " << longestCommonPrefix(v) << endl;

    return 0;
}'''


grazie_assistant(cl_ip, tokn, tekst_zadatka, pokusaj_resenja, "None")