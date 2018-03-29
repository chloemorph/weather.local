import scrollphathd as sphd

def draw_pixels(a,offset):
    for pixel in a:
        sphd.set_pixel(pixel[0]+offset, pixel[1]+1, 0.25)

def draw(i,c):
    a = []
    if c == "1":
        a = [[1,0],[1,1],[1,2],[1,3],[1,4]]
    elif c == "2":
        a = [[0,0],[1,0],[2,0],[2,1],[2,2],[1,2],[0,2],[0,3],[0,4],[1,4],[2,4]]
    elif c == "3":
        a = [[0,0],[1,0],[2,0],[2,1],[2,2],[1,2],[0,2],[0,4],[2,3],[1,4],[2,4]]
    elif c == "4":
        a = [[0,0],[0,1],[0,2],[1,2],[2,2],[2,0],[2,1],[2,3],[2,4]]
    elif c == "5":
        a = [[2,0],[1,0],[0,0],[0,1],[0,2],[1,2],[2,2],[2,3],[2,4],[1,4],[0,4]]
    elif c == "6":
        a = [[0,0],[0,1],[0,2],[0,3],[0,4],[1,4],[2,4],[2,3],[2,2],[1,2]]
    elif c == "7":
        a = [[0,0],[1,0],[2,0],[2,1],[2,2],[2,3],[2,4]]
    elif c == "8":
        a = [[0,0],[1,0],[2,0],[0,1],[2,1],[0,2],[1,2],[2,2],[0,3],[2,3],[0,4],[1,4],[2,4]]
    elif c == "9":
        a = [[0,0],[1,0],[2,0],[0,1],[2,1],[0,2],[1,2],[2,2],[2,3],[2,4]]
    elif c == "0":
        a = [[0,0],[1,0],[2,0],[0,1],[2,1],[0,2],[1,2],[2,2],[0,3],[2,3],[0,4],[1,4],[2,4]]
    elif c == "+":
        a = [[1,1],[1,2],[1,3],[0,2],[2,2]]
    elif c == "-":
        a = [[0,2],[1,2],[2,2]]
    elif c == ".":
        a = [[1,4]]
    else:
        a = [[0,0],[1,1],[2,2]]
    draw_pixels(a,i * 4)

def write(str):
    print(str)
    for i,c in enumerate(str):
        if i > 3: break
        draw(i,c)

