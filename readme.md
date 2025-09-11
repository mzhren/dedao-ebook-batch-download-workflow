# 得到电子书批量下载工作流

本项项目是基于[yann0917/dedao-dl: 得到 APP 课程下载工具，可在终端查看文章内容，可生成 PDF，音频文件，markdown 文稿，可下载电子书。](https://github.com/yann0917/dedao-dl)的脚本。通过dedao-dl工具获取得到电子书的 ID，然后通过该脚本生成下载命令。

`dedao-dl-utils` 是一组用于管理和下载电子书的实用工具。包括以下步骤和脚本：

## 1 访问 [得到官网](https://www.dedao.cn/) 获取电子书列表请求（HAR）

## 2 将 HAR 文件转换为 JSON 文件

02_har_to_json.py 脚本用于将 HAR 文件转换为 JSON 文件。使用方法如下：

```bash
python 02_har_to_json.py input.har output.json
```

其中：
- `input.har`：输入的 HAR 文件路径
- `output.json`：输出的 JSON 文件路径

## 3 通过 Automa 浏览器插件将电子书添加到个人书架

## 4 通过 Dedao-dl 工具获取电子书列表

```bash
dedao-dl ebook > ebook_list.txt
```

## 5 从电子书列表中提取电子书真实 ID

05_extract_ebook_ids.py 脚本用于从电子书列表中提取电子书的真实 ID。使用方法如下：

```bash
python 05_extract_ebook_ids.py -in ebook_list.txt -o ebook_ids.json
```

其中：
- `-in ebook_list.txt`：输入文件，包含电子书列表的文本文件
- `-o ebook_ids.json`：输出文件，包含提取的电子书 ID

## 6 通过脚本生成下载命令

06_batch_generate_download_commands.py 脚本用于生成下载命令。使用方法如下：

```bash
python 06_batch_generate_download_commands.py -i ebook_ids.json -o download_commands.txt -t 4 -e existing_books.json
```

其中：
- `-i ebook_ids.json`：输入文件，包含电子书 ID 的 JSON 文件
- `-o download_commands.txt`：输出文件，包含生成的下载命令
- `-t 4`：type 参数，1 表示下载 html，2 表示下载 pdf，3 表示下载 epub，4 表示同时下载 pdf 和 epub
- `-e existing_books.json`：可选参数，包含已存在电子书 ID的 JSON 文件，避免重复下载（就是上次下载过的电子书）




