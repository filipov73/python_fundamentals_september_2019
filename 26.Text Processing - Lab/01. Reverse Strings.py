st_rev = ""
while True:
    st = input()
    if st == "end":
        break
    for ch in reversed(st):
        st_rev += ch
    print(f"{st} = {st_rev}")

# while True:
#     st = input()
#     if st == "end":
#         break
#     st_rev = st[::-1]
#     print(f"{st} = {st_rev}")
