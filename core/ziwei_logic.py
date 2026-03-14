# core/ziwei_logic.py

class ZiWeiCore:
    def __init__(self):
        self.branches = ["寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥", "子", "丑"]

    def calculate_palace_positions(self, month, hour_index):
        """
        根据农历月份和时辰索引计算命身宫坐标
        hour_index: 0=寅, 1=卯... 10=子, 11=丑
        """
        # 命宫：寅起正月，顺数月，逆数时
        life_idx = (month - 1 - hour_index) % 12
        # 身宫：寅起正月，顺数月，顺数时
        body_idx = (month - 1 + hour_index) % 12
        
        return {
            "life_palace": {"index": life_idx, "label": self.branches[life_idx]},
            "body_palace": {"index": body_idx, "label": self.branches[body_idx]}
        }

    def get_twelve_palaces(self, life_idx):
        """
        从命宫开始，逆布十二宫名
        """
        palace_names = ["命宫", "兄弟", "夫妻", "子女", "财帛", "疾厄", 
                        "迁移", "奴仆", "官禄", "田宅", "福德", "父母"]
        layout = {}
        for i in range(12):
            current_idx = (life_idx - i) % 12
            layout[self.branches[current_idx]] = palace_names[i]
        return layout
