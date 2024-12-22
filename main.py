import flet as ft

def main(page: ft.Page):
    page.title = "Walimatul Khitan Aiham"
    page.padding = 0
    page.bgcolor="white"
    page.vertical_alignment = "start"
    page.horizontal_alignment = "center"
    page.scroll = "auto"
    page.fonts = {
        "Poppins": "fonts/Poppins-Regular.ttf",
        "Courgette": "fonts/Courgette-Regular.ttf",
        "GreatVibes": "fonts/GreatVibes-Regular.ttf"
    }

    def open_google_maps(e):
        page.launch_url("https://www.google.com")

    page.add(
        ft.Column(
            controls=[
                # Landing Section
                ft.Stack(
                    alignment=ft.alignment.center,
                    controls=[
                        ft.Container(
                            expand=True,
                            width=page.width,
                            height=page.height,
                            bgcolor="white",
                        ),

                        ft.Image(
                            expand=True,
                            src="bg_land_page.png",
                            fit=ft.ImageFit.COVER,
                            width=450,
                            height=page.height,
                            border_radius=20
                        ),

                        ft.Image(
                            expand=True,
                            src="bg_putih.png",
                            fit=ft.ImageFit.COVER,
                            width=300,
                            height=500,
                            border_radius=50,
                        ),

                        ft.Column(
                            controls=[
                                ft.Text("Assalamu'alaikum Wr. Wb.",
                                    size=22,
                                    text_align="center",
                                    weight=ft.FontWeight.BOLD,
                                    color="#3f4b2e",
                                    font_family="GreatVibes",
                                ),

                                ft.Text(
                                    "Dengan memohon Rahmat dan Ridho Allah\nKami mengundang Bapak/Ibu/Saudara/i\nuntuk menghadiri acara tasyakuran\nwalimatul khitan putra kami:",
                                    size=12,
                                    text_align="center",
                                    color="#303923",
                                    font_family="Poppins"
                                ),

                                ft.Divider(height=20, color="transparent"),

                                ft.Container(
                                    bgcolor="white10",
                                    width=186,
                                    height=186,
                                    shape=ft.BoxShape("circle"),
                                    image_src="profil.png",
                                    image_fit="cover",
                                    shadow=ft.BoxShadow(
                                        spread_radius=4,
                                        blur_radius=8,
                                        color=ft.colors.with_opacity(0.71, "#3f4b2e"),
                                    )
                                ),

                                ft.Divider(height=10, color="transparent"),

                                ft.Text(
                                    "Aiham Zunzadi Azhar",
                                    size=20,
                                    weight=ft.FontWeight.BOLD,
                                    color="#3f4b2e",
                                    font_family="Courgette",
                                    text_align="center"
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                        ft.Column(
                            controls=[
                                ft.Divider(height=600, color="transparent"),
                                ft.Text(
                                    "Lihat undangan",
                                    size=12,
                                    text_align="center",
                                    weight=ft.FontWeight.BOLD,
                                    color="#303923",
                                    font_family="Poppins"
                                ),

                                ft.Icon(
                                    ft.icons.ARROW_DROP_DOWN,
                                    color="black",
                                    size=40
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                    ]
                ),

                ft.Divider(height=0, color="transparent"),

                # Information Section
                ft.Stack(
                    alignment=ft.alignment.center,
                    controls=[
                        ft.Container(
                            expand=True,
                            width=page.width,
                            height=page.height,
                            bgcolor="white",
                        ),

                        ft.Image(
                            expand=True,
                            src="bg_info_page.png",
                            fit=ft.ImageFit.COVER,
                            width=450,
                            height=page.height,
                            border_radius=20
                        ),

                        ft.Image(
                            expand=True,
                            src="bg_putih.png",
                            fit=ft.ImageFit.COVER,
                            width=300,
                            height=450,
                            border_radius=50
                        ),

                        ft.Column(
                            controls=[
                                ft.Text(
                                    "Save The Date",
                                    size=20,
                                    weight=ft.FontWeight.BOLD,
                                    text_align="center",
                                    color="#3f4b2e",
                                    font_family="Courgette"
                                ),

                                ft.Text(
                                    "Rabu-Kamis, 25-26 Desember 2024",
                                    size=12,
                                    weight=ft.FontWeight.BOLD,
                                    text_align="center",
                                    color="#303923",
                                    font_family="Poppins"
                                ),

                                ft.Text(
                                    "Tempat :\nKampungbaru,\nDesa Tamansari Rt 02 Rw 05,\nKec. Karangmoncol,\nKab. Purbalingga.",
                                    size=12,
                                    text_align="center",
                                    color="#303923",
                                    font_family="Poppins"
                                ),

                                ft.ElevatedButton(
                                    "Lihat Lokasi",
                                    on_click=open_google_maps,
                                    color="white",
                                    bgcolor="#3f4b2e",
                                    icon=ft.icons.SHARE_LOCATION_ROUNDED,
                                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5000))
                                ),

                                ft.Text(
                                    "Merupakan suatu kehormatan dan\nkebahagiaan bagi kami apabila\nBapak/Ibu/Saudara/i berkenan hadir",
                                    size=12,
                                    text_align="center",
                                    color="#303923",
                                    font_family="Poppins"
                                ),

                                ft.Text("Wassalamu'alaikum Wr. Wb.",
                                    size=20,
                                    text_align="center",
                                    weight=ft.FontWeight.BOLD,
                                    color="#3f4b2e",
                                    font_family="GreatVibes",
                                ),

                                ft.Text(
                                    "Hormat kami:\nIsnanto, S.Pd.I., M.Pd.\nAlfi Khasanah, S.Pd.I",
                                    size=12,
                                    text_align="center",
                                    color="#303923",
                                    font_family="Poppins"
                                )
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                    ]
                )
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

ft.app(target=main, view=ft.AppView.WEB_BROWSER, assets_dir="assets")
