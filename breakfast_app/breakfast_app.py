
import random
import datetime as dt
import os
import json


BREADS  = ["לחם לבן", "לחם מלא", "פיתה", "טוסט", "טורטיה", "לחמניה"]
SPREADS = ["שוקולד", "חמאת בוטנים", "חומוס", "גבינה לבנה", "קוטג׳"]
VEGGIES = ["עגבנייה", "מלפפון", "גזר", "גמבה"]
FRUITS  = ["תפוח", "בננה", "אגס", "תות"]
DRINKS  = ["מים", "שוקו", "מיץ תפוזים", "מיץ תפוחים"]

def pick_one(title, opts):
    print(f"\n{title}"); [print(f"{i+1}. {o}") for i,o in enumerate(opts)]
    i = int(input("בחר מספר: ").strip()) - 1
    return opts[i]

def pick_multi(title, opts):
    print(f"\n{title}"); [print(f"{i+1}. {o}") for i,o in enumerate(opts)]
    raw = input("בחר מספרים בפסיקים (או Enter לדלג): ").strip()
    if not raw: return []
    idxs = [int(x)-1 for x in raw.split(",") if x.strip()]
    return [opts[i] for i in idxs if 0 <= i < len(opts)]

name   = input("מה השם שלך? ").strip() or "אנונימי"
bread  = pick_one("🍞 בחר/י לחם:", BREADS)
spread = pick_one("🍫 בחר/י ממרח:", SPREADS)
vegs   = pick_multi("🥒 בחר/י ירקות (אפשר כמה):", VEGGIES)
frts   = pick_multi("🍎 בחר/י פירות (אפשר כמה):", FRUITS)
drink  = pick_one("🧃 בחר/י שתייה:", DRINKS)

print("\n✅ סיכום:")
print(f"- שם: {name}")
print(f"- לחם: {bread}")
print(f"- ממרח: {spread}")
print(f"- ירקות: {', '.join(vegs) if vegs else 'בלי'}")
print(f"- פירות: {', '.join(frts) if frts else 'בלי'}")
print(f"- שתייה: {drink}")