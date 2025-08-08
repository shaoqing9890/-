/**
 * 帮助示例 (Help Example)
 * 
 * 这是一个简单的 JavaScript 示例，展示如何创建有用的函数。
 * This is a simple JavaScript example showing how to create useful functions.
 */

// 问候函数 (Greeting function)
function helloWorld() {
    console.log("你好，世界！(Hello, World!)");
    console.log("欢迎使用帮助项目！(Welcome to the Help Project!)");
}

// 帮助信息函数 (Help information function)
function helpMessage() {
    const helpText = `
    帮助项目示例 (Help Project Example)
    
    这个脚本演示了基本的 JavaScript 功能：
    This script demonstrates basic JavaScript functionality:
    
    - 函数定义 (Function definition)
    - 控制台输出 (Console output)
    - 模板字符串 (Template strings)
    - 模块导出 (Module exports)
    
    使用方法 (Usage):
    node examples/hello.js
    `;
    console.log(helpText);
}

// 用户交互函数 (User interaction function)
function greetUser(name = "朋友 (Friend)") {
    console.log(`你好，${name}！很高兴认识你！`);
    console.log(`Hello, ${name}! Nice to meet you!`);
}

// 主函数 (Main function)
function main() {
    console.log("=".repeat(50));
    helloWorld();
    console.log("=".repeat(50));
    helpMessage();
    console.log("=".repeat(50));
    greetUser("开发者 (Developer)");
    console.log("=".repeat(50));
}

// 如果直接运行此文件 (If running this file directly)
if (require.main === module) {
    main();
}

// 导出函数以供其他模块使用 (Export functions for use by other modules)
module.exports = {
    helloWorld,
    helpMessage,
    greetUser,
    main
};