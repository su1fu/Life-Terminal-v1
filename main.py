import json
import os

def run_advanced_audit():
    # 模拟高级紫微+八字算法产出的数据
    results = {
        "user_info": {
            "bazi": "丙午 庚寅 辛亥 戊子", 
            "element": "钗钏金"
        },
        "liunian_analysis": "<b>2026 丙午流年审计：</b><br>当前触发[天机化忌]预警。命主官禄磁场波动，建议在代码架构上保持‘防御性编程’，切勿盲目重构核心逻辑。",
        "dayun_analysis": "<b>十年大运核算：</b><br>当前大运正处于‘破军’变局。技术栈虽有更迭风险，但也是重塑底层逻辑的最佳契机。",
        "palace_data": [
            {"name": "命宫", "stars": ["紫微", "七杀"], "location": "辰"},
            {"name": "官禄", "stars": ["天机", "化忌"], "location": "申"},
            {"name": "财帛", "stars": ["武曲", "天府"], "location": "子"}
        ]
    }
    
    # 强制写入 ui 文件夹，确保与 index.html 同级
    ui_dir = os.path.join(os.getcwd(), 'ui')
    os.makedirs(ui_dir, exist_ok=True)
    
    with open(os.path.join(ui_dir, 'data.json'), 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=4)
        
    print(f">> [SUCCESS] 审计数据已同步至：{os.path.join(ui_dir, 'data.json')}")

if __name__ == "__main__":
    run_advanced_audit()
