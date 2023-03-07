from functools import partial

import flet as ft


def main(page: ft.Page):
    """Main App"""

    page.title = "JCal"
    page.theme_mode = "dark"
    page.padding = 20 
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.window_max_height = 600
    page.window_max_width = 400

    

    calc_input = ft.TextField(text_align="right", width=300, autofocus=True)
    
    page.add(calc_input)

    def enterdata(e, number):
        """Function to print entered data"""
        if (number == 'C'):
            calc_input.value = ''
            page.add(calc_input)
        else:
            calc_input.value = calc_input.value + number
            page.add(calc_input)

    def calculate(e):
        """Function to display calculated data"""
        
        
        output = eval(calc_input.value)
        calc_input.value = output
        page.add(calc_input)
        
        

    #Creating buttons 7 to +
    but7 = ft.ElevatedButton("7", on_click=partial(enterdata, number = '7'))
    but8 = ft.ElevatedButton("8", on_click=partial(enterdata, number = '8'))
    but9 = ft.ElevatedButton("9", on_click=partial(enterdata, number = '9'))
    but_add = ft.ElevatedButton("+", on_click=partial(enterdata, number = '+'), bgcolor="orange", color="black")

    #Adding buttons to row and page
    row1 = ft.Row(width=300,controls=[but7, but8, but9, but_add], alignment="center")
    page.add(row1)

    #Creating buttons 4 to -
    but4 = ft.ElevatedButton("4", on_click=partial(enterdata, number = '4'))
    but5 = ft.ElevatedButton("5", on_click=partial(enterdata, number = '5'))
    but6 = ft.ElevatedButton("6", on_click=partial(enterdata, number = '6'))
    but_minus = ft.ElevatedButton("-", on_click=partial(enterdata, number = '-'), bgcolor="orange", color="black")

    #Adding buttons to row and page
    row2 = ft.Row(width=300,controls=[but4, but5, but6, but_minus], alignment="center")
    page.add(row2)

    #Creating buttons 1 to x
    but1 = ft.ElevatedButton("1", on_click=partial(enterdata, number = '1'))
    but2 = ft.ElevatedButton("2", on_click=partial(enterdata, number = '2'))
    but3 = ft.ElevatedButton("3", on_click=partial(enterdata, number = '3'))
    but_mul = ft.ElevatedButton("X", on_click=partial(enterdata, number = '*'), bgcolor="orange", color="black")

    #Adding buttons to row and page
    row3 = ft.Row(width=300,controls=[but1, but2, but3, but_mul], alignment="center")
    page.add(row3)

    #Creating . to /
    but_dot = ft.ElevatedButton(".", on_click=partial(enterdata, number = '.'))
    but0 = ft.ElevatedButton("0", on_click=partial(enterdata, number = '0'))
    but_clear = ft.ElevatedButton("AC", on_click=partial(enterdata, number = 'C'), bgcolor="orange", color="black")
    but_clear = ft.ElevatedButton("AC", on_click=partial(enterdata, number = 'C'), bgcolor="orange", color="black")
    but_divide = ft.ElevatedButton("/", on_click=partial(enterdata, number = '/'), bgcolor="orange", color="black")

    #Adding to row and page
    row4 = ft.Row(width=300,controls=[but_dot, but0, but_clear, but_divide], alignment="center")
    page.add(row4)

    #Adding = button
    but_equal = ft.ElevatedButton("=", width=300,on_click=calculate, bgcolor="cyan", color="black")
    page.add(but_equal)



ft.app(target=main, view=ft.WEB_BROWSER)