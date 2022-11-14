package microservicio.seguridad.MainSecurity.Repositorios;

import microservicio.seguridad.MainSecurity.Modelos.Rol;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface RepositorioRol extends MongoRepository<Rol,String>{
}
