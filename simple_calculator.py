# 简易计算器 - 适合公开的演示代码
# 用于 Git 版本管理实践提交

def add(a, b):
    """加法"""
    return a + b

def sub(a, b):
    """减法"""
    return a - b

def mul(a, b):
    """乘法"""
    return a * b

def div(a, b):
    """除法"""
    if b == 0:
        return "错误：除数不能为0"
    return a / b

if __name__ == "__main__":
    print("=== 简易计算器 ===")
    print("1 + 2 =", add(1, 2))
    print("5 - 3 =", sub(5, 3))
    print("4 × 6 =", mul(4, 6))
    print("8 ÷ 2 =", div(8, 2))
    print("9 ÷ 0 =", div(9, 0))