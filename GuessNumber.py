import random

while True:

    number = random.randint(1, 100)
    attempts = 0

    print("\nبه بازی حدس اعداد خوش آمدید!")
    print("یک عدد بین 1 تا 100 حدس بزن.")
    print("شما 5 فرصت دارید.")

    while attempts < 5:

        guess = input("\nعدد مورد نظر را وارد کن: ")

        # بررسی ورودی
        if not guess.isdigit():
            print("لطفاً فقط عدد وارد کن.")
            continue

        guess = int(guess)

        if guess < 1 or guess > 100:
            print("عدد باید بین 1 تا 100 باشد.")
            continue

        attempts = attempts + 1

        print("تلاش:", attempts, "از 5")
        print("جان باقی مانده:", 5 - attempts)

        # بررسی حدس
        if guess == number:
            print("\nآفرین! برنده شدی.")

            if attempts == 1:
                print("رتبه شما: نمونه ای")
            elif attempts == 2:
                print("رتبه شما: بسیار خوبی")
            elif attempts == 3:
                print("رتبه شما: خوب")
            elif attempts == 4:
                print("رتبه شما: قبول")
            else:
                print("رتبه شما: با شانس بردی!")

            break

        elif guess > number:
            print("عدد کوچک تری وارد کن.")

        else:
            print("عدد بزرگ تری وارد کن.")

        # راهنمای نزدیک یا دور
        difference = abs(guess - number)

        if difference <= 5:
            print("خیلی نزدیکی!")
        elif difference <= 15:
            print("نزدیکی، ولی هنوز فاصله داری!")
        else:
            print("خیلی دوری!")

    # بررسی باخت
    if attempts == 5 and guess != number:
        print("\nمتأسفانه باختی!")
        print("عدد مخفی این بود:", number)

    # بازی مجدد
    again = input("\nآیا می خواهی دوباره بازی کنی؟ (بله/خیر): ")

    if again.strip() != "بله":
        print("\nممنون از بازی شما. خداحافظ!")
        break