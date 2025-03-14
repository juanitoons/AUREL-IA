import flet as ft
import random
import os
import json

ARCHIVO_NUMERO = "numero_guardado.txt"

# Función para guardar el número
def guardar_numero(numero):
    numeros = leer_numeros()  # Lee la lista actual de números
    numeros.append(numero)  # Agrega el nuevo número
    with open(ARCHIVO_NUMERO, "w") as archivo:
        json.dump(numeros, archivo)  # Guarda la lista en formato JSON

# Función para leer la lista de números guardados
def leer_numeros():
    if os.path.exists(ARCHIVO_NUMERO):
        with open(ARCHIVO_NUMERO, "r") as archivo:
            return json.load(archivo)  # Lee la lista desde el archivo
    return []  # Si el archivo no existe, retorna una lista vacía

# Función para obtener el último número guardado
def obtener_ultimo_numero():
    numeros = leer_numeros()
    return str(numeros[-1]) if numeros else "00"  # Retorna el último número como cadena o "00" si no hay números

def main(page: ft.Page):
    page.title = "AUREL-IA"
    page.bgcolor = "#734A91"
    page.padding = 20

    numero_aleatorio = random.randint(10, 99)  # Número de 2 dígitos
    numero_guardado = obtener_ultimo_numero()  # Obtiene el último número guardado como cadena

    print(f"Número guardado: {numero_guardado}")  # Depuración

    def cerrar_app(e):
        guardar_numero(numero_aleatorio)  # Guarda el número aleatorio antes de cerrar
        page.window.destroy()

    # Declarar input_numero y resultado_texto como variables globales
    input_numero = ft.TextField(hint_text="Número", max_length=2)
    resultado_texto = ft.Text("")

    def desbloquear_app(e):
        if len(input_numero.value) != 2 or not input_numero.value.isdigit():
            resultado_texto.value = "Ingresa un número de 2 dígitos."
        elif input_numero.value == numero_guardado:  # Compara como cadenas
            guardar_numero("00")  # Guarda "00" para desbloquear
            ir_a_vista("/")
        else:
            resultado_texto.value = f"Número incorrecto, intenta de nuevo. (Guardado: {numero_guardado})"
        page.update()  # Actualiza la página

    # Pantalla de bloqueo
    def vista_bloqueo():
        return ft.View(
            route="/bloqueo",
            controls=[
                ft.AppBar(title=ft.Text("Pantalla de bloqueo"), bgcolor=ft.colors.PURPLE_300,center_title=True),
                ft.Container(
                    content=ft.Column([
                        ft.Row([ft.Image(src=("src/assets/flor2.png"), width=250, height=250)], alignment=ft.MainAxisAlignment.CENTER),
                        ft.Text("Introduce el número guardado para desbloquear:",size=20),
                        input_numero,  # Usamos la variable global
                        ft.Row([ft.ElevatedButton("Desbloquear", on_click=desbloquear_app)],alignment=ft.MainAxisAlignment.CENTER),
                        resultado_texto  # Usamos la variable global
                    ], alignment=ft.MainAxisAlignment.CENTER),
                    alignment=ft.alignment.center,
                    expand=True
                )
            ],
            bgcolor="#734A91"  # Color de fondo de la vista
        )

    # Función para navegar entre vistas
    def ir_a_vista(ruta):
        page.route = ruta
        page.update()

    def regresar(_):
        page.route = "/"
        page.update()

    # Vista principal (Menú)
    def vista_menu():
        return ft.View(
            route="/",
            controls=[
                ft.AppBar(
                    title=ft.Text("AUREL-IA", color=ft.colors.WHITE),
                    bgcolor=ft.colors.PURPLE_300,
                    center_title=True
                ),
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Row([ft.Image(src=("src/assets/flor2.png"), width=250, height=250)], alignment=ft.MainAxisAlignment.CENTER),
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
                                                content=ft.Icon(ft.icons.EDIT_DOCUMENT, color=ft.colors.BLACK, size=60),
                                                width=90, height=90, bgcolor=ft.colors.WHITE, border_radius=20,
                                                alignment=ft.alignment.center,
                                                on_click=lambda _: ir_a_vista("/denuncia")
                                            ),
                                            ft.Text("Denuncia", text_align=ft.TextAlign.CENTER),
                                            ft.Container(
                                                content=ft.Icon(ft.icons.WARNING_AMBER_ROUNDED, color=ft.colors.BLACK, size=60),
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
                            ),
                            ft.Row([ft.Checkbox(label="Aceptar termino de privacidad", value=False)], alignment=ft.MainAxisAlignment.CENTER, height=100)
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                    alignment=ft.alignment.center,
                    expand=True
                )
            ],
            bgcolor="#734A91"  # Color de fondo de la vista
        )
    
    RESPUESTAS_PREDETERMINADAS = [
    "Tienes derecho a recibir asesoría legal gratuita en casos de violencia.",
    "Puedes solicitar medidas de protección inmediatas si te encuentras en peligro.",
    "Es importante que sepas que nadie puede obligarte a quedarte en una situación de riesgo.",
    "Si te sientes insegura, acude a un centro de atención especializado.",
    "Recuerda que puedes denunciar cualquier acto de violencia ante las autoridades.",
    ]

    RESPUESTAS_PREDETERMINADAS2 = [ 
    "Es importante que recopiles cualquier evidencia que pueda respaldar tu denuncia, como mensajes, fotos o testigos.",
    "¿En que fecha y a que hora sucedieron los hechos?",
    "¿Quien realizo los hechos?",
    "Hay algun partido politico involucrado",
    "¿En donde sucedieron los hechos?",
    "Puedes especificar la ubicacion",
    "¿Como sucedieron los hechos?",
    "¿Quieres hacer el documento de denuncia?"
    ]



    # Índice para controlar el recorrido de la lista de respuestas
    indice_respuesta = 0
    indice_respuesta2 = 0

    # Vista "Conoce tus derechos"
    def vista_conoce_derechos():
        chat_mensajes = ft.ListView(expand=True, spacing=10, auto_scroll=True)

        def enviar_mensaje(e):
            nonlocal indice_respuesta  # Permite que el índice se mantenga en cada llamada

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

                # Simular respuesta del chatbot recorriendo la lista
                respuesta_chatbot = RESPUESTAS_PREDETERMINADAS[indice_respuesta]
                indice_respuesta = (indice_respuesta + 1) % len(RESPUESTAS_PREDETERMINADAS)

                chat_mensajes.controls.append(
                    ft.Column(
                        [
                            ft.Row([
                                ft.Image(src="src/assets/flor2.png", width=30, height=30),
                                ft.Text("AUREL-IA", size=16, color=ft.colors.WHITE)
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

                input_mensaje.value = ""
                input_mensaje.update()
                chat_mensajes.update()

        # Mensaje inicial del chatbot
        chat_mensajes.controls.append(
            ft.Column(
                [
                    ft.Row([
                        ft.Image(src="src/assets/flor2.png", width=30, height=30),
                        ft.Text("AUREL-IA", size=16, color=ft.colors.WHITE)
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

        input_mensaje = ft.TextField(hint_text="Escribe tu mensaje...", bgcolor=ft.colors.WHITE, color=ft.colors.BLACK, border_radius=30, expand=True)
        boton_enviar = ft.IconButton(ft.icons.SEND, bgcolor=ft.colors.PURPLE_300, icon_color=ft.colors.WHITE, on_click=enviar_mensaje)

        return ft.View(
            route="/conoce_tus_derechos",
            controls=[
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
                                expand=True,
                                padding=10,
                                border_radius=10
                            ),
                            ft.Container(
                                content=ft.Row([input_mensaje, boton_enviar, ft.IconButton(icon=ft.icons.WARNING_AMBER_ROUNDED, icon_color=ft.colors.BLACK, bgcolor=ft.colors.RED_400, on_click=cerrar_app)], 
                                alignment=ft.MainAxisAlignment.CENTER),
                                padding=10
                            )
                        ],
                        expand=True
                    )
                )
            ],
            bgcolor="#734A91"  # Color de fondo de la vista
        )

    # Vista "Instituciones de apoyo"
    def vista_instituciones():
        return ft.View(
            route="/instituciones",
            controls=[
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
            ],
            bgcolor="#734A91"  # Color de fondo de la vista
        )

    # Vista "Denuncia"
    def vista_denuncia():
        chat_mensajes = ft.ListView(expand=True, spacing=10, auto_scroll=True)

        def enviar_mensaje(e):
            nonlocal indice_respuesta2  

            if input_mensaje.value.strip():
                chat_mensajes.controls.append(
                    ft.Container(
                        content=ft.Text(input_mensaje.value, size=16, color=ft.colors.WHITE),
                        bgcolor=ft.colors.BLUE_500,
                        padding=10,
                        border_radius=30,
                        alignment=ft.alignment.center_right
                    )
                )

                respuesta_chatbot = RESPUESTAS_PREDETERMINADAS2[indice_respuesta2]

                # Si es la respuesta 7, se crea un contenedor especial para el documento
                if indice_respuesta2 == 7:
                    chat_mensajes.controls.append(
                        ft.Container(
                            content=ft.Text(
                                spans=[
                                    ft.TextSpan("📄 Aquí está tu ", style={"color": ft.colors.BLACK, "size": 16}),
                                    ft.TextSpan("documento de denuncia.pdf", 
                                                style={
                                                    "decoration": ft.TextDecoration.UNDERLINE, 
                                                    "font_weight": ft.FontWeight.BOLD,
                                                    "size":16
                                                })
                                ],
                            ),
                            bgcolor=ft.colors.GREEN,
                            padding=10,
                            border_radius=30,
                            alignment=ft.alignment.center_left,
                            on_click=lambda _: ir_a_vista("/denuncia_Doc")
                        )
                    )
                else:
                    chat_mensajes.controls.append(
                        ft.Column(
                            [
                                ft.Row([
                                    ft.Image(src="src/assets/flor2.png", width=30, height=30),
                                    ft.Text("AUREL-IA", size=16, color=ft.colors.WHITE)
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

                indice_respuesta2 = (indice_respuesta2 + 1) % len(RESPUESTAS_PREDETERMINADAS2)

                input_mensaje.value = ""
                input_mensaje.update()
                chat_mensajes.update()

        # Mensaje inicial del chatbot
        chat_mensajes.controls.append(
            ft.Column(
                [
                    ft.Row([
                        ft.Image(src="src/assets/flor2.png", width=30, height=30),
                        ft.Text("AUREL-IA", size=16, color=ft.colors.WHITE)
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

        input_mensaje = ft.TextField(hint_text="Escribe tu mensaje...", bgcolor=ft.colors.WHITE,color=ft.colors.BLACK, border_radius=30, expand=True)
        boton_enviar = ft.IconButton(ft.icons.SEND,bgcolor=ft.colors.PURPLE_300,icon_color=ft.colors.WHITE, on_click=enviar_mensaje)

        return ft.View(
            route="/denuncia",
            controls=[
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
                            expand=True,
                            padding=10,
                            border_radius=10
                        ),
                        ft.Container(
                            content=ft.Row([input_mensaje, boton_enviar, ft.IconButton(icon=ft.icons.WARNING_AMBER_ROUNDED, icon_color=ft.colors.BLACK, bgcolor=ft.colors.RED_400, on_click=cerrar_app)], 
                            alignment=ft.MainAxisAlignment.CENTER),
                            padding=10
                        )
                    ],
                    expand=True
                )
            )
            ],
            bgcolor="#734A91"  # Color de fondo de la vista
        )

    # Vista "Denuncia Documento"
    def vista_denuncia_doc():
        def cambiar_estado(e, contenedor, texto):
            contenedor.bgcolor = ft.colors.BLUE  # Cambia el color a azul
            texto.value = "Descarga completada"  # Cambia el texto
            e.page.update()
        
        texto_descarga = ft.Text("Descargar", color=ft.colors.WHITE, size=16)
        contenedor_descarga = ft.Container(
            content=texto_descarga,
            bgcolor=ft.colors.GREEN,
            padding=10,
            border_radius=30,
            on_click=lambda e: cambiar_estado(e, contenedor_descarga, texto_descarga)
        )

        return ft.View(
            route="/denuncia_Doc",
            controls=[
                ft.AppBar(
                ft.IconButton(ft.Icons.ARROW_BACK_ROUNDED, on_click=regresar),
                title=ft.Text("Descargar de documento"),
                bgcolor=ft.colors.PURPLE_300
            ),
            ft.Container(
                content=ft.Column(
                    [
                        ft.Container(
                            content=ft.Row(
                                [ft.Image(src=("src/assets/Doc.jpg"), width=250, height=150)],
                                alignment=ft.MainAxisAlignment.CENTER
                            ),
                            bgcolor=ft.colors.PURPLE_300,
                            padding=15,
                            border_radius=20
                        ),
                        contenedor_descarga  # Contenedor de descarga
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                ),
                expand=True,
                alignment=ft.alignment.center
            )
            ],
            bgcolor="#734A91"  # Color de fondo de la vista
        )

    # Función para manejar cambios de ruta
    def route_change(e):
        page.views.clear()

        if numero_guardado == "00" or not os.path.exists(ARCHIVO_NUMERO):
            page.views.append(vista_menu())
        else:
            page.views.append(vista_bloqueo())

        if page.route == "/":
            page.views.append(vista_menu())
        elif page.route == "/conoce_tus_derechos":
            page.views.append(vista_conoce_derechos())
        elif page.route == "/instituciones":
            page.views.append(vista_instituciones())
        elif page.route == "/denuncia":
            page.views.append(vista_denuncia())
        elif page.route == "/denuncia_Doc":
            page.views.append(vista_denuncia_doc())

        page.update()

    # Configuración inicial
    page.on_route_change = route_change
    page.route = "/bloqueo" if numero_guardado != "00" and os.path.exists(ARCHIVO_NUMERO) else "/"
    route_change(None)

ft.app(target=main)