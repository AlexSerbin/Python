import graphics as gr


# def build_house(window, upper_left_corner, width):
#
#     height = calculate_height(width)
#
# def calculate_height(size):
#     return size * 2
"""
    for M, N in (A, B), (B, C), (C, D), (D, A):                  
        gr.Line(gr.Point(*M), gr.Point(*N)).draw(window)
                        эквивалентно
    gr.Line(gr.Point(*A), gr.Point(*B)).draw(window)
    gr.Line(gr.Point(*B), gr.Point(*C)).draw(window)
    gr.Line(gr.Point(*C), gr.Point(*D)).draw(window)
    gr.Line(gr.Point(*D), gr.Point(*A)).draw(window)
"""

window = gr.GraphWin('FuckThePolice', 600, 600)
alpha = 0.2
def fractal_rectangle(A, B, C, D, deep=100):
    if deep < 1:
        return

    for M, N in (A,B), (B,C), (C,D), (D,A):
        gr.Line(gr.Point(*M), gr.Point(*N)).draw(window)
    A1 = (A[0] * (1 - alpha) + B[0] * alpha), (A[1] * (1 - alpha) + B[1] * alpha)
    B1 = (B[0] * (1 - alpha) + C[0] * alpha), (B[1] * (1 - alpha) + C[1] * alpha)
    C1 = (C[0] * (1 - alpha) + D[0] * alpha), (C[1] * (1 - alpha) + D[1] * alpha)
    D1 = (D[0] * (1 - alpha) + A[0] * alpha), (D[1] * (1 - alpha) + A[1] * alpha)
    fractal_rectangle(A1, B1, C1, D1, deep - 1)

    # gr.Line(gr.Point(*A), gr.Point(*B)).draw(window)
    # gr.Line(gr.Point(*B), gr.Point(*C)).draw(window)
    # gr.Line(gr.Point(*C), gr.Point(*D)).draw(window)
    # gr.Line(gr.Point(*D), gr.Point(*A)).draw(window)

fractal_rectangle((100, 100), (500, 100), (500, 500), (100, 500))
my_rectangle = gr.Rectangle(gr.Point(2, 4), gr.Point(4,8))
my_rectangle.draw(window)


