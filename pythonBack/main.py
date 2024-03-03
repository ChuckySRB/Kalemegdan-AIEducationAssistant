import os
import random
from assistant.api.client.gateway import AuthType, GrazieApiGatewayClient,GrazieHeaders
from assistant.api.client.chat.prompt import ChatPrompt
from assistant.api.client.endpoints import GrazieApiGatewayUrls
from assistant.api.client.profiles import Profile

token = "eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJHcmF6aWUgQXV0aGVudGljYXRpb24iLCJ1aWQiOiJhYmQ1MDQxOS0xMjQ2LTQzMWUtYjI0ZC01N2I3ZTMxNzUwNDEiLCJ0eXBlIjoiY3VzdG9tIiwibGljZW5zZSI6ImN1c3RvbV9hcHA6YjNmNjEwODgtYjcxYy00MGY2LWE4MmYtNDY2MjM1YWE0ZTYyIiwibGljZW5zZV90eXBlIjoiamV0YnJhaW5zLWFpLmFwcGxpY2F0aW9uLnN0YW5kYXJkIiwiZXhwIjoxNzEwNDQ2MTAwfQ.lz482uMjAKcTXyggXiL-4g2W-03w-5DwQ4dN7WkHPB3oKeb1QH9RzOG0fzoU1u_f2yFiT7PG-DYWVIEVtcSm9UvoIKFVJHJYeuWnTfndZSCvfaiKvfd4jrteMa0ZNh6mdigfObeOcVTUd5TRE1nXKDBMs5R6lvYJt5JnISNsSa3ze8jQlHOTXDRgbCKJfkSxUpjkrx7es1Zzeq-KlvrsyJZssjv9djrr06yVNgr0BFYVGJYZXTKbzuzj75oyNOuQyGpzev9j-NytR9dwFf-19QkYwVEEoAUaGpfSu_zKGWG-mA9iygDSowfVMqAZDQXDr7GGKTRxGIBKleMnAEkesQ"
# In a real application, you would have to supply the client's IP address
client_ip = "{}.{}.{}.{}".format(*[str(random.randint(0, 255)) for octet
in range(4)])

get_time = lambda f: os.stat(f).st_ctime

if not os.path.exists('code.txt'):
    with open('code.txt', 'w') as file:
        file.write('')
file = open('code.txt', 'r+')
new_content=file.read()
try:
    client = GrazieApiGatewayClient(
        url=GrazieApiGatewayUrls.STAGING,
        grazie_jwt_token=token,
        auth_type=AuthType.APPLICATION,
    )
    response = client.chat(
        chat=(
            ChatPrompt().add_system("You are a professional coding student assistant.").add_user(new_content)
        ),
        profile=Profile.OPENAI_GPT_4,
        headers={
            GrazieHeaders.ORIGINAL_USER_IP: client_ip,
        }
    )
    print(response.content)
except Exception as e:
    print(e)


