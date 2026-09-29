facts = {
    "GoodAttendance",
    "HighMarks",
    "CompletedProjects",
    "GoodCommunication"
}

rules = {
    "GoodAcademicPerformance": [
        ["HighMarks", "GoodAttendance"]
    ],

    "ReadyForPlacement": [
        ["GoodAcademicPerformance", "CompletedProjects"]
    ],

    "EligibleForPlacement": [
        ["ReadyForPlacement", "GoodCommunication"]
    ],

    "NeedsExtraPractice": [
        ["GoodAttendance"]
    ]
}

def backward_chaining(goal, visited=None):
    if visited is None:
        visited = set()

    print("Checking:", goal)

    if goal in facts:
        print("  Fact found:", goal)
        return True

    if goal in visited:
        return False

    visited.add(goal)

    if goal in rules:
        for conditions in rules[goal]:
            print("  Rule:", " AND ".join(conditions), "->", goal)

            all_true = True

            for condition in conditions:
                if not backward_chaining(condition, visited):
                    all_true = False
                    break

            if all_true:
                print("  Goal proved:", goal)
                return True

    print("  Cannot prove:", goal)
    return False


goal = "EligibleForPlacement"

print("Backward Chaining Expert System")
print("--------------------------------")
print("Goal:", goal)
print()

result = backward_chaining(goal)

print()
if result:
    print("Final Conclusion:")
    print(goal, "is TRUE")
else:
    print("Final Conclusion:")
    print(goal, "is FALSE")


# Backward Chaining starts with a goal and works backward to find the facts needed to prove it.

# example:

# EligibleForPlacement
#         ↓
# ReadyForPlacement + GoodCommunication
#         ↓
# GoodAcademicPerformance + CompletedProjects
#         ↓
# HighMarks + GoodAttendance