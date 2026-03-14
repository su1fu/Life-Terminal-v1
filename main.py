import json
import os

def run_ziwu_audit():
    # 模拟数据
    results = {
        "liunian_analysis": "<b>2026丙午年专业审计：</b><br>当前触发[天机化忌]预警。底层架构可能面临非预期重构，建议保持代码简洁。",
        "dayun_analysis": "<b>大运趋势：</b><br>当前大运重心位于‘财帛-福德’线。今年是‘破局’之年，宜动不宜静。",
        "palace_data": ["紫微", "七杀", "天机化忌", "武曲"] 
    }
    
    # 因为 main.py 在根目录，直接找同级下的 ui 文件夹
    target_dir = 'ui'
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
        
    target_file = os.path.join(target_dir, 'data.json')
    
    with open(target_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=4)
    
    print(f">> [SUCCESS] 审计结果已写入 {target_file}")

if __name__ == "__main__":
    run_ziwu_audit()
