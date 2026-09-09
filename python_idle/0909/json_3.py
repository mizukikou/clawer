import json
config = {"url": "http://example.com","retry": 3}

with open("config.json", "w", encoding="utf-8") as f:
    json.dump(config, f, indent=4, ensure_ascii=False)

with open("config.json", "r", encoding="utf-8") as f:
    loaded_config = json.load(f)
    print(loaded_config)