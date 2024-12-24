event1 = {"Anaya", "Bob", "Charlie", "Aditya", "Eva"}
event2 = {"Bob", "Charlie", "Naman", "Grace", "Eva"}
print("Q1. Event Attendance:")
print("The students that attended both the events are: ", event1.intersection(event2))
print("The students that attended only 1 event are: ", event1 ^ event2)
print("The students that attended atleast 1 event are: ", event1 | event2)

