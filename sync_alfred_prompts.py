#!/usr/bin/env python3
"""
同步 Alfred AI Prompt snippets 到 Markdown 文件
"""

import json
import os
from pathlib import Path

# 配置
ALFRED_SNIPPETS_BASE = Path.home() / "workspace/vault/alfred/Alfred.alfredpreferences/snippets"
OUTPUT_DIR = Path(__file__).parent

# 源文件夹 -> 输出文件名 映射
FOLDER_MAPPING = {
    "ai_prompt1_brain": "Alfred_Brain.md",
    "ai_prompt2_readwrite": "Alfred_ReadWrite.md",
    "ai_prompt3_code": "Alfred_Code.md",
    "ai_prompt4_tool": "Alfred_Tool.md",
    "ai_prompt5_inbox": "Alfred_Inbox.md",
}

# Markdown 标题映射
TITLE_MAPPING = {
    "ai_prompt1_brain": "Alfred AI Prompt - Brain",
    "ai_prompt2_readwrite": "Alfred AI Prompt - ReadWrite",
    "ai_prompt3_code": "Alfred AI Prompt - Code",
    "ai_prompt4_tool": "Alfred AI Prompt - Tool",
    "ai_prompt5_inbox": "Alfred AI Prompt - Inbox",
}


def parse_snippet_file(file_path: Path) -> dict | None:
    """解析单个 Alfred snippet JSON 文件"""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        snippet_data = data.get("alfredsnippet", {})
        return {
            "name": snippet_data.get("name", ""),
            "snippet": snippet_data.get("snippet", ""),
        }
    except (json.JSONDecodeError, KeyError) as e:
        print(f"⚠️  解析失败: {file_path.name} - {e}")
        return None


def get_snippets_from_folder(folder_name: str) -> list[dict]:
    """从指定文件夹读取所有 snippets"""
    folder_path = ALFRED_SNIPPETS_BASE / folder_name
    if not folder_path.exists():
        print(f"❌ 文件夹不存在: {folder_path}")
        return []

    snippets = []
    for file_path in folder_path.glob("*.json"):
        # 跳过 info.plist 等非 snippet 文件
        if file_path.name == "info.plist":
            continue
        snippet = parse_snippet_file(file_path)
        if snippet and snippet["name"]:
            snippets.append(snippet)

    # 按 name 排序
    snippets.sort(key=lambda x: x["name"])
    return snippets


def generate_markdown(title: str, snippets: list[dict]) -> str:
    """生成 Markdown 内容"""
    lines = [
        "<!-- ⚠️ 此文件由 sync_alfred_prompts.py 自动生成，请勿手动编辑 -->",
        "<!-- 修改请编辑 Alfred snippets，然后运行脚本重新生成 -->",
        "",
        f"# {title}",
        "",
    ]

    for snippet in snippets:
        lines.append(f"### {snippet['name']}")
        lines.append("")
        lines.append(snippet["snippet"])
        lines.append("")

    return "\n".join(lines)


def sync_folder(folder_name: str):
    """同步单个文件夹到 Markdown"""
    output_file = OUTPUT_DIR / FOLDER_MAPPING[folder_name]
    title = TITLE_MAPPING[folder_name]

    snippets = get_snippets_from_folder(folder_name)
    if not snippets:
        print(f"⚠️  {folder_name}: 没有找到 snippets")
        return

    markdown_content = generate_markdown(title, snippets)

    # 写入文件
    output_file.parent.mkdir(parents=True, exist_ok=True)
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(markdown_content)

    print(f"✅ {folder_name} -> {output_file.name} ({len(snippets)} snippets)")


def main():
    print("🔄 开始同步 Alfred AI Prompts...\n")

    for folder_name in FOLDER_MAPPING:
        sync_folder(folder_name)

    print("\n🎉 同步完成!")


if __name__ == "__main__":
    main()
