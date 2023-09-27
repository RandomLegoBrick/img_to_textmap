try:
    import math
    from PIL import Image
    from tkinter import Tk, filedialog, Text
    from tkinter.ttk import Button
    import pyperclip

    window = Tk()
    output = Text(window)
    output.pack()
    window.iconify()
    def copybox():
        pyperclip.copy(output.get("0.0", "end"))
        window.destroy()
    copy = Button(window, text="COPY", command=copybox)
    copy.pack(fill="x")

    PATH = filedialog.askopenfile().name

    if not PATH:
        window.destroy()
        exit()

    chrs = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890àáâãäåāăąǎǟǡǻȁȃȧḁạảấầẩẫậắằẳẵặḃḅḇçćĉċčḉďḋḍḏḑḓèéêëēĕėęěȅȇȩḕḗḙḛḝẹẻẽếềểễệḟĝğġģǧǵḡĥȟḣḥḧḩḫẖìíîïĩīĭįǐȉȋḭḯỉịĵǰķǩḱḳḵĺļľḷḹḻḽḿṁṃñńņňǹṅṇṉṋòóôõöōŏőơǒǫǭȍȏȫȭȯȱṍṏṑṓọỏốồổỗộớờởỡợṕṗŕŗřȑȓṙṛṝṟśŝşšșṡṣṥṧṩţťțṫṭṯṱẗùúûüũūŭůűųưǔǖǘǚǜȕȗṳṵṷṹṻụủứừửữựṽṿŵẁẃẅẇẉẘẋẍýÿŷȳẏẙỳỵỷỹźżžẑẓẕ"
    img = Image.open(PATH)
    w = img.width
    h = img.height
    img = img.convert("RGBA")
    data = img.getdata()
    bmp = [[] for i in range(h)]
    usedColors = [(0, 0, 0, 0)]
    y = -1
    for i in range(len(data)):
        color = data[i]

        if i % w == 0:
            y += 1
            
        if not (color in usedColors):
            usedColors.append(color)

        
        bmp[y].append(chrs[usedColors.index(color)])

    finalCode = "[\n"

    for i in range(len(bmp)):
        bmp[i] = "".join(bmp[i])

    for i in bmp:
        finalCode += '    "'+i+'",\n'
    finalCode += "]; \n\n"

    clrs = '\n'
    for i, c in enumerate(usedColors):
        clrs += '    "'+chrs[i]+'" : color({0}, {1}, {2}, {3}),\n'.format(c[0], c[1], c[2], c[3])
    finalCode += '{'+clrs+'}'

    output.insert("end", finalCode)
    window.deiconify()

    window.mainloop()
except:
    exit()