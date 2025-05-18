import re, randomfrom colorama import Fore, init

#Initialize colorama (autoreset ensures each print resets after use)
init(autoreset=True)

#Destination & joke data
destinations = {
"beaches" ["Bali," "Maldives," "Phuket"],
 "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],
    "cities": ["Tokyo", "Paris", "New York"]
}
jokes = [
    "Why don't programmers like nature? Too many bugs!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why do travelers always feel warm? Because of all their hot spots!"
]

#Helper function to normalize