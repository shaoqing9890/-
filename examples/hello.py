#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
帮助示例 (Help Example)

这是一个简单的 Python 示例，展示如何创建一个有用的脚本。
This is a simple Python example showing how to create a useful script.
"""

def hello_world():
    """
    打印问候语的函数
    Function to print greetings
    """
    print("你好，世界！(Hello, World!)")
    print("欢迎使用帮助项目！(Welcome to the Help Project!)")

def help_message():
    """
    显示帮助信息
    Display help information
    """
    help_text = """
    帮助项目示例 (Help Project Example)
    
    这个脚本演示了基本的 Python 功能：
    This script demonstrates basic Python functionality:
    
    - 函数定义 (Function definition)
    - 字符串处理 (String handling)
    - 用户交互 (User interaction)
    
    使用方法 (Usage):
    python examples/hello.py
    """
    print(help_text)

def main():
    """
    主函数
    Main function
    """
    print("=" * 50)
    hello_world()
    print("=" * 50)
    help_message()
    print("=" * 50)
    
    # 用户交互示例 (User interaction example)
    user_input = input("请输入你的名字 (Please enter your name): ")
    print(f"你好，{user_input}！很高兴认识你！")
    print(f"Hello, {user_input}! Nice to meet you!")

if __name__ == "__main__":
    main()