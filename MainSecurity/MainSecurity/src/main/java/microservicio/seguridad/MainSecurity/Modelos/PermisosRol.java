package microservicio.seguridad.MainSecurity.Modelos;

import lombok.Data;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.DBRef;
import org.springframework.data.mongodb.core.mapping.Document;

// Decoradores, Para definir que esta clase sera almacenada en la base de datos.
@Data
@Document

// Clase con atributos, creacion de tabla en mongo
public class PermisosRol {
    @Id
    private String _id; //Campo unico del documento

    @DBRef             // Relacion
    private Rol rol;

    @DBRef            // Relacion
    private Permiso permiso;

    // Constructor
    public PermisosRol(){

    }
    // Getter y Setter de la clase.
    // nos permiten leer y escribir los valores de nuestras variables privadas desde fuera de la clase donde fueron creadas.
    public String get_id(){
        return _id;
    }

    public Rol getRol() {
        return rol;
    }

    public void setRol(Rol rol) {
        this.rol = rol;
    }

    public Permiso getPermiso() {
        return permiso;
    }

    public void setPermiso(Permiso permiso) {
        this.permiso = permiso;
    }
}
