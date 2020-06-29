def cipher(target):
    result = ""
    for i in target:
        if i.islower():
            result += chr(219 - ord(i))
        else:
            result += i
    return result

i = "I was king"
result = cipher(i)
result2 = cipher(result)

print("元の値" + i)
print("暗号化" + result)
print("復号化" + result2)
