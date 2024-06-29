import json
import uuid

json_file_path = 'csv.json'

# 파일 열기
with open(json_file_path, 'r') as json_file:
    data = json.load(json_file)

# 각 항목에 UUID 부여
for item in data:
    item["id"] = str(uuid.uuid4())

# 수정된 데이터를 새로운 JSON 파일에 저장
with open("data.json", "w") as new_json_file:
    json.dump(data, new_json_file, indent=2)
