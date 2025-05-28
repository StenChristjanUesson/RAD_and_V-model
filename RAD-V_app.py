import time

class RADProject:
    def __init__(self, iterations=4):
        self.iterations = iterations
        self.current_iteration = 0

    def plan(self):
        print(f"[Iteration {self.current_iteration+1}] Planning phase: defining features and goals.")

    def develop(self):
        print(f"[Iteration {self.current_iteration+1}] Development phase: coding and prototyping.")

    def test(self):
        print(f"[Iteration {self.current_iteration+1}] Testing phase: user feedback and bug fixing.")

    def demo(self):
        print(f"[Iteration {self.current_iteration+1}] Demo to client: presenting MVP and gathering feedback.\n")

    def run(self):
        print("Starting RAD development process...\n")
        for i in range(self.iterations):
            self.current_iteration = i
            self.plan()
            time.sleep(0.5)
            self.develop()
            time.sleep(0.5)
            self.test()
            time.sleep(0.5)
            self.demo()
            time.sleep(0.5)
        print("RAD development completed!\n")


class VModelProject:
    def __init__(self):
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
        for phase in self.left_phases:
            print(f"Phase: {phase} - planning and design.")
            time.sleep(0.7)

        print("\nCoding phase completed, starting testing phases...\n")
        for phase in self.right_phases:
            print(f"Phase: {phase} - executing tests.")
            time.sleep(0.7)

        print("\nV-Model development and testing completed!\n")


def main():
    print("Choose the development model to simulate:")
    print("1. RAD (Rapid Application Development)")
    print("2. V-Model")
    print("3. Run both RAD and V-Model")
    choice = input("Enter 1, 2, or 3: ").strip()

    if choice == '1':
        rad_project = RADProject()
        rad_project.run()
    elif choice == '2':
        v_project = VModelProject()
        v_project.run()
    elif choice == '3':
        rad_project = RADProject()
        v_project = VModelProject()
        rad_project.run()
        v_project.run()
    else:
        print("Invalid choice. Please run the program again and enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
