# logic_gates/risk_engine.py

class RiskEngine:
    def __init__(self, user_profile, interpretations):
        self.profile = user_profile
        self.db = interpretations
        self.base_resilience = user_profile['system_variables']['resilience_buffer']

    def evaluate_impact(self, star_status):
        """
        核心公式：风险等级判定逻辑
        根据触发的化忌或煞星组合计算冲击力 (Impact_Force)
        """
        impact_score = 0
        active_triggers = []

        # 遍历数据库，匹配当前用户触发的风险点
        for entry in self.db['data']:
            if entry['trigger'] in star_status:
                impact_score += 4.0  # 假设为高危触发
                active_triggers.append(entry)
        
        return impact_score, active_triggers

    def calculate_final_risk(self, impact_score):
        """
        最终风险评分映射：0 - 100
        公式：(Impact * 10) - (Resilience * 0.2)
        """
        raw_score = (impact_score * 10) - (self.base_resilience * 0.2)
        final_score = max(0, min(100, raw_score)) # 约束在0-100区间
        
        # 等级判定
        level = "L1_GREEN"
        if final_score > 80: level = "L4_RED"
        elif final_score > 50: level = "L3_ORANGE"
        elif final_score > 20: level = "L2_YELLOW"
        
        return {"score": final_score, "level": level}

    def generate_report(self, star_status):
        impact, triggers = self.evaluate_impact(star_status)
        risk = self.calculate_final_risk(impact)
        
        print(f"--- SYSTEM RISK AUDIT ---")
        print(f"STATUS: {risk['level']} | SCORE: {risk['score']}")
        for t in triggers:
            print(f"[!] {t['risk_type']}: {t['warning']}")
            print(f"建议指令: {t['commands']}")
