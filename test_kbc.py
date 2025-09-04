#!/usr/bin/env python3
"""
Simple test script for KBC game functionality
"""

import kbc_game

def test_game_initialization():
    """Test game initialization"""
    print("Testing game initialization...")
    game = kbc_game.KBCGame()
    
    assert len(game.questions) == 15, "Should have 15 questions"
    assert len(game.prize_money) == 15, "Should have 15 prize levels"
    assert game.current_question == 0, "Should start at question 0"
    assert game.total_winnings == 0, "Should start with 0 winnings"
    assert all(game.lifelines.values()), "All lifelines should be available"
    
    print("✅ Game initialization test passed")

def test_question_structure():
    """Test question data structure"""
    print("Testing question structure...")
    game = kbc_game.KBCGame()
    
    for i, question in enumerate(game.questions):
        assert 'question' in question, f"Question {i} missing 'question' field"
        assert 'options' in question, f"Question {i} missing 'options' field"
        assert 'correct' in question, f"Question {i} missing 'correct' field"
        assert 'difficulty' in question, f"Question {i} missing 'difficulty' field"
        
        assert len(question['options']) == 4, f"Question {i} should have 4 options"
        assert question['correct'] in ['A', 'B', 'C', 'D'], f"Question {i} has invalid correct answer"
        assert 1 <= question['difficulty'] <= 5, f"Question {i} has invalid difficulty"
    
    print("✅ Question structure test passed")

def test_lifelines():
    """Test lifeline functionality"""
    print("Testing lifelines...")
    game = kbc_game.KBCGame()
    question = game.questions[0]
    
    # Test 50-50
    initial_5050 = game.lifelines['50-50']
    game.use_lifeline_5050(question)
    assert game.lifelines['50-50'] != initial_5050, "50-50 lifeline should be used"
    
    # Test audience poll
    initial_audience = game.lifelines['audience_poll']
    game.use_lifeline_audience(question)
    assert game.lifelines['audience_poll'] != initial_audience, "Audience poll should be used"
    
    # Test phone friend
    initial_phone = game.lifelines['phone_friend']
    game.use_lifeline_phone(question)
    assert game.lifelines['phone_friend'] != initial_phone, "Phone friend should be used"
    
    print("✅ Lifeline functionality test passed")

def test_prize_structure():
    """Test prize money structure"""
    print("Testing prize structure...")
    game = kbc_game.KBCGame()
    
    expected_prizes = [
        1000, 2000, 3000, 5000, 10000,
        20000, 40000, 80000, 160000, 320000,
        640000, 1250000, 2500000, 5000000, 10000000
    ]
    
    assert game.prize_money == expected_prizes, "Prize structure doesn't match expected values"
    assert game.prize_money[-1] == 10000000, "Final prize should be 1 crore (10 million)"
    
    print("✅ Prize structure test passed")

def run_all_tests():
    """Run all tests"""
    print("=" * 50)
    print("🧪 RUNNING KBC GAME TESTS")
    print("=" * 50)
    
    try:
        test_game_initialization()
        test_question_structure()
        test_lifelines()
        test_prize_structure()
        
        print("\n" + "=" * 50)
        print("🎉 ALL TESTS PASSED! KBC GAME IS READY TO PLAY!")
        print("=" * 50)
        
        # Show sample gameplay
        print("\n📋 Sample Question Preview:")
        game = kbc_game.KBCGame()
        sample = game.questions[0]
        print(f"Q: {sample['question']}")
        for opt in sample['options']:
            print(f"   {opt}")
        print(f"Correct Answer: {sample['correct']}")
        
        print(f"\n💰 Prize Structure: ₹{game.prize_money[0]:,} → ₹{game.prize_money[-1]:,}")
        print(f"🆘 Lifelines: {list(game.lifelines.keys())}")
        
    except AssertionError as e:
        print(f"❌ Test failed: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False
    
    return True

if __name__ == "__main__":
    run_all_tests()