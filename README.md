# Vínkulo API

一个使用FastAPI构建的简单认证API系统。

## 功能特点

- 用户注册
- 用户登录与JWT令牌生成
- 受保护的端点（需要JWT令牌验证）
- 内存数据存储（模拟数据库）

## 技术栈

- [FastAPI](https://fastapi.tiangolo.com/) - 高性能的现代Python Web框架
- [Pydantic](https://pydantic-docs.helpmanual.io/) - 数据验证和设置管理
- [PyJWT](https://pyjwt.readthedocs.io/) - JWT令牌管理
- [Passlib](https://passlib.readthedocs.io/) - 密码哈希处理

## 安装

1. 克隆此仓库
   ```bash
   git clone <repository-url>
   cd V-nkulo
   ```

2. 创建虚拟环境并激活
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/MacOS
   source venv/bin/activate
   ```

3. 安装依赖
   ```bash
   pip install -r requirements.txt
   ```

## 运行应用

```bash
uvicorn main:app --reload
```

服务器将在 http://localhost:8000 上启动。

## API端点

- **GET /** - 根路由，返回欢迎消息
- **POST /auth/register** - 注册新用户
- **POST /auth/login** - 用户登录，获取JWT令牌
- **GET /auth/users/me** - 获取当前用户信息（需要JWT认证）

## API文档

启动应用后，可以通过以下URL访问自动生成的API文档：
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 安全注意事项

**注意:** 此项目是一个演示应用，不应在生产环境中直接使用。在生产环境中，您应该：

1. 将SECRET_KEY存储在环境变量中，而不是硬编码
2. 使用真实数据库而不是内存存储
3. 实现更强大的错误处理
4. 添加日志记录和监控
5. 考虑使用HTTPS 