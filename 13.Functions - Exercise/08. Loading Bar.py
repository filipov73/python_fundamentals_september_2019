def loading_bar(prt):
    prt_sign = percent // 10
    return f"[{'%' * prt_sign}{'.' * (10 - prt_sign) }]"
    pass


percent = int(input())
res = loading_bar(percent)
if percent == 100:
    print(f"100% Complete!")
    print(f"{res}")
else:
    print(f"{percent}% {res}")
    print(f"Still loading...")
