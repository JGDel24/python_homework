import traceback

try:
    with open('diary.txt', 'a') as diary_file:
        prompt = 'What happened today? '
   

    while True:
        line = input(prompt)
        diary_file.write(line + '\n')

        if line.strip().lower() == "done for now":
            break

        prompt = "What else? "

except Exception as e:
    print("An exception occurred.")
    print("Exception type:", type(e).__name__)
    print("Exception message:", str(e))
    print("Traceback:")
    traceback.print_tb(e.__traceback__) 

