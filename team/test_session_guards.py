"""Offline checks of safeguards around billable session creation."""
import unittest
from run_agent import validate_request

class SessionGuards(unittest.TestCase):
    def test_explicit_budget_and_work_branch(self):
        self.assertEqual(validate_request("12.50", "work/source-audit"), "1250")
    def test_invalid_budgets_do_not_reach_api(self):
        for budget in ["0", "-2", "NaN", "Infinity", "0.001", "not-money"]:
            with self.subTest(budget=budget), self.assertRaises(ValueError):
                validate_request(budget, "work/source-audit")
    def test_main_and_invalid_branches_do_not_reach_api(self):
        for branch in ["", "main", "master", "HEAD", "--all", "bad branch", "work/../main"]:
            with self.subTest(branch=branch), self.assertRaises(ValueError):
                validate_request("10", branch)

if __name__ == "__main__":
    unittest.main()
