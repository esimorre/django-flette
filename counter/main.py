
import flet
from flet import IconButton, Page, Row, TextField, icons, Text
import req

async def main(page: Page):
    import micropip
    await micropip.install("requests")

    page.title = "Flet counter example"
    page.vertical_alignment = "center"

    txt_number = TextField(value="0", text_align="right", width=100)
    text = Text(value="initial\nline")

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()
        rep =  req.fetch("http://localhost:8000/api")
        text.value = rep["text"]
        page.update()

    page.add(
        Row(
            [
                IconButton(icons.REMOVE, on_click=minus_click),
                txt_number,
                IconButton(icons.ADD, on_click=plus_click),
            ],
            alignment="center",
        )
    )
    page.add(
        Row([text], alignment="center")
    )

flet.app(target=main)
