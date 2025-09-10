from fastapi import FastAPI

app = FastAPI()

# Greeting messages
greetings = {
    1: "Hello! Wishing you a wonderful day 🌞",
    2: "Good Morning! Stay positive and strong 💪",
    3: "Good Afternoon! Keep up the great work 🚀",
    4: "Good Evening! Relax and recharge 🌇",
    5: "Happy Day! Spread kindness wherever you go 🌸",
    6: "Cheers! You’re doing amazing 🎉",
    7: "Lucky Seven! May success follow you 🍀",
    8: "Stay motivated! Bright days are ahead 🌈",
    9: "Keep smiling! Happiness looks good on you 😊",
    10: "Best wishes! You’re capable of great things ⭐"
}

@app.get("/greet/{number}")
def greet(number: int):
    return {"greeting": greetings.get(number, "Invalid number! Choose 1–10.")}
from fastapi import FastAPI

app = FastAPI()

# Greeting messages
greetings = {
    1: "Hello! Wishing you a wonderful day 🌞",
    2: "Good Morning! Stay positive and strong 💪",
    3: "Good Afternoon! Keep up the great work 🚀",
    4: "Good Evening! Relax and recharge 🌇",
    5: "Happy Day! Spread kindness wherever you go 🌸",
    6: "Cheers! You’re doing amazing 🎉",
    7: "Lucky Seven! May success follow you 🍀",
    8: "Stay motivated! Bright days are ahead 🌈",
    9: "Keep smiling! Happiness looks good on you 😊",
    10: "Best wishes! You’re capable of great things ⭐"
}

@app.get("/greet/{number}")
def greet(number: int):
    return {"greeting": greetings.get(number, "Invalid number! Choose 1–10.")}
