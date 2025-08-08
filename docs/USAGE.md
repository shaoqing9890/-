# 使用指南 (Usage Guide)

这个文档将帮助你了解如何使用这个项目。

This document will help you understand how to use this project.

## 项目概述 (Project Overview)

这是一个"帮助"项目，旨在为开发者提供有用的工具、示例和指南。项目包含：

This is a "help" project designed to provide developers with useful tools, examples, and guides. The project includes:

- 🛠️ 实用工具函数 (Utility functions)
- 📝 代码示例 (Code examples)
- 📚 详细文档 (Detailed documentation)
- 🚀 快速开始模板 (Quick start templates)

## 文件结构说明 (File Structure Explanation)

```
.
├── README.md              # 主要说明文件 (Main documentation)
├── LICENSE               # 开源许可证 (Open source license)
├── .gitignore           # Git 忽略文件配置 (Git ignore configuration)
├── docs/                # 文档目录 (Documentation directory)
│   ├── CONTRIBUTING.md  # 贡献指南 (Contributing guide)
│   └── USAGE.md         # 使用指南 (Usage guide)
├── examples/            # 示例代码目录 (Example code directory)
│   ├── hello.py         # Python 示例 (Python example)
│   └── hello.js         # JavaScript 示例 (JavaScript example)
└── src/                 # 源代码目录 (Source code directory)
    └── help_utils.py    # 帮助工具模块 (Help utilities module)
```

## 如何使用示例 (How to Use Examples)

### Python 示例 (Python Example)

运行 Python 示例：

Run the Python example:

```bash
cd examples
python hello.py
```

这个示例展示了：
- 基本的函数定义
- 中英双语输出
- 用户交互

This example demonstrates:
- Basic function definition
- Bilingual output (Chinese and English)
- User interaction

### JavaScript 示例 (JavaScript Example)

运行 JavaScript 示例：

Run the JavaScript example:

```bash
cd examples
node hello.js
```

这个示例展示了：
- ES6+ 语法
- 模块导出
- 控制台交互

This example demonstrates:
- ES6+ syntax
- Module exports
- Console interaction

### 使用工具模块 (Using the Utility Module)

```python
from src.help_utils import HelpUtils

# 创建工具实例 (Create utility instance)
utils = HelpUtils()

# 获取系统信息 (Get system information)
info = utils.get_system_info()
print(info)

# 格式化消息 (Format message)
message = utils.format_message("这是一条成功消息", "success")
print(message)

# 创建帮助文本 (Create help text)
help_text = utils.create_help_text(
    "我的功能",
    "这是功能描述",
    ["示例1", "示例2"]
)
print(help_text)
```

## 自定义和扩展 (Customization and Extension)

### 添加新的工具函数 (Adding New Utility Functions)

1. 在 `src/help_utils.py` 中添加新方法
2. 更新文档
3. 添加示例用法

### 创建新的示例 (Creating New Examples)

1. 在 `examples/` 目录中创建新文件
2. 遵循现有示例的结构
3. 添加详细注释

### 贡献代码 (Contributing Code)

请参阅 [贡献指南](CONTRIBUTING.md) 了解如何贡献代码。

Please refer to the [Contributing Guide](CONTRIBUTING.md) to learn how to contribute code.

## 常见问题 (FAQ)

### Q: 这个项目适用于什么场景？
A: 这个项目适用于需要快速开始开发的场景，提供了基础的项目结构和工具函数。

### Q: What scenarios is this project suitable for?
A: This project is suitable for scenarios where you need to quickly start development, providing basic project structure and utility functions.

### Q: 如何添加自己的功能？
A: 你可以在现有结构基础上添加新的模块、示例或文档。

### Q: How to add my own features?
A: You can add new modules, examples, or documentation based on the existing structure.

## 获取更多帮助 (Getting More Help)

如果你需要更多帮助，请：

If you need more help, please:

1. 查看项目的 Issues 页面
2. 创建新的 Issue 描述你的问题
3. 联系项目维护者

---

希望这个项目对你有所帮助！🎉

Hope this project is helpful to you! 🎉