#!/usr/bin/env python3
"""
Demo script to showcase KBC game functionality
"""

import kbc_game

def demo_game():
    """Demo the game with automated responses"""
    print("=" * 60)
    print("🎮 KBC GAME DEMO - AUTOMATED GAMEPLAY")
    print("=" * 60)
    
    game = kbc_game.KBCGame()
    
    # Show welcome (without waiting for input)
    print("\n🎯 WELCOME TO KBC - KAUN BANEGA CROREPATI 🎯")
    print("\nStarting automated demo...")
    
    # Play first few questions automatically
    demo_answers = ['B', 'A', 'C', 'B', 'C']  # Correct answers for first 5 questions
    
    for i in range(min(5, len(game.questions))):
        print(f"\n{'='*60}")
        
        # Display question
        question = game.questions[i]
        prize = game.prize_money[i]
        
        print(f"💡 QUESTION {i + 1} FOR ₹{prize:,}")
        print(f"{'='*60}")
        print(f"\n{question['question']}")
        for option in question['options']:
            print(f"   {option}")
        
        # Use a lifeline on question 3
        if i == 2:
            print(f"\n🆘 Using 50-50 lifeline for demonstration...")
            game.use_lifeline_5050(question)
        
        # Auto-answer
        answer = demo_answers[i]
        print(f"\n🤖 Demo Answer: {answer}")
        
        # Check answer
        if answer == question['correct']:
            game.current_question += 1
            game.total_winnings = game.prize_money[i]
            print(f"\n🎉 CORRECT! Demo player has won ₹{game.total_winnings:,}")
        else:
            print(f"\n❌ WRONG! Game would end here.")
            break
        
        print(f"\nContinuing to next question...")
    
    print(f"\n{'='*60}")
    print(f"📊 DEMO RESULTS:")
    print(f"   Questions answered: {game.current_question}")
    print(f"   Total winnings: ₹{game.total_winnings:,}")
    print(f"   Lifelines used: {[name for name, used in game.lifelines.items() if not used]}")
    print(f"{'='*60}")
    
    print(f"\n🎮 To play the interactive game, run:")
    print(f"   python3 kbc_game.py")
    
    return game.total_winnings

if __name__ == "__main__":
    demo_game()