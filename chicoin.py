#Importacion de libreria
import tkinter as tk
import sqlite3
from tkinter import messagebox
'''

------PALETA COLOR MORADO-------
#5A51A0(color morado mas fuerte)
#7368B8(morado mas bajito)
#8B7FD0(aun mas bajito)
#A496E7(mas bajito que el anterior)
#BCADFF(el mas bajito de todos)


'''





#ventana login


#variable fuente
font_title = ("Karmatic Arcade", 16)
font_title_log = ("Blackside DEMO Regular", 14)

def crear_cuenta():
    ventana_crear_cuenta = tk.Tk()
    ventana_crear_cuenta.title("Crea tu cuenta")
    ventana_crear_cuenta.config(bg="#5A51A0")
    
    label_titulo_crear = tk.Label(ventana_crear_cuenta, text="Crea tu Chicoincuenta!", font=font_title, bg="#5A51A0", fg="#FFFFFF")
    label_titulo_crear.grid(row=0, column=2, padx=10, pady=10)
    
    label_crear_user = tk.Label(ventana_crear_cuenta, text="Crea tu usuario:", fg="#FFFFFF", bg="#5A51A0", font=font_title_log)
    label_crear_user.grid(row=1, column=2, padx=10, pady=5)
    
    caja_texto_crear_usuario = tk.Entry(ventana_crear_cuenta, bg="#BCADFF", relief="ridge", fg="#FFFFFF")
    caja_texto_crear_usuario.grid(row=2, column=2, padx=10, pady=5)
    
    label_crear_correo = tk.Label(ventana_crear_cuenta, text="Ingresa un correo", fg="#FFFFFF", bg="#5A51A0", font=font_title_log)
    label_crear_correo.grid(row=3, column=2, padx=10, pady=5)
    
    caja_texto_crear_correo = tk.Entry(ventana_crear_cuenta, bg="#BCADFF", relief="ridge", fg="#FFFFFF")
    caja_texto_crear_correo.grid(row=4, column=2, padx=10, pady=5)
    
    label_crear_contraseña = tk.Label(ventana_crear_cuenta, text="Crea tu contraseña:", fg="#FFFFFF", bg="#5A51A0", font=font_title_log)
    label_crear_contraseña.grid(row=5, column=2, padx=10, pady=5)
    
    caja_texto_crear_contraseña = tk.Entry(ventana_crear_cuenta, bg="#BCADFF", relief="ridge", fg="#FFFFFF", show="*")
    caja_texto_crear_contraseña.grid(row=6, column=2, padx=10, pady=5)
    
    label_confirmar_registro = tk.Label(ventana_crear_cuenta, text="Confirma tu cuenta en el siguiente boton:", fg="#FFFFFF", bg="#5A51A0", font=font_title_log)
    label_confirmar_registro.grid(row=7, column=2, padx=10, pady=5)
    
   
    
    def registrar_usuario():
        #Obtener los valores de los campos
        usuario = caja_texto_crear_usuario.get()
        correo = caja_texto_crear_correo.get()
        contraseña = caja_texto_crear_contraseña.get()
        try:
            #Insertar el nuevo usuario en la BD
            conexion = sqlite3.connect("ChiCoin")
            cursor = conexion.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS UsuariosChi (USUARIO TEXT PRIMARY KEY, CORREO TEXT, PASSWORD TEXT)")
            cursor.execute("INSERT INTO UsuariosChi VALUES (?,?,?)", (usuario, correo, contraseña))
            conexion.commit()
            messagebox.showinfo("Conexion con BD con exito","Usuario Registrado con exito")
        except:
            messagebox.showinfo("Error","Error en la conexion con la base de datos")
            
    boton_confirmar = tk.Button(ventana_crear_cuenta,text="Crea cuenta", bg="#8B7FD0", relief="groove", fg="#FFFFFF", command=registrar_usuario)
    boton_confirmar.grid(row=8, column=2, padx=10, pady=10)

def iniciosesion():
    usuarioinicio = caja_user.get()
    try:
       conexion = sqlite3.connect("ChiCoin")
       cursor = conexion.cursor()
       cursor.execute("SELECT USUARIO, CORREO, PASSWORD FROM UsuariosChi WHERE USUARIO = ?",(usuarioinicio,))
       contrasenas = cursor.fetchall()
       contrseñaingresada=caja_contraseña.get()
       for contrasena in contrasenas:
          contraseñareal=(contrasena[2])
          conexion.commit()
    except:
        messagebox.showwarning("¡Atención!", "Error en la Búsqueda")
    if contrseñaingresada==contraseñareal:
        messagebox.showwarning("Acceso concedido","Contraseña correcta")
        ventana_mina = tk.Toplevel(ventana1)
        ventana_mina.title("Hola bienvenido de nuevo")
        ventana_mina.geometry("800x800")
        ventana_mina.config(bg="#5A51A0")
        ventana_mina.geometry("+{}+{}".format((ventana_mina.winfo_screenwidth() - ventana_mina.winfo_reqwidth()) // 2, (ventana_mina.winfo_screenheight() - ventana_mina.winfo_reqheight()) // 3))
        ruta_imagen = "C:\\Users\\Rodrigo Oropeza\\Desktop\\RecursosPython\\Dodge.png"
        imagen = PhotoImage(file=ruta_imagen)
        etiqueta_imagen = tk.Label(ventana_mina, image=imagen)
        etiqueta_imagen.image = imagen
        etiqueta_imagen.pack()

    elif contrseñaingresada==None:
        messagebox.showerror("Error","Campo de contraseña vacio")
    else:
        messagebox.showwarning("Acceso denegado","Contraseña incorrecta")

ventana_login = tk.Tk()
ventana_login.title("ChiCoin")
ventana_login.config(bg="#5A51A0")





#label bievenida
label_bienvenida = tk.Label(ventana_login, text="Bienvenido a ChiCoin!", font=font_title, bg="#5A51A0", fg="#FFFFFF")
label_bienvenida.grid(row=1, column=2, padx=10, pady=10)

label_usuario = tk.Label(ventana_login,text="Usuario", fg="#FFFFFF", bg="#5A51A0", font=font_title_log)
label_usuario.grid(row=2, column=2, padx=10, pady=5)

caja_user = tk.Entry(ventana_login, bg="#BCADFF", relief="ridge", fg="#FFFFFF")
caja_user.grid(row=3, column=2, padx=10, pady=5)

label_pass = tk.Label(ventana_login, text="Contraseña", bg="#5A51A0", fg="#FFFFFF", font=font_title_log,)
label_pass.grid(row=4, column=2, padx=10, pady=5 )

caja_pass = tk.Entry(ventana_login, bg="#BCADFF", relief="ridge", show="*")
caja_pass.grid(row=5, column=2, padx=10, pady=5)

boton_iniciar_sesion = tk.Button(ventana_login, text="Iniciar Sesion", bg="#8B7FD0", relief="groove", command=iniciosesion, fg="#FFFFFF")
boton_iniciar_sesion.grid(row=6, column=2, padx=10, pady=5)

label_crear_cuenta = tk.Label(ventana_login,text="¿No tienes cuenta? Crea una ", fg="#FFFFFF", bg="#5A51A0", font=font_title_log)
label_crear_cuenta.grid(row=7, column=2, padx=10, pady=5)

boton_crear_cuenta = tk.Button(ventana_login, text="Crear cuenta", bg="#8B7FD0", relief="groove", command=crear_cuenta, fg="#FFFFFF")
boton_crear_cuenta.grid(row=8, column=2, padx=10, pady=5)





ventana_login.mainloop()