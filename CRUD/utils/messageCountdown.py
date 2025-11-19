import time

def messageNcountdown(message):
    # Result message
    print(f"\n{message}\n")
            
    # Countdown
    seconds = 5
    for i in range(seconds, 0, -1):
        print(f"redirect dalam {i}...")
        time.sleep(1)