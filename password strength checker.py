import re
import time

while True:
    # check common passwords
    common_passwords = set(["123456", "password", "Password123", "PassWord123", "123456789", "12345678", "12345", "qwerty", "abc123"])

    def CheckCommonPassword(password: str) -> bool:
        """Checks if the password is among the most common passwords."""
        return password in common_passwords

    def CheckPasswordStrength(password: str) -> (str, int):
        # Criteria for password strength
        scores = {
            "length": 1 if len(password) >= 8 else 0,
            "digit": 1 if re.search(r"\d", password) else 0,
            "uppercase": 1 if re.search(r"[A-Z]", password) else 0,
            "lowercase": 1 if re.search(r"[a-z]", password) else 0,
            "symbol": 1 if re.search(r"\W", password) else 0,
            "common": -1 if CheckCommonPassword(password) else 0
        }
        score = sum(scores.values())
        strength = "Very Weak"
        
        if score < 3:
            strength = "Very Weak"
        elif score == 3:
            strength = "Weak"
        elif score == 4:
            strength = "Moderate"
        elif score == 5:
            strength = "Strong"
        elif score > 5:
            strength = "Very Strong"
        
        return strength, score

    def SuggestImprovements(password: str):
        """Suggests password improvements."""
        suggestions = []
        if len(password) < 8:
            suggestions.append("\033[33m"+"Password must be at least 8 characters."+"\033[0m")
        if not re.search(r"\d", password):
            suggestions.append("\033[33m"+"Password must contain at least one digit."+"\033[0m")
        if not re.search(r"[A-Z]", password):
            suggestions.append("\033[33m"+"Password must contain at least one uppercase letter."+"\033[0m")
        if not re.search(r"[a-z]", password):
            suggestions.append("\033[33m"+"Password must contain at least one lowercase letter."+"\033[0m")
        if not re.search(r"\W", password):
            suggestions.append("\033[33m"+"Password must contain at least one symbol."+"\033[0m")
        if CheckCommonPassword(password):
            suggestions.append("Choose a less common password.")
        
        return suggestions

    def main():
        password = input("\nEnter a password to test its strength: ")
        strength, score = CheckPasswordStrength(password)

        if strength == "Very Weak":
            print("\033[31m"+f"Your password is: {strength} (Score: {score})"+"\033[0m")

        elif strength == "Weak":
            print("\033[31m"+f"Your password is: {strength} (Score: {score})"+"\033[0m")

        elif strength == "Moderate":
            print("\033[33m"+f"Your password is: {strength} (Score: {score})"+"\033[0m")  
        
        elif strength == "Strong":
            print("\033[32m"+f"Your password is: {strength} (Score: {score})"+"\033[0m")

        elif strength == "Very Strong":
            print("\033[32m"+f"Your password is: {strength} (Score: {score})"+"\033[0m")

        if strength in ["Very Weak", "Weak", "Moderate"]:
            suggestions = SuggestImprovements(password)
            print("\033[33m"+"\nSuggestions for improvement:"+"\033[0m")
            for suggestion in suggestions:
                print(f" {suggestion}")

    if __name__ == "__main__":
        main()

    ContinuePrompt = input("\nDo you want to continue? (y/n)")
    if ContinuePrompt.lower() in ("y","yes","yah"):
        pass
        
    elif ContinuePrompt.lower() in ("n","not","nah","not"):
        print("\nThanks for using our service\n")
        break

    else:
        print("\033[31m"+f"'{ContinuePrompt}' is not part of the program"+"\033[0m")
        print("Try again\n")
        time.sleep(4)
        break
