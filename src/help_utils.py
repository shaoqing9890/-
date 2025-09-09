"""
帮助工具模块 (Help Utilities Module)

这个模块提供了一些有用的工具函数。
This module provides some useful utility functions.
"""

import sys
import os
from datetime import datetime

class HelpUtils:
    """
    帮助工具类 (Help Utilities Class)
    """
    
    @staticmethod
    def get_system_info():
        """
        获取系统信息 (Get system information)
        
        Returns:
            dict: 包含系统信息的字典 (Dictionary containing system information)
        """
        return {
            "platform": sys.platform,
            "python_version": sys.version,
            "current_time": datetime.now().isoformat(),
            "current_directory": os.getcwd()
        }
    
    @staticmethod
    def format_message(message, style="info"):
        """
        格式化消息 (Format message)
        
        Args:
            message (str): 要格式化的消息 (Message to format)
            style (str): 样式类型 (Style type)
            
        Returns:
            str: 格式化后的消息 (Formatted message)
        """
        styles = {
            "info": f"ℹ️  {message}",
            "success": f"✅ {message}",
            "warning": f"⚠️  {message}",
            "error": f"❌ {message}",
            "help": f"🆘 {message}"
        }
        return styles.get(style, message)
    
    @staticmethod
    def create_help_text(title, description, examples=None):
        """
        创建帮助文本 (Create help text)
        
        Args:
            title (str): 标题 (Title)
            description (str): 描述 (Description)
            examples (list): 示例列表 (List of examples)
            
        Returns:
            str: 格式化的帮助文本 (Formatted help text)
        """
        help_text = f"""
{title}
{'=' * len(title)}

{description}

"""
        if examples:
            help_text += "示例 (Examples):\n"
            help_text += "=" * 15 + "\n"
            for i, example in enumerate(examples, 1):
                help_text += f"{i}. {example}\n"
        
        return help_text

def main():
    """
    主函数，演示工具的使用 (Main function demonstrating tool usage)
    """
    utils = HelpUtils()
    
    # 显示系统信息 (Display system information)
    print(utils.format_message("显示系统信息 (Displaying system information)", "info"))
    sys_info = utils.get_system_info()
    for key, value in sys_info.items():
        print(f"{key}: {value}")
    
    print("\n" + "=" * 50 + "\n")
    
    # 演示消息格式化 (Demonstrate message formatting)
    messages = [
        ("这是一条信息", "info"),
        ("操作成功！", "success"),
        ("这是一个警告", "warning"),
        ("发生错误！", "error"),
        ("需要帮助", "help")
    ]
    
    for msg, style in messages:
        print(utils.format_message(msg, style))
    
    print("\n" + "=" * 50 + "\n")
    
    # 创建帮助文本 (Create help text)
    help_text = utils.create_help_text(
        "帮助工具使用指南",
        "这个工具提供了各种有用的功能来帮助开发者。",
        [
            "utils.get_system_info() - 获取系统信息",
            "utils.format_message('消息', '样式') - 格式化消息",
            "utils.create_help_text('标题', '描述', ['示例']) - 创建帮助文本"
        ]
    )
    print(help_text)

if __name__ == "__main__":
    main()