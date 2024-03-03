from grazie.api.client.gateway import AuthType, GrazieApiGatewayClient, GrazieHeaders
from grazie.api.client.chat.prompt import ChatPrompt
from grazie.api.client.endpoints import GrazieApiGatewayUrls
from grazie.api.client.profiles import Profile

token = "eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJHcmF6aWUgQXV0aGVudGljYXRpb24iLCJ1aWQiOiJhYmQ1MDQxOS0xMjQ2LTQzMWUtYjI0ZC01N2I3ZTMxNzUwNDEiLCJ0eXBlIjoiY3VzdG9tIiwibGljZW5zZSI6ImN1c3RvbV9hcHA6YjNmNjEwODgtYjcxYy00MGY2LWE4MmYtNDY2MjM1YWE0ZTYyIiwibGljZW5zZV90eXBlIjoiamV0YnJhaW5zLWFpLmFwcGxpY2F0aW9uLnN0YW5kYXJkIiwiZXhwIjoxNzEwNDQ2MTAwfQ.lz482uMjAKcTXyggXiL-4g2W-03w-5DwQ4dN7WkHPB3oKeb1QH9RzOG0fzoU1u_f2yFiT7PG-DYWVIEVtcSm9UvoIKFVJHJYeuWnTfndZSCvfaiKvfd4jrteMa0ZNh6mdigfObeOcVTUd5TRE1nXKDBMs5R6lvYJt5JnISNsSa3ze8jQlHOTXDRgbCKJfkSxUpjkrx7es1Zzeq-KlvrsyJZssjv9djrr06yVNgr0BFYVGJYZXTKbzuzj75oyNOuQyGpzev9j-NytR9dwFf-19QkYwVEEoAUaGpfSu_zKGWG-mA9iygDSowfVMqAZDQXDr7GGKTRxGIBKleMnAEkesQ"
client_ip = "192.168.0.19"


def grazie_assistant_request(assistant, task_text, task_past_attempts, task_attempt):
    whole_prompt = "Your setting: " + assistant.setting \
                   + "Your Name: " + assistant.name \
                    + "Required Task: " + task_text \
                   + "Format of your answer should be: " + assistant.format + assistant.format_explanation\
                   + "Your Context of previous entries:" + task_past_attempts \
                   + "Your Content: " + task_attempt    \


    client = GrazieApiGatewayClient(
        url=GrazieApiGatewayUrls.STAGING,
        grazie_jwt_token=token,
        auth_type=AuthType.APPLICATION,
    )
    response = client.chat(
        chat=(
            ChatPrompt().add_system(assistant.system).add_user(whole_prompt)
        ),
        profile=Profile.OPENAI_GPT_4,
        headers={
            GrazieHeaders.ORIGINAL_USER_IP: client_ip,
        }
    )
    print("HELPFUL ASSISTANT---------------------------------------------------------------------")
    print(response.content)
