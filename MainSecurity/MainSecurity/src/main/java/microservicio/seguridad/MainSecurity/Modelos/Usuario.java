package microservicio.seguridad.MainSecurity.Modelos;

import lombok.Data;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.DBRef;
import org.springframework.data.mongodb.core.mapping.Document;

// Decorador, Para definir que esta clase sera almacenada en la base de datos.
@Data
@Document()

// Clase con atributos, creacion de tabla en mongo
public class Usuario {
    @Id                     //Campo unico del documento
    private String _id;
    private String seudonimo;
    private String correo;
    private String contrasena;

    @DBRef
    private Rol rol;

    // Constructor
    public Usuario(String seudonimo, String correo, String contrasena) {
        this.seudonimo = seudonimo;
        this.correo = correo;
        this.contrasena = contrasena;
    }

    // Getter y Setter de la clase.
    // nos permiten leer y escribir los valores de nuestras variables privadas desde fuera de la clase donde fueron creadas.

    public String get_id() {
        return _id;
    }

    public String getSeudonimo() {
        return seudonimo;
    }

    public void setSeudonimo(String seudonimo) {
        this.seudonimo = seudonimo;
    }

    public String getCorreo() {
        return correo;
    }

    public void setCorreo(String correo) {
        this.correo = correo;
    }

    public String getContrasena() {
        return contrasena;
    }

    public void setContrasena(String contrasena) {
        this.contrasena = contrasena;
    }
}



