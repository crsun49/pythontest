import random

#生成随机数
def generate_random(num):
    """
    生成一个随机整数，范围是1到3（包括1和3）。
    """
    return random.randint(1, num)
#生成指定区间的随机数需要支持精确到几位小数的
def generate_random_number(min_value, max_value, decimal_places):
    # 生成一个在 min_value 和 max_value 之间的随机浮点数
    random_number = random.uniform(min_value, max_value)
    # 使用 round() 函数来控制小数位数
    rounded_number = round(random_number, decimal_places)
    return rounded_number