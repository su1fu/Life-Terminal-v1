# main.py - 系统总调度中心

import json
from core.ziwei_logic import ZiWeiCore
from logic_gates.risk_engine import RiskEngine

def load_data():
    """加载所有外部配置文件"""
    try:
        with open('profiles/alex_2026_test.json', 'r', encoding='utf-8') as f:
            profile = json.load(f)
        with open('database/interpretations_dev.json', 'r', encoding='utf-8') as f:
            db = json.load(f)
        return profile, db
    except FileNotFoundError as e:
        print(f"Error: 关键配置文件缺失 - {e}")
        return None, None

def run_system():
    print("--- LIFE_TERMINAL_V1: STARTING_BOOT_SEQUENCE ---")
    
    # 1. 加载数据
    profile, db = load_data()
    if not profile or not db: return

    # 2. 初始化排盘内核
    core = ZiWeiCore()
    # 根据 Alex 的生日计算命身宫
    pos = core.calculate_palace_positions(
        profile['birth_data']['lunar_month'], 
        profile['birth_data']['lunar_hour_index']
    )
    
    # 3. 模拟检测：假设当前 2026 流年触发了天机化忌 (TIAN_JI_HUA_JI)
    # 在真实版本中，这里会通过 logic_gates 自动计算出当前的化忌星曜
    current_star_status = ["TIAN_JI_HUA_JI"] 

    # 4. 运行风险审计引擎
    engine = RiskEngine(profile, db)
    engine.generate_report(current_star_status)

if __name__ == "__main__":
    run_system()
