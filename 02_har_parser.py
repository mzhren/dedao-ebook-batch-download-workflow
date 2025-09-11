import json
import re

def extract_id_out_from_file(file_path):
    """从文本文件中提取所有id_out值"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 使用正则表达式提取所有的id_out值
    # 匹配格式：\"id_out\":\"值\"
    pattern = r'\\"id_out\\":\\"([^\\"]+)\\"'
    id_out_values = re.findall(pattern, content)
    
    return id_out_values

def save_to_json(id_out_values, output_file_path):
    """将id_out值保存到JSON文件"""
    with open(output_file_path, 'w', encoding='utf-8') as f:
        json.dump(id_out_values, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="从HAR文件中提取id_out并保存为JSON")
    parser.add_argument("-i", "--input", required=True, help="输入文件路径")
    parser.add_argument("-o", "--output", required=True, help="输出JSON文件路径")
    args = parser.parse_args()

    input_file_path = args.input
    output_file_path = args.output

    id_out_values = extract_id_out_from_file(input_file_path)

    if not id_out_values:
        print("未找到任何id_out值。请检查文件格式。")
    else:
        save_to_json(id_out_values, output_file_path)
        print(f"已提取 {len(id_out_values)} 个id_out值，并保存到 {output_file_path}")
