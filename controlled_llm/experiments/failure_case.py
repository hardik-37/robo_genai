from main import run
try:
    run("give me a bad answer")
except RuntimeError as e:
    print("Handled failure:", e)
