def get_valid_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                raise ValueError("Value must be non-negative.")
            return value
        except ValueError as e:
            print(f"Invalid input. {e}")

# Input from user
total_emails = get_valid_input("Enter total number of emails: ")
emails_with_free = get_valid_input("Enter number of emails containing 'free': ")
spam_emails = get_valid_input("Enter number of spam emails: ")
spam_and_free = get_valid_input("Enter number of emails that are both spam and contain 'free': ")

# Validation
if total_emails == 0:
    print("Total emails cannot be zero.")
elif emails_with_free > total_emails or spam_emails > total_emails or spam_and_free > spam_emails:
    print("Invalid input: counts cannot exceed total or respective categories.")
else:
    # Bayes’ Theorem
    P_spam = spam_emails / total_emails
    P_free = emails_with_free / total_emails
    P_free_given_spam = spam_and_free / spam_emails

    # Compute P(Spam | Free)
    P_spam_given_free = (P_free_given_spam * P_spam) / P_free if P_free != 0 else 0

    # Output
    print(f"\nEstimated P(Spam | Email contains 'free') = {P_spam_given_free:.4f}")
