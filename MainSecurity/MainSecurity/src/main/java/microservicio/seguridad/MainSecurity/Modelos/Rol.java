package microservicio.seguridad.MainSecurity.Modelos;

import lombok.Data;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

// Decorador, Para definir que esta clase sera almacenada en la base de datos.
@Data
@Document()

// Clase con atributos, creacion de tabla en mongo
public class Rol {
    @Id //Campo unico del documento
    private String _id;
    private String nombre;
    private String descripcion;

    // Constructor
    public Rol(String nombre, String descripcion) {
        this.nombre = nombre;
        this.descripcion = descripcion;
    }

    // Getter y Setter de la clase.
    // nos permiten leer y escribir los valores de nuestras variables privadas desde fuera de la clase donde fueron creadas.

    public String get_id() {
        return _id;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getDescripcion() {
        return descripcion;
    }

    public void setDescripcion(String descripcion) {
        this.descripcion = descripcion;
    }
}

