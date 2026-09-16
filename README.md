# Agent项目
Agent项目-扫地机器人

安装依赖：`uv sync`。IDE 的 Python 解释器请选择项目下的 `.venv/bin/python`。

配置环境变量 `DASHSCOPE_API_KEY`，在项目根目录运行向量库模块：

```bash
uv run python -m rag.vector_store
```

运行前请在 `config/rag.yml` 中配置可用的模型名称，并按 `config/chroma.yml` 的
`data_path` 配置准备知识库文件。运行模块会调用嵌入模型并写入本地向量库。
