#!/usr/bin/env python3
"""
KBC (Kaun Banega Crorepati) Quiz Game
A simple implementation of the famous quiz show game.
"""

import random
import json


class KBCGame:
    def __init__(self):
        self.current_question = 0
        self.total_winnings = 0
        self.lifelines = {
            '50-50': True,
            'audience_poll': True,
            'phone_friend': True
        }
        self.prize_money = [
            1000, 2000, 3000, 5000, 10000,
            20000, 40000, 80000, 160000, 320000,
            640000, 1250000, 2500000, 5000000, 10000000
        ]
        self.questions = self.load_questions()
    
    def load_questions(self):
        """Load questions from the questions data"""
        return [
            {
                "question": "What is the capital of India?",
                "options": ["A) Mumbai", "B) Delhi", "C) Kolkata", "D) Chennai"],
                "correct": "B",
                "difficulty": 1
            },
            {
                "question": "Who wrote the Indian National Anthem?",
                "options": ["A) Rabindranath Tagore", "B) Bankim Chandra", "C) Mahatma Gandhi", "D) Subhas Chandra Bose"],
                "correct": "A",
                "difficulty": 1
            },
            {
                "question": "What is the largest planet in our solar system?",
                "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Saturn"],
                "correct": "C",
                "difficulty": 2
            },
            {
                "question": "In which year did India gain independence?",
                "options": ["A) 1945", "B) 1947", "C) 1948", "D) 1950"],
                "correct": "B",
                "difficulty": 2
            },
            {
                "question": "What is the chemical symbol for Gold?",
                "options": ["A) Go", "B) Gd", "C) Au", "D) Ag"],
                "correct": "C",
                "difficulty": 3
            },
            {
                "question": "Who painted the Mona Lisa?",
                "options": ["A) Van Gogh", "B) Picasso", "C) Da Vinci", "D) Michelangelo"],
                "correct": "C",
                "difficulty": 3
            },
            {
                "question": "What is the square root of 144?",
                "options": ["A) 12", "B) 14", "C) 16", "D) 18"],
                "correct": "A",
                "difficulty": 2
            },
            {
                "question": "Which element has the atomic number 1?",
                "options": ["A) Helium", "B) Hydrogen", "C) Oxygen", "D) Carbon"],
                "correct": "B",
                "difficulty": 3
            },
            {
                "question": "Who is known as the Father of the Nation in India?",
                "options": ["A) Nehru", "B) Gandhi", "C) Patel", "D) Bose"],
                "correct": "B",
                "difficulty": 1
            },
            {
                "question": "What is the speed of light in vacuum?",
                "options": ["A) 3×10^8 m/s", "B) 3×10^6 m/s", "C) 3×10^10 m/s", "D) 3×10^12 m/s"],
                "correct": "A",
                "difficulty": 4
            },
            {
                "question": "Which is the longest river in the world?",
                "options": ["A) Amazon", "B) Nile", "C) Yangtze", "D) Mississippi"],
                "correct": "B",
                "difficulty": 3
            },
            {
                "question": "What is the currency of Japan?",
                "options": ["A) Yuan", "B) Won", "C) Yen", "D) Rupiah"],
                "correct": "C",
                "difficulty": 2
            },
            {
                "question": "Who developed the theory of relativity?",
                "options": ["A) Newton", "B) Einstein", "C) Galileo", "D) Tesla"],
                "correct": "B",
                "difficulty": 3
            },
            {
                "question": "What is the hardest natural substance on Earth?",
                "options": ["A) Gold", "B) Iron", "C) Diamond", "D) Platinum"],
                "correct": "C",
                "difficulty": 2
            },
            {
                "question": "In which year was the first computer bug found?",
                "options": ["A) 1945", "B) 1947", "C) 1950", "D) 1955"],
                "correct": "B",
                "difficulty": 5
            }
        ]
    
    def display_welcome(self):
        """Display welcome message and game rules"""
        print("="*60)
        print("    🎯 WELCOME TO KBC - KAUN BANEGA CROREPATI 🎯")
        print("="*60)
        print("\n📋 GAME RULES:")
        print("• Answer 15 questions correctly to win ₹1 Crore!")
        print("• Each question has 4 options (A, B, C, D)")
        print("• You have 3 lifelines: 50-50, Audience Poll, Phone a Friend")
        print("• Type 'quit' anytime to leave with current winnings")
        print("• Type 'lifeline' to use a lifeline")
        print("\n💰 PRIZE STRUCTURE:")
        for i, prize in enumerate(self.prize_money, 1):
            print(f"   Question {i:2d}: ₹{prize:,}")
        print("="*60)
    
    def use_lifeline_5050(self, question):
        """Use 50-50 lifeline"""
        if not self.lifelines['50-50']:
            print("❌ 50-50 lifeline already used!")
            return False
        
        correct_option = question['correct']
        options = ['A', 'B', 'C', 'D']
        wrong_options = [opt for opt in options if opt != correct_option]
        
        # Remove 2 wrong options randomly
        to_remove = random.sample(wrong_options, 2)
        remaining_options = [opt for opt in options if opt not in to_remove]
        
        print("\n🔥 50-50 Lifeline Used!")
        print("Two wrong answers have been eliminated:")
        for opt in remaining_options:
            idx = ord(opt) - ord('A')
            print(f"   {question['options'][idx]}")
        
        self.lifelines['50-50'] = False
        return True
    
    def use_lifeline_audience(self, question):
        """Use audience poll lifeline"""
        if not self.lifelines['audience_poll']:
            print("❌ Audience Poll lifeline already used!")
            return False
        
        correct_option = question['correct']
        
        # Simulate audience poll with correct answer having higher probability
        poll_results = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
        
        # Give correct answer 60-80% chance
        correct_percentage = random.randint(60, 80)
        poll_results[correct_option] = correct_percentage
        
        # Distribute remaining percentage among other options
        remaining = 100 - correct_percentage
        other_options = [opt for opt in ['A', 'B', 'C', 'D'] if opt != correct_option]
        
        for i, opt in enumerate(other_options):
            if i == len(other_options) - 1:
                poll_results[opt] = remaining
            else:
                percentage = random.randint(0, remaining // 2)
                poll_results[opt] = percentage
                remaining -= percentage
        
        print("\n📊 Audience Poll Results:")
        for opt in ['A', 'B', 'C', 'D']:
            print(f"   Option {opt}: {poll_results[opt]}%")
        
        self.lifelines['audience_poll'] = False
        return True
    
    def use_lifeline_phone(self, question):
        """Use phone a friend lifeline"""
        if not self.lifelines['phone_friend']:
            print("❌ Phone a Friend lifeline already used!")
            return False
        
        correct_option = question['correct']
        
        # Simulate friend's confidence (70-90% chance of giving correct answer)
        if random.randint(1, 100) <= 80:
            confidence = random.choice(["quite confident", "pretty sure", "think"])
            print(f"\n📞 Your friend says: 'I {confidence} the answer is {correct_option}'")
        else:
            wrong_options = [opt for opt in ['A', 'B', 'C', 'D'] if opt != correct_option]
            friend_answer = random.choice(wrong_options)
            print(f"\n📞 Your friend says: 'I'm not sure, but I think it might be {friend_answer}'")
        
        self.lifelines['phone_friend'] = False
        return True
    
    def display_question(self, question_num):
        """Display current question"""
        if question_num >= len(self.questions):
            return None
        
        question = self.questions[question_num]
        prize = self.prize_money[question_num]
        
        print(f"\n{'='*60}")
        print(f"💡 QUESTION {question_num + 1} FOR ₹{prize:,}")
        print(f"{'='*60}")
        print(f"\n{question['question']}")
        print()
        for option in question['options']:
            print(f"   {option}")
        
        # Show available lifelines
        available_lifelines = [name for name, available in self.lifelines.items() if available]
        if available_lifelines:
            print(f"\n🆘 Available Lifelines: {', '.join(available_lifelines)}")
        
        return question
    
    def handle_lifeline_choice(self, question):
        """Handle lifeline selection"""
        print("\nAvailable Lifelines:")
        lifeline_options = []
        if self.lifelines['50-50']:
            lifeline_options.append("1) 50-50")
        if self.lifelines['audience_poll']:
            lifeline_options.append("2) Audience Poll")
        if self.lifelines['phone_friend']:
            lifeline_options.append("3) Phone a Friend")
        
        if not lifeline_options:
            print("❌ No lifelines available!")
            return
        
        for option in lifeline_options:
            print(f"   {option}")
        
        choice = input("\nEnter lifeline number (or 'back' to return): ").strip().lower()
        
        if choice == 'back':
            return
        elif choice == '1' and self.lifelines['50-50']:
            self.use_lifeline_5050(question)
        elif choice == '2' and self.lifelines['audience_poll']:
            self.use_lifeline_audience(question)
        elif choice == '3' and self.lifelines['phone_friend']:
            self.use_lifeline_phone(question)
        else:
            print("❌ Invalid choice!")
    
    def play_game(self):
        """Main game loop"""
        self.display_welcome()
        
        print("\nPress Enter to start the game...")
        input()
        
        while self.current_question < len(self.questions):
            question = self.display_question(self.current_question)
            if not question:
                break
            
            # Get player's answer
            while True:
                answer = input(f"\nYour answer (A/B/C/D), 'lifeline', or 'quit': ").strip().upper()
                
                if answer == 'QUIT':
                    print(f"\n🏃 You chose to quit with ₹{self.total_winnings:,}")
                    print("Thanks for playing KBC! 👋")
                    return
                
                elif answer == 'LIFELINE':
                    self.handle_lifeline_choice(question)
                    continue
                
                elif answer in ['A', 'B', 'C', 'D']:
                    break
                
                else:
                    print("❌ Please enter A, B, C, D, 'lifeline', or 'quit'")
            
            # Check answer
            if answer == question['correct']:
                self.current_question += 1
                self.total_winnings = self.prize_money[self.current_question - 1]
                
                print(f"\n🎉 CORRECT! You've won ₹{self.total_winnings:,}")
                
                if self.current_question == len(self.questions):
                    print("\n🏆 CONGRATULATIONS! YOU'VE WON ₹1 CRORE! 🏆")
                    print("You are the KBC CHAMPION! 👑")
                    return
                
                print("Moving to the next question...")
                input("Press Enter to continue...")
            
            else:
                correct_option = question['correct']
                print(f"\n❌ WRONG ANSWER!")
                print(f"The correct answer was {correct_option}")
                print(f"💔 You leave with ₹{self.total_winnings:,}")
                print("Better luck next time! Thanks for playing KBC! 👋")
                return


def main():
    """Main function to start the game"""
    game = KBCGame()
    game.play_game()


if __name__ == "__main__":
    main()