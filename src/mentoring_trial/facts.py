"""试点报名、实际指导和随访结果的读取。"""

import json
from pathlib import Path


def load_records(path):
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(payload, list):
        raise ValueError("记录文件必须包含数组")
    records = []
    seen = set()
    for position, record in enumerate(payload):
        required = ("id", "student_id", "event", "date")
        if not isinstance(record, dict) or any(not record.get(field) for field in required):
            raise ValueError(f"第 {position + 1} 条试点记录缺少必填字段")
        if record["id"] in seen:
            raise ValueError(f"重复记录标识：{record['id']}")
        seen.add(record["id"])
        if record["event"] not in {"offered", "session", "transfer", "pause", "outcome"}:
            raise ValueError(f"记录 {record['id']} 的 event 无效")
        records.append(dict(record))
    return records
