import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(title):
    print("=" * 60)
    print(f" {title.upper()} ".center(60, "="))
    print("=" * 60)

# --- 1. ZERO-SHOT DEMO ---
def zero_shot_demo():
    clear_screen()
    print_header("1. Zero-Shot Classification")
    print("Concept: Asking the AI to classify something with NO examples.\n")
    
    review = "The delivery took two weeks and the box was completely crushed."
    print(f"Input Text: \"{review}\"\n")
    
    print("Executing Zero-Shot Prompt...")
    time.sleep(1)
    
    # Simulating LLM Logic based on prompt constraints
    if "crushed" in review or "took two weeks" in review:
        output = "Negative"
    else:
        output = "Positive"
        
    print(f"\n[AI Output]: {output}")
    input("\nPress Enter to return to the main menu...")

# --- 2. FEW-SHOT DEMO ---
def few_shot_demo():
    clear_screen()
    print_header("2. Few-Shot Categorization")
    print("Concept: Providing examples to force a specific formatting pattern.\n")
    
    prompt = """
    Task: Categorize the support ticket.
    
    Example 1: "My card was charged twice." -> Category: Billing
    Example 2: "The app crashes when I click save." -> Category: Tech Support
    Example 3: "Do you ship to Canada?" -> Category: General Inquiry
    
    New Ticket: "I need to reset my password, the link is broken." -> 
    """
    print("--- Structured Prompt Sent to System ---")
    print(prompt.strip())
    print("---------------------------------------")
    
    time.sleep(1.5)
    # Simulating LLM pattern matching
    simulated_output = "Category: Tech Support"
    
    print(f"\n[AI Pattern-Matched Output]: {simulated_output}")
    input("\nPress Enter to return to the main menu...")

# --- 3. CHAIN-OF-THOUGHT DEMO ---
def chain_of_thought_demo():
    clear_screen()
    print_header("3. Chain-of-Thought (CoT) Reasoning")
    print("Concept: Forcing the system to output its steps before the final answer.\n")
    
    print("Problem: A store has 20 laptops. They sell 5, receive a shipment of 10, and split the remaining stock equally between 2 display rooms. How many laptops per room?")
    
    print("\n[Executing CoT Prompt: 'Think step-by-step']...")
    time.sleep(2)
    
    steps = [
        "Step 1: Start with initial laptops = 20",
        "Step 2: Subtract sold laptops: 20 - 5 = 15",
        "Step 3: Add new shipment: 15 + 10 = 25",
        "Step 4: Divide by display rooms: 25 / 2 = 12.5",
        "Final Answer: 12.5 laptops per room."
    ]
    
    print("\n--- AI Reasoning Path ---")
    for step in steps:
        print(f" -> {step}")
        time.sleep(0.8)
        
    input("\nPress Enter to return to the main menu...")

# --- MAIN MENU ---
def main():
    while True:
        clear_screen()
        print_header("Prompt Engineering Optimization Sandbox")
        print("Select a prompt technique to execute:")
        print("[1] Run Zero-Shot Classification")
        print("[2] Run Few-Shot Pattern Matching")
        print("[3] Run Chain-of-Thought Reasoning")
        print("[4] Exit Framework")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == '1':
            zero_shot_demo()
        elif choice == '2':
            few_shot_demo()
        elif choice == '3':
            chain_of_thought_demo()
        elif choice == '4':
            print("\nExiting Sandbox. Happy Engineering!")
            break
        else:
            print("\nInvalid choice. Try again.")
            time.sleep(1)

if __name__ == "__main__":
    main()