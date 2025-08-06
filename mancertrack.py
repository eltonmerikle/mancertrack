import requests
import time
import json
from datetime import datetime
import random

class CryptomancerWatcher:
    def __init__(self, pattern_db_path="cryptomancer/pattern_db.json"):
        self.pattern_db_path = pattern_db_path
        self.historical_patterns = self.load_patterns()

    def load_patterns(self):
        try:
            with open(self.pattern_db_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def fetch_wallet_activity(self):
        # Заглушка: вместо настоящего API — фейковые данные
        # В продакшене здесь можно использовать Glassnode, Arkham API или Etherscan
        return [{
            "wallet": f"0x{random.randint(10**15, 10**16):x}",
            "tx_count": random.randint(3, 25),
            "volume": round(random.uniform(10000, 1000000), 2),
            "timestamp": datetime.utcnow().isoformat()
        } for _ in range(5)]

    def detect_suspicious_activity(self, activity):
        alerts = []
        for tx in activity:
            if tx["volume"] > 500000 and tx["tx_count"] > 10:
                if self.is_pattern_similar(tx):
                    alerts.append(tx)
        return alerts

    def is_pattern_similar(self, tx):
        for pattern in self.historical_patterns:
            if abs(pattern["volume"] - tx["volume"]) < 100000 and abs(pattern["tx_count"] - tx["tx_count"]) < 5:
                return True
        return False

    def run(self, interval=30):
        print("🧙 Cryptomancer is watching the chains...")
        while True:
            activity = self.fetch_wallet_activity()
            suspicious = self.detect_suspicious_activity(activity)
            if suspicious:
                for s in suspicious:
                    print(f"🚨 Suspicious activity detected from {s['wallet']} | Volume: ${s['volume']:,}")
            else:
                print("✨ No suspicious activity. All is quiet.")
            time.sleep(interval)
