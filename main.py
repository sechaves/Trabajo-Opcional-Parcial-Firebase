from viewmodel.biblioteca import BibliotecaViewModel
import presentation.menu as menu
import ui.input_output as ui

def run():
    """
    Función principal que inicia y controla el flujo de la aplicación.
    """
    view_model = BibliotecaViewModel()

    while True:
        menu.mostrar_menu_principal()
        opcion = ui.obtener_opcion()

        if opcion == '1':
            titulo, autor, categoria, isbn = ui.obtener_datos_libro()
            mensaje = view_model.agregar_libro(titulo, autor, categoria, isbn)
            ui.mostrar_mensaje(mensaje)
        
        elif opcion == '2':
            lista_libros = view_model.listar_libros()
            ui.mostrar_lista_libros(lista_libros)

        elif opcion == '3':
            nombre, doc, programa = ui.obtener_datos_usuario()
            mensaje = view_model.registrar_usuario(nombre, doc, programa)
            ui.mostrar_mensaje(mensaje)
            
        elif opcion =='4':
            listar_usuario = view_model.listar_usuarios()
            ui.mostrar_lista_usuarios(listar_usuario)
            
        elif opcion == '5':
            isbn = ui.obtener_isbn_libro()
            mensaje = view_model.eliminar_libro(isbn)
            ui.mostrar_mensaje(mensaje)

        elif opcion == '6': 
            documento = ui.obtener_documento_usuario()
            mensaje = view_model.eliminar_usuario(documento)
            ui.mostrar_mensaje(mensaje)

        elif opcion == '7':
            ui.mostrar_mensaje("Byeee")
            break
        
        else:
            ui.mostrar_mensaje("Opción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    run()