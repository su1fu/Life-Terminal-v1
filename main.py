import json
import os

def run_ziwu_audit():
    # 模拟生成的深度解析数据
    results = {
        "liunian_analysis": "<b>2026丙午年流年预警：</b><br>天机化忌入流年官禄宫。由于天机主逻辑，化忌主阻滞，对于开发者而言，这预示着底层架构可能遭遇非预期重构。建议：停止一切不必要的优化，优先保证系统稳定性。",
        "dayun_analysis": "<b>十年大运审计：</b><br>当前正值破局之运，命宫磁场剧烈震荡。你的事业重心正从单纯的技术实现向跨领域架构迁移。虽有波折，但这也是重塑生命底层的契机。",
        "palace_data": ["紫微", "七杀", "天机化忌", "武曲"] 
    }
    
    # 获取当前脚本所在目录
    base_path = os.path.dirname(os.path.abspath(__file__))
    # 强制指向 ui 文件夹
    ui_path = os.path.join(base_path, 'ui')
    
    if not os.path.exists(ui_path):
        os.makedirs(ui_path)
        
    target_file = os.path.join(ui_path, 'data.json')
    
    with open(target_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=4)
    
    print(f">> [SUCCESS] 数据已成功同步至: {target_file}")

if __name__ == "__main__":
    run_ziwu_audit()
