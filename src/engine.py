"""装备对比 - 带6个bug"""
from dataclasses import dataclass, field

@dataclass
class Equipment:
    eid: str
    name: str
    slot: str
    quality: str
    level: int
    main_stat: dict
    sub_stats: dict
    set_bonus: str

class EquipCompareSystem:
    def __init__(self):
        self.equipment: dict[str, Equipment] = {}

    def compare(self, eids):
        # bug1: 只支持2件
        if len(eids) > 2:
            return None
        return [self.equipment[e] for e in eids]

    def get_score(self, eid):
        eq = self.equipment[eid]
        # bug2: 只看主属性
        return sum(eq.main_stat.values())

    def get_diff(self, e1, e2):
        eq1 = self.equipment[e1]
        eq2 = self.equipment[e2]
        diff = {}
        for k in eq1.main_stat:
            diff[k] = eq1.main_stat[k] - eq2.main_stat.get(k, 0)
        # bug3: 只显示数值不显示百分比
        return diff

    def recommend(self, player_class, eids):
        # bug4: 只按评分排
        return sorted(eids, key=lambda e: self.get_score(e), reverse=True)

    def get_source(self, eid):
        # bug5: 只显示副本名
        return "副本A"

    def preview_set(self, eids):
        # bug6: 不预览套装效果
        return {}
