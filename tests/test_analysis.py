import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from mentoring_trial.analysis import summarize
from mentoring_trial.reports import build_report


class MentoringTrialTests(unittest.TestCase):
    def setUp(self):
        self.events = [
            {"id": "a1", "student_id": "s1", "event": "offered", "date": "2026-01-01", "arm": "new"},
            {"id": "a2", "student_id": "s1", "event": "session", "date": "2026-01-10", "arm": "new"},
            {"id": "a3", "student_id": "s1", "event": "transfer", "date": "2026-02-01"},
            {"id": "a4", "student_id": "s1", "event": "outcome", "date": "2026-03-01", "value": 4.2},
            {"id": "b1", "student_id": "s2", "event": "offered", "date": "2026-01-02", "arm": "usual"},
            {"id": "b2", "student_id": "s2", "event": "pause", "date": "2026-02-02"},
        ]

    def test_invitation_and_exposure_are_not_conflated(self):
        results = summarize(self.events)
        self.assertEqual(results["s1"]["invited_arm"], "new")
        self.assertEqual(results["s1"]["sessions_received"], 1)
        self.assertTrue(results["s1"]["transferred"])

    def test_missing_followup_is_not_zero_outcome(self):
        report = build_report(self.events, "rev-2")
        self.assertEqual(report["followup_missing"], ["s2"])
        self.assertIsNone(report["students"]["s2"]["latest_outcome"])

    def test_result_is_bound_to_source_revision(self):
        self.assertEqual(build_report(self.events, "rev-3")["source_revision"], "rev-3")


if __name__ == "__main__":
    unittest.main()
