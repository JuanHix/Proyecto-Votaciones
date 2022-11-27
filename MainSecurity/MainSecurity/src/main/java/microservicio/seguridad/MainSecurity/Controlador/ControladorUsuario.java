package microservicio.seguridad.MainSecurity.Controlador;

import microservicio.seguridad.MainSecurity.Modelos.Usuario;
import microservicio.seguridad.MainSecurity.Modelos.Rol;
import microservicio.seguridad.MainSecurity.Repositorios.RepositorioUsuario;
import microservicio.seguridad.MainSecurity.Repositorios.RepositorioRol;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;

import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.util.List;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

// Clase que recibe las peticiones del cliente, crea e interactua los objetos que
// representan los modelos, manipulacion de las transacciones con la base de datos.

// Decoradores
@CrossOrigin                     // permite que se lleven acabo transacciones al servidor. desde pc.
@RestController                 // permite definir esta clase como puerta de entrada a servidor, para hacer CRUD
@RequestMapping("/usuarios")  // permite definir la sub ruta de acceso que utilizará para activar los métodos programados

public class ControladorUsuario {
    @Autowired
    private RepositorioUsuario miRepositorioUsuario;
    @Autowired
    private RepositorioRol miRepositorioRol;

    // Funcion Listar todos los elementos
    @GetMapping("")
    public List<Usuario> index() {
        return this.miRepositorioUsuario.findAll();
    }

    // Funcion Creacion nuevo Objeto
    @ResponseStatus(HttpStatus.CREATED)
    @PostMapping
    public Usuario create(@RequestBody Usuario infoUsuario) {
        infoUsuario.setContrasena(convertirSHA256(infoUsuario.getContrasena())); // Cifrado de contrasena
        return this.miRepositorioUsuario.save(infoUsuario);
    }

    // Funcion Listar por Objeto por Id
    @GetMapping("{id}")
    public Usuario show(@PathVariable String id) {
        Usuario usuarioActual = this.miRepositorioUsuario
                .findById(id)
                .orElse(null);
        return usuarioActual;
    }

    // Funcion Actualiza objeto por Id
    @PutMapping("{id}")
    public Usuario update(@PathVariable String id, @RequestBody Usuario infoUsuario) {
        Usuario usuarioActual = this.miRepositorioUsuario
                .findById(id)
                .orElse(null);
        if (usuarioActual != null) {
            usuarioActual.setSeudonimo(infoUsuario.getSeudonimo());
            usuarioActual.setCorreo(infoUsuario.getCorreo());
            usuarioActual.setContrasena(convertirSHA256(infoUsuario.getContrasena()));
            return this.miRepositorioUsuario.save(usuarioActual);
        } else {
            return null;
        }
    }

    // Funcion Elimina objeto por Id
    @ResponseStatus(HttpStatus.NO_CONTENT)
    @DeleteMapping("{id}")
    public void delete(@PathVariable String id) {
        Usuario usuarioActual = this.miRepositorioUsuario
                .findById(id)
                .orElse(null);
        if (usuarioActual != null) {
            this.miRepositorioUsuario.delete(usuarioActual);
        }
    }

    // Funcion Realiza el proceso de cifrado
    public String convertirSHA256(String password) {
        MessageDigest md = null;
        try {
            md = MessageDigest.getInstance("SHA-256");
        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
            return null;
        }
        byte[] hash = md.digest(password.getBytes());
        StringBuffer sb = new StringBuffer();
        for (byte b : hash) {
            sb.append(String.format("%02x", b));
        }
        return sb.toString();
    }

    // Función que añade un rol a un usuario

    @PutMapping("{id_usuario}/rol/{id_rol}")
    public Usuario asignarRolUsuario(@PathVariable String id_usuario,
                                     @PathVariable String id_rol) {
        Usuario usuarioActual = miRepositorioUsuario
                .findById(id_usuario)
                .orElse(null);
        Rol rolActual = miRepositorioRol
                .findById(id_rol)
                .orElse(null);
        if (usuarioActual != null && rolActual != null) {
            usuarioActual.setRol(rolActual);
            return miRepositorioUsuario.save(usuarioActual);
        } else {
            return null;
        }
    }

    // Validar el ingreso de algún usuario

    @PostMapping("/validar")
    public Usuario validate(@RequestBody Usuario infoUsuario,
                            final HttpServletResponse response)
            throws IOException {
        Usuario usuarioActual = miRepositorioUsuario.getUserByMail(infoUsuario.getCorreo());
        Usuario usuarioPorSeudonimo = miRepositorioUsuario.getUserBySeudonimo(infoUsuario.getSeudonimo());
        if(usuarioActual != null && usuarioActual.getContrasena()
                .equals(convertirSHA256(infoUsuario.getContrasena()))
                && usuarioPorSeudonimo.getSeudonimo() != null){
            usuarioActual.setContrasena((""));
            return usuarioActual;
        }else{
            response.sendError(HttpServletResponse.SC_UNAUTHORIZED);
            return null;
        }

    }

}

