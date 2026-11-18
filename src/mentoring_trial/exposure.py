"""重建学生被邀请与实际接受指导的不同经历。"""

from collections import defaultdict


def histories(records):
    by_student = defaultdict(list)
    for record in records:
        by_student[str(record["student_id"])].append(record)
    result = {}
    for student, events in by_student.items():
        events.sort(key=lambda event: (event["date"], event["id"]))
        offers = [event for event in events if event["event"] == "offered"]
        sessions = [event for event in events if event["event"] == "session"]
        result[student] = {
            "invited_arm": offers[-1].get("arm") if offers else None,
            "sessions": sessions,
            "transfers": [event for event in events if event["event"] == "transfer"],
            "paused": any(event["event"] == "pause" for event in events),
            "outcomes": [event for event in events if event["event"] == "outcome"],
            "event_ids": [event["id"] for event in events],
        }
    return result
