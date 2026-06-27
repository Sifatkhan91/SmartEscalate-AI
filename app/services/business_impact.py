class BusinessImpactAnalyzer:

    def analyze(self, action: str):

        action_lower = action.lower()

        if "delete" in action_lower and "database" in action_lower:
            return {
                "impact": "Customer information could be permanently deleted.",
                "severity": "CRITICAL"
            }

        if "deploy" in action_lower:
            return {
                "impact": "Customers may experience downtime if deployment fails.",
                "severity": "HIGH"
            }

        if "credential" in action_lower:
            return {
                "impact": "Unauthorized access may become possible.",
                "severity": "CRITICAL"
            }

        if "force push" in action_lower:
            return {
                "impact": "Shared commit history may be overwritten.",
                "severity": "HIGH"
            }

        return {
            "impact": "Human approval is recommended before continuing.",
            "severity": "MEDIUM"
        }