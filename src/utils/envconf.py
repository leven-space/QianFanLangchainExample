from configparser import ConfigParser
import os

def read_env_file(env_path):
    parser = ConfigParser()
    parser.read(env_path)
    return parser['DEFAULT']

if __name__ == "__main__":
    env_path = ".env" # 替换为你的.env文件路径
    env = read_env_file(env_path)
    print(os.getenv('QIANFAN_AK', env.get('QIANFAN_AK')))
    print(os.getenv('QIANFAN_SK', env.get('QIANFAN_SK')))