"""区分试点邀请、实际参与与随访结果。"""

from .exposure import histories


def summarize(records):
    result = {}
    for student, history in sorted(histories(records).items()):
        sessions = history["sessions"]
        outcomes = history["outcomes"]
        result[student] = {
            "invited_arm": history["invited_arm"],
            "sessions_received": len(sessions),
            "session_arms": sorted({str(event.get("arm", "unknown")) for event in sessions}),
            "outcome_count": len(outcomes),
            "latest_outcome": outcomes[-1].get("value") if outcomes else None,
            "transferred": bool(history["transfers"]),
            "followup_observed": bool(outcomes),
            "paused": history["paused"],
            "events": history["event_ids"],
        }
    return result
