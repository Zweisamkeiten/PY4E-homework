text = "X-DSPAM-Confidence:    0.8475"
dotpos = text.find('.')
print(float(text[dotpos - 1:]))
