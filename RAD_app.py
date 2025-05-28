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


if __name__ == "__main__":
    rad_project = RADProject()
    rad_project.run()
