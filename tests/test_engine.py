"""对比测试"""
import pytest, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from src.engine import EquipCompareSystem, Equipment

class TestCompare:
    def test_supports_4_items(self):
        ecs = EquipCompareSystem()
        ecs.equipment = {f"e{i}": Equipment(f"e{i}",f"n{i}","weapon","rare",10,{"atk":100},{},"") for i in range(4)}
        result = ecs.compare(["e0","e1","e2","e3"])
        assert result is not None and len(result) == 4, "不支持4件对比"

class TestScore:
    def test_score_includes_sub(self):
        ecs = EquipCompareSystem()
        ecs.equipment = {"e1": Equipment("e1","n","weapon","rare",10,{"atk":100},{"crit":50},"")}
        assert ecs.get_score("e1") > 100, "副属性不计分"
