def data_types(word, st):
    if word == "string":
        if not st.isdigit():
            print(f"${st}$")
    elif word == "real":
        if bool(float(st)):
            print(f"{float(st) * 1.5:.2f}")
    elif word == "int":
        if st.isdigit():
            print(f"{int(st) * 2}")


word = input()
st = input()
data_types(word, st)
