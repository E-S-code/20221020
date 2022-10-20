#%%
uru = int(input("西暦で年を入力してください。"))
if uru % 400 == 0:
    print(uru,"年はうるう年です。")
elif uru % 100 == 0:
    print(uru,"年はうるう年ではありません。")
elif uru % 4 == 0:
    print(uru,"年はうるう年です。")
else:
    print(uru,"年はうるう年ではありません。")
# %%
