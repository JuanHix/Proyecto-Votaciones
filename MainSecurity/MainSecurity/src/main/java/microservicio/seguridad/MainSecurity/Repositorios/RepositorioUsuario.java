package microservicio.seguridad.MainSecurity.Repositorios;

import microservicio.seguridad.MainSecurity.Modelos.Usuario;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.mongodb.repository.Query;

// Hereda de MongoRepository
public interface RepositorioUsuario extends MongoRepository<Usuario,String>{
    @Query("{'correo':?0}")
    public Usuario getUserByMail(String correo);

    @Query("{'seudonimo':?0}")
    public Usuario getUserBySeudonimo(String seudonimo);
}

