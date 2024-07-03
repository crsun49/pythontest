
import tweepy
# 替换为你的API密钥和访问令牌
api_key = 'bidDjvDw7m4kM3PtW2FEp8a6L'
api_secret_key = 'FsgUqkV79AvQAKUsyyQlxVYqIHzyrC1itMAbnnunsiD9vRPJSR'
access_token = '1492064576384700421-ZfQcIeCMxwWgzH3V8C3OhLHsPLmH9W'
access_token_secret = 'vZiDUIZIoLdJCNSBvp5OZiToBALnz0DcLg0427pbIush8'

proxies = {
    'http': '127.0.0.1:33210',
    'https': '127.0.0.1:33210'
}
# 使用tweepy进行身份验证
auth = tweepy.OAuth1UserHandler(api_key, api_secret_key, access_token, access_token_secret)

api = tweepy.API(auth, proxy=proxies)


# 发送 API 请求
user = api.me()

# 输出用户信息，如果能成功输出用户信息，则验证成功
print(user.screen_name)
# 指定要抓取的Twitter用户名
username = 'paul9886'

public_tweets=api.home_timeline()
# 获取用户的帖子
tweets = api.user_timeline(screen_name=username, count=10, tweet_mode='extended')

# 打印每条帖子的内容
for tweet in tweets:
    print(f"{tweet.user.screen_name} said: {tweet.full_text}\n")

# 注意：count参数指定要获取的帖子数量，最大为200
