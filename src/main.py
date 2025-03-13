import flet as ft
import random

def main(page: ft.Page):
    page.title = "AUREL-IA"
    page.bgcolor = "#734A91"
    page.padding = 20  

    numero_aleatorio = random.randint(10, 99)

    # Función para navegar entre vistas
    def ir_a_vista(ruta):
        page.route = ruta
        page.update()

    def regresar(_):
        page.route = "/"
        page.update()

    page.window.prevent_close = True

    def cerrar_app(e):
        page.window.destroy()

    # Vista principal (Menú)
    def vista_menu():
        return [
            ft.AppBar(
                title=ft.Text("AUREL-IA", color=ft.colors.WHITE),
                bgcolor=ft.colors.PURPLE_300
            ),
            ft.Container(
                content=ft.Column(
                    [
                        ft.Row([ft.Image(src=("src/assets/flor2.png"), width=250, height=250)],alignment=ft.MainAxisAlignment.CENTER),
                        ft.Row(
                            [
                                ft.Column(
                                    [
                                        ft.Container(
                                            content=ft.Icon(ft.icons.QUESTION_MARK_SHARP, color=ft.colors.BLACK, size=60),
                                            width=90, height=90, bgcolor=ft.colors.WHITE, border_radius=20,
                                            alignment=ft.alignment.center,
                                            on_click=lambda _: ir_a_vista("/conoce_tus_derechos")
                                        ),
                                        ft.Text("Conoce tus derechos", text_align=ft.TextAlign.CENTER),
                                        ft.Container(
                                            content=ft.Icon(ft.icons.HOME_OUTLINED, color=ft.colors.BLACK, size=60),
                                            width=90, height=90, bgcolor=ft.colors.WHITE, border_radius=20,
                                            alignment=ft.alignment.center,
                                            on_click=lambda _: ir_a_vista("/instituciones")
                                        ),
                                        ft.Text("Instituciones de apoyo", text_align=ft.TextAlign.CENTER)
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER
                                ),
                                ft.Column(
                                    [
                                        ft.Container(
                                            content=ft.Icon(ft.icons.WARNING_AMBER_ROUNDED, color=ft.colors.BLACK, size=60),
                                            width=90, height=90, bgcolor=ft.colors.WHITE, border_radius=20,
                                            alignment=ft.alignment.center,
                                            on_click=lambda _: ir_a_vista("/denuncia")
                                        ),
                                        ft.Text("Denuncia", text_align=ft.TextAlign.CENTER),
                                        ft.Container(
                                            content=ft.Icon(ft.icons.EMERGENCY, color=ft.colors.BLACK, size=60),
                                            width=90, height=90, bgcolor=ft.colors.RED_400, border_radius=20,
                                            alignment=ft.alignment.center,
                                            on_click=cerrar_app
                                        ),
                                        ft.Text("Salida rápida", text_align=ft.TextAlign.CENTER)
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER
                                )
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=30
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                alignment=ft.alignment.center,
                expand=True  
            )
        ]

    # Vistas individuales
    def vista_conoce_derechos():
        chat_mensajes = ft.ListView(expand=True, spacing=10, auto_scroll=True)  # Lista con desplazamiento automático

        def enviar_mensaje(e):
            if input_mensaje.value.strip():
                # Agregar mensaje del usuario
                chat_mensajes.controls.append(
                    ft.Container(
                        content=ft.Text(input_mensaje.value, size=16, color=ft.colors.WHITE),
                        bgcolor=ft.colors.BLUE_500,
                        padding=10,
                        border_radius=30,
                        alignment=ft.alignment.center_right
                    )
                )

                # Simular respuesta del chatbot
                respuesta_chatbot = f"{input_mensaje.value[::-1]}"  # Solo invierte el texto como ejemplo
                chat_mensajes.controls.append(
                    ft.Column(
                        [
                            ft.Row([ft.Image(src="src/assets/flor2.png", width=30, height=30),
                                    ft.Text("AUREL-IA",size=16,color=ft.colors.WHITE)
                                    ]),
                            ft.Container(
                                content=ft.Text(respuesta_chatbot, size=16, color=ft.colors.BLACK),
                                bgcolor=ft.colors.GREY_300,
                                padding=10,
                                border_radius=30,
                                alignment=ft.alignment.center_left
                            )
                        ]
                    )
                )

                input_mensaje.value = ""  # Limpiar input
                input_mensaje.update()
                chat_mensajes.update()  # Actualizar vista

        # Mensaje inicial del chatbot
        chat_mensajes.controls.append(
            ft.Column(
                [
                    ft.Row([ft.Image(src="src/assets/flor2.png", width=30, height=30),
                                    ft.Text("AUREL-IA",size=16,color=ft.colors.WHITE)
                                    ]),
                    ft.Container(
                        content=ft.Text("Hola, ¿en qué te puedo ayudar?", size=16, color=ft.colors.BLACK),
                        bgcolor=ft.colors.GREY_300,
                        padding=10,
                        border_radius=30,
                        alignment=ft.alignment.center_left
                    )
                ]
            )
        )

        input_mensaje = ft.TextField(hint_text="Escribe tu mensaje...",bgcolor=ft.colors.WHITE ,border_radius=30,expand=True)
        boton_enviar = ft.IconButton(ft.icons.SEND, on_click=enviar_mensaje)

        return [
            ft.AppBar(
                leading=ft.IconButton(ft.icons.ARROW_BACK, on_click=regresar),
                title=ft.Text(f"En caso de bloqueo recuerda los siguientes números:{numero_aleatorio}", size=20, color=ft.colors.WHITE),
                bgcolor=ft.colors.PURPLE_300
            ),
            ft.Container(
                expand=True,
                content=ft.Column(
                    [
                        ft.Container(
                            content=chat_mensajes,
                            expand=True,  # Se ajusta automáticamente
                            padding=10,
                            border_radius=10
                        ),
                        ft.Container(  # Input siempre visible
                            content=ft.Row([input_mensaje, boton_enviar,ft.IconButton(icon=ft.icons.EMERGENCY,icon_color=ft.colors.BLACK,bgcolor=ft.colors.RED_400,on_click=cerrar_app)], alignment=ft.MainAxisAlignment.CENTER),
                            padding=10
                        )
                    ],
                    expand=True
                )
            )
        ]


    def vista_instituciones():
        return [
            ft.AppBar(ft.IconButton(ft.Icons.ARROW_BACK_ROUNDED,on_click=regresar),title=ft.Text("Instituciones de apoyo"), bgcolor=ft.colors.PURPLE_300),
            ft.Container(
                content=ft.Column(
                    [
                        ft.Container(content=ft.Row(
                            [
                                ft.Container(
                                    content=ft.Column([ft.Text("A")],alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER),border_radius=60,bgcolor=ft.colors.BLUE,width=30,height=30
                                    ),
                                ft.Text("Delegacion\nAv Cortez 01",color=ft.colors.BLACK)
                                ]),
                                bgcolor=ft.colors.WHITE,
                                padding=15,
                                border_radius=20
                            ),
                        ft.Container(content=ft.Row(
                            [
                                ft.Container(
                                    content=ft.Column([ft.Text("A")],alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER),border_radius=60,bgcolor=ft.colors.BLUE,width=30,height=30
                                    ),
                                ft.Text("Centro de Atencion\nAv Cortez 01",color=ft.colors.BLACK)
                                ]),
                                bgcolor=ft.colors.WHITE,
                                padding=15,
                                border_radius=20
                            ),
                        ft.Container(content=ft.Row(
                            [
                                ft.Container(
                                    content=ft.Column([ft.Text("A")],alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER),border_radius=60,bgcolor=ft.colors.BLUE,width=30,height=30
                                    ),
                                ft.Text("Atención Psicológica\nAv Cortez 01",color=ft.colors.BLACK)
                                ]),
                                bgcolor=ft.colors.WHITE,
                                padding=15,
                                border_radius=20
                            )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                ),
                alignment=ft.alignment.center,
                expand=True
            )
        ]

    def vista_denuncia():
        chat_mensajes = ft.ListView(expand=True, spacing=10, auto_scroll=True)  # Lista con desplazamiento automático

        def enviar_mensaje(e):
            if input_mensaje.value.strip():
                # Agregar mensaje del usuario
                chat_mensajes.controls.append(
                    ft.Container(
                        content=ft.Text(input_mensaje.value, size=16, color=ft.colors.WHITE),
                        bgcolor=ft.colors.BLUE_500,
                        padding=10,
                        border_radius=30,
                        alignment=ft.alignment.center_right
                    )
                )

                # Simular respuesta del chatbot
                respuesta_chatbot = f"{input_mensaje.value[::-1]}"  # Solo invierte el texto como ejemplo
                chat_mensajes.controls.append(
                    ft.Column(
                        [
                            ft.Row([ft.Image(src="src/assets/flor2.png", width=30, height=30),
                                    ft.Text("AUREL-IA",size=16,color=ft.colors.WHITE)
                                    ]),
                            ft.Container(
                                content=ft.Text(respuesta_chatbot, size=16, color=ft.colors.BLACK),
                                bgcolor=ft.colors.GREY_300,
                                padding=10,
                                border_radius=30,
                                alignment=ft.alignment.center_left
                            )
                        ]
                    )
                )

                input_mensaje.value = ""  # Limpiar input
                input_mensaje.update()
                chat_mensajes.update()  # Actualizar vista

        # Mensaje inicial del chatbot
        chat_mensajes.controls.append(
            ft.Column(
                [
                    ft.Row([ft.Image(src="src/assets/flor2.png", width=30, height=30),
                                    ft.Text("AUREL-IA",size=16,color=ft.colors.WHITE)
                                    ]),
                    ft.Container(
                        content=ft.Text("¿Te encuentras en peligro inmediato?", size=16, color=ft.colors.BLACK),
                        bgcolor=ft.colors.GREY_300,
                        padding=10,
                        border_radius=30,
                        alignment=ft.alignment.center_left
                    )
                ]
            )
        )

        input_mensaje = ft.TextField(hint_text="Escribe tu mensaje...",bgcolor=ft.colors.WHITE ,border_radius=30,expand=True)
        boton_enviar = ft.IconButton(ft.icons.SEND, on_click=enviar_mensaje)

        return [
            ft.AppBar(
                leading=ft.IconButton(ft.icons.ARROW_BACK, on_click=regresar),
                title=ft.Text(f"En caso de bloqueo recuerda los siguientes números:{numero_aleatorio}", size=20, color=ft.colors.WHITE),
                bgcolor=ft.colors.PURPLE_300
            ),
            ft.Container(
                expand=True,
                content=ft.Column(
                    [
                        ft.Container(
                            content=chat_mensajes,
                            expand=True,  # Se ajusta automáticamente
                            padding=10,
                            border_radius=10
                        ),
                        ft.Container(  # Input siempre visible
                            content=ft.Row([input_mensaje, boton_enviar,ft.IconButton(icon=ft.icons.EMERGENCY,icon_color=ft.colors.BLACK,bgcolor=ft.colors.RED_400,on_click=cerrar_app)], alignment=ft.MainAxisAlignment.CENTER),
                            padding=10
                        )
                    ],
                    expand=True
                )
            )
        ]


    # Función para manejar cambios de ruta
    def route_change(e):
        page.views.clear()
        
        if page.route == "/":
            page.views.append(ft.View(route=page.route, bgcolor=page.bgcolor, controls=vista_menu()))
        elif page.route == "/conoce_tus_derechos":
            page.views.append(ft.View(route=page.route, bgcolor=page.bgcolor, controls=vista_conoce_derechos()))
        elif page.route == "/instituciones":
            page.views.append(ft.View(route=page.route, bgcolor=page.bgcolor, controls=vista_instituciones()))
        elif page.route == "/denuncia":
            page.views.append(ft.View(route=page.route, bgcolor=page.bgcolor, controls=vista_denuncia()))
        
        page.update()

    # Configuración inicial
    page.on_route_change = route_change
    page.route = "/"  
    route_change(None)  

ft.app(target=main)

