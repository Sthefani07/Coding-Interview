def rotate_zodiac(signs, k):

    k = k % len(signs)

    # in case it negative K
    if k < 0:
        k  += len(signs)

    # rotate using slicing
    rotated_signs = signs[-k:] + signs[:-k]

    return rotated_signs

zodiac_signs = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio","Sagittarius", "Capricorn", "Aquarius", "Pisces"]

k = 6
rotated = rotate_zodiac(zodiac_signs, k)
print(rotated) 
print("--------")  
print("K is iqual to:", k) 