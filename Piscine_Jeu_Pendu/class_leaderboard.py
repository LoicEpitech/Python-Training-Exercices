import json
import os


class Leaderboard:
    def __init__(self, base_dir):
        self.file = os.path.join(base_dir, "leaderboard.json")

    def load(self):
        try:
            with open(self.file, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []

    def save(self, data):
        try:
            with open(self.file, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print("Erreur sauvegarde classement:", e)
