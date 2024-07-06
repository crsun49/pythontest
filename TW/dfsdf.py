import tweepy
consumer_key = 'bidDjvDw7m4kM3PtW2FEp8a6L'
consumer_secret = 'FsgUqkV79AvQAKUsyyQlxVYqIHzyrC1itMAbnnunsiD9vRPJSR'
access_token = '1492064576384700421-ZfQcIeCMxwWgzH3V8C3OhLHsPLmH9W'
access_token_secret = 'vZiDUIZIoLdJCNSBvp5OZiToBALnz0DcLg0427pbIush8'
# 使用您的 API 密钥进行身份验证
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# 创建 Twitter API 对象
api = tweepy.API(auth)

# 获取用户 ID
user_id = 'paul9886'  # 替换为要抓取其帖子的用户的 ID

# 获取用户最近 10 条推文
tweets = api.user_timeline(user_id=user_id, count=10)

# 打印推文
for tweet in tweets:
    print(tweet.text)