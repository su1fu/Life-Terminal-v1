# 伪代码示例：main.py 核心缝合逻辑
import json

def generate_web_data(profile_data, analysis_result):
    web_output = {
        "user_name": profile_data['name'],
        "birth_date": f"{profile_data['year']}-{profile_data['month']}-{profile_data['day']}",
        "life_palace": "申宫",  # 这里由你的紫微算法算出
        "stars": ["紫微", "七杀", "天机化忌"],
        "dayun_analysis": "当前大运正值转折点...",
        "liunian_analysis": "2026丙午年，天机化忌冲击官禄..."
    }
    with open('ui/data.json', 'w', encoding='utf-8') as f:
        json.dump(web_output, f, ensure_ascii=False, indent=4)

print(">> 已更新 UI 数据库：data.json")
