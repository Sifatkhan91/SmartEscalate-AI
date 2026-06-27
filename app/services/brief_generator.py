class BriefGenerator:

    def generate(self, action: str, decision: str, priority: str):

        action_lower = action.lower()

        if "delete" in action_lower and "database" in action_lower:

            return {
                "priority": priority,
                "summary": "Deleting this database may permanently remove customer information.",
                "business_risk": "Customer records could be lost permanently.",
                "options": [
                    {
                        "id": 1,
                        "title": "Delete Database",
                        "risk": "Permanent data loss"
                    },
                    {
                        "id": 2,
                        "title": "Cancel Operation",
                        "risk": "Deployment delayed"
                    }
                ],
                "expected_reply": "Delete Database or Cancel Operation"
            }

        if "deploy" in action_lower:

            return {
                "priority": priority,
                "summary": "You are about to deploy changes to the production environment.",
                "business_risk": "Customers could experience downtime if deployment fails.",
                "options": [
                    {
                        "id": 1,
                        "title": "Deploy",
                        "risk": "Potential downtime"
                    },
                    {
                        "id": 2,
                        "title": "Cancel",
                        "risk": "Deployment delayed"
                    }
                ],
                "expected_reply": "Deploy or Cancel"
            }

        return {
            "priority": priority,
            "summary": action,
            "business_risk": "Human approval is required before continuing.",
            "options": [
                {
                    "id": 1,
                    "title": "Continue",
                    "risk": "Accept the proposed action"
                },
                {
                    "id": 2,
                    "title": "Cancel",
                    "risk": "Stop execution"
                }
            ],
            "expected_reply": "Continue or Cancel"
        }