import time

time_input = str(input("Please enter the time in HH:MM:SS format: "))
print(f"Time Selected: {time_input}")

print(f"wait..")
while True:
    if time_input == time.strftime("%H:%M:%S"):
        print("Alarm now")
        break
