import json
from datetime import datetime

class HorseTrainerAI:
    def __init__(self):
        self.load_knowledge()
        self.log_file = "training_log.txt"
    
    def load_knowledge(self):
        with open('knowledge_base.json') as f:
            self.knowledge = json.load(f)
    
    def get_advice(self, issue, age=None):
        advice = []
        if issue in self.knowledge:
            if age and age < 3 and 'young_horse' in self.knowledge[issue]:
                advice = self.knowledge[issue]['young_horse']
            else:
                advice = list(self.knowledge[issue].values())[0]
        return advice or ["No advice available"]
    
    def log_session(self, horse_name, issue, solutions):
        with open(self.log_file, 'a') as f:
            f.write(f"\n{datetime.now().strftime('%Y-%m-%d %H:%M')}")
            f.write(f"\nHorse: {horse_name}")
            f.write(f"\nIssue: {issue}")
            f.write("\nSolutions:")
            for sol in solutions:
                f.write(f"\n- {sol}")
            f.write("\n" + "="*30 + "\n")

def main():
    print("🐴 Horse Training AI Assistant 🐴")
    ai = HorseTrainerAI()
    
    while True:
        print("\n1. Get training advice\n2. View logs\n3. Exit")
        choice = input("Select: ").strip()
        
        if choice == "1":
            horse_name = input("Horse name: ").title()
            age = input("Age (years, optional): ")
            issue = input("Training issue: ").lower()
            
            age = int(age) if age.isdigit() else None
            advice = ai.get_advice(issue, age)
            
            print("\nRecommended Solutions:")
            for i, sol in enumerate(advice, 1):
                print(f"{i}. {sol}")
            
            ai.log_session(horse_name, issue, advice)
            
        elif choice == "2":
            print("\nTraining Log:")
            try:
                with open(ai.log_file) as f:
                    print(f.read())
            except FileNotFoundError:
                print("No logs yet!")
        
        elif choice == "3":
            print("Goodbye! 🐎")
            break

if __name__ == "__main__":
    main()
