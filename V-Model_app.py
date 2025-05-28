import time

class VModelProject:
    def __init__(self):
        # Define phases (left and right of the 'V')
        self.left_phases = [
            "Requirements Analysis",
            "System Design",
            "Architecture Design",
            "Module Design",
            "Coding"
        ]
        self.right_phases = [
            "Unit Testing",
            "Integration Testing",
            "System Testing",
            "Acceptance Testing"
        ]

    def run(self):
        print("Starting V-Model development process...\n")
        # Left side: planning and design phases
        for phase in self.left_phases:
            print(f"Phase: {phase} - planning and design.")
            time.sleep(0.7)

        print("\nCoding phase completed, starting testing phases...\n")
        # Right side: testing phases (in reverse order of left phases)
        for phase in self.right_phases:
            print(f"Phase: {phase} - executing tests.")
            time.sleep(0.7)

        print("\nV-Model development and testing completed!\n")


if __name__ == "__main__":
    v_project = VModelProject()
    v_project.run()
