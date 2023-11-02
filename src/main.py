import os
import qianfan
from utils import envconf
from langchain.chat_models import QianfanChatEndpoint
from langchain.prompts import ChatPromptTemplate

env=envconf.read_env_file(".env")

os.environ['QIANFAN_AK']=env.get('QIANFAN_AK')
os.environ['QIANFAN_SK']=env.get('QIANFAN_SK')



if __name__ == "__main__":
   qianfan_chat=QianfanChatEndpoint(model="ERNIE-Bot-4")
   template_temp="""写一首诗歌，参考李白,其中主题为{head}"""
   head="除夕不放假"
   temp=ChatPromptTemplate.from_template(template=template_temp)
   customer_msg=temp.format_messages(head=head)
   print(customer_msg)
   response=qianfan_chat(customer_msg)
   print(response)