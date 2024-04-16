from sword import Swords
import pytest

class TestSwordsCreation:
    def test_create_sword_from_random_rarity(self):
        rarities = ["Basic", "White", "Green", "Blue", "Yellow", "Epic", "Legend"]
        for rarity in rarities:
            sword = Swords.create_from_rarity("Test Sword", rarity)
            assert sword.rarity == rarity, f"Expected rarity {rarity}, but got {sword.rarity}"
