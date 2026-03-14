import json
import os

def run_ziwu_audit():
    # 这里是你的专业解析数据库，后期你可以根据算法动态生成这些文字
    results = {
        "liunian_analysis": "<b>2026丙午年专业审计：</b><br>当前触发[天机化忌]预警。天机主变动与逻辑，化忌则主失算。在程序开发层面，这意味着底层架构可能面临非预期重构。建议：保持代码简洁，严禁过度设计。",
        "dayun_analysis": "<b>大运趋势：</b><br>当前大运重心位于‘财帛-福德’线。磁场显示你的技术积累已达临界点，今年是‘破局’之年，宜动不宜静。",
        "palace_data": ["紫微", "七杀", "天机化忌", "武曲"] 
    }
    
    # 核心步骤：确保 ui 文件夹存在，否则 Actions 会报错
    if not os.path.exists('ui'):
        os.makedirs('ui')
        
    # 将结果写入 ui/data.json
    # 这样网页 index.html 就能通过 fetch('data.json') 拿到它
    with open('ui/data.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=4)
    
    print(">> [SUCCESS] 审计结果已同步至 UI 数据库。")

if __name__ == "__main__":
    run_ziwu_audit()
