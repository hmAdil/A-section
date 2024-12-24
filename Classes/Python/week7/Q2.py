positive_keywords = ["excellent", "great", "satisfied", "happy"]
negative_keywords = ["poor", "bad", "disappointed", "unsatisfied"]
keyword_counts = {"excellent": 0, "great": 0, "satisfied": 0, "happy": 0, "poor": 0, "bad": 0, "disappointed": 0, "unsatisfied": 0}
good_feedback_count = 0
bad_feedback_count = 0

with open("/home/b3ast/Python Stuff/week7/feedback.txt", "r") as file:
    lines = file.readlines()
    print("Contents of feedback.txt:")
    for line in lines:
        print(line.strip())  

good_feedback = []
bad_feedback = []

for line in lines:
    line_lower = line.lower()  # Convert line to lowercase
    is_positive = False        # I'm initializing -ve and +ve variables.
    is_negative = False
    
    for keyword in positive_keywords:
        if keyword in line_lower:
            keyword_counts[keyword] += 1
            is_positive = True

    for keyword in negative_keywords:
        if keyword in line_lower:
            keyword_counts[keyword] += 1
            is_negative = True
    
    if is_positive and not is_negative:
        good_feedback.append(line)
        good_feedback_count += 1
    elif is_negative and not is_positive:
        bad_feedback.append(line)
        bad_feedback_count += 1

with open("good_feedback.txt", "a") as good_feed:
    good_feed.writelines(good_feedback)  # `writelines` writes the list of lines at once

with open("bad_feedback.txt", "a") as bad_feed:
    bad_feed.writelines(bad_feedback)  

with open("keyword_counts.csv", "a") as count_feed:
    if count_feed.tell() == 0:  # here tell function checks if the file is empty
        count_feed.write("Keyword, Count\n")  # Add header for the first write
    
    for keyword, count in keyword_counts.items():
        count_feed.write(f"{keyword}, {count}\n")
    
    count_feed.write(f"Good Feedback, {good_feedback_count}\n")
    count_feed.write(f"Bad Feedback, {bad_feedback_count}\n")

print("\nTotal good feedback:", good_feedback_count)
print("Total bad feedback:", bad_feedback_count)
print("Good feedback written to good_feedback.txt")
print("Bad feedback written to bad_feedback.txt")

for keyword, count in keyword_counts.items():
    print(f"Keyword: {keyword}, Count: {count}")

print("Overall counts written to keyword_counts.csv")
print("\nFeedback processing complete.")
