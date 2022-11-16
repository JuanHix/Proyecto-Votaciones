package microservicio.seguridad.MainSecurity.Modelos;

import lombok.Data;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

// Decoradores, Para definir que esta clase sera almacenada en la base de datos.
@Data
@Document()

// Clase con atributos, creacion de tabla en mongo
public class Permiso {
    @Id                 //Campo unico del documento
    private String _id;
    private String url;
    private String metodo;

    // Constructor
    public Permiso(String url, String metodo) {
        this.url = url;
        this.metodo = metodo;
    }

    // Getter y Setter de la clase.
    // nos permiten leer y escribir los valores de nuestras variables privadas desde fuera de la clase donde fueron creadas.

    public String get_id() {
        return _id;
    }

    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }

    public String getMetodo() {
        return metodo;
    }

    public void setMetodo(String metodo) {
        this.metodo = metodo;
    }
}

